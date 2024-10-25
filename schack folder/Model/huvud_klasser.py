from Model.kataloger import färg_katalog
from Controller.matris_funktioner import är_vektor2_i_matris, är_vektor2_en_icke_valid_kollision_med_annan_pjäs

class Drag():
    def __init__(self, pjäs, schackbräde_matris, flytta_till_vektor2,resultat_funktion=None):
        self.pjäs = pjäs
        self.flytta_till_vektor2 = flytta_till_vektor2
        self.schackbräde_matris = schackbräde_matris
        self.förra_positionen_vektor2=None
        self.förra_positionen_pjäs=None
        self.resultat_funktion=resultat_funktion
        self.fångad_pjäs = None  # Lägg till denna rad
    def utför_flytt(self):

        vald_schack_position=self.schackbräde_matris[self.flytta_till_vektor2[0]][self.flytta_till_vektor2[1]]

        start_schack_position=self.schackbräde_matris[self.pjäs.x][self.pjäs.y]
        self.förra_positionen_vektor2=[self.pjäs.x,self.pjäs.y]
        self.förra_positionen_pjäs=vald_schack_position.pjäs
        start_schack_position.pjäs=None

        vald_schack_position.pjäs=self.pjäs
        
        self.pjäs.x=self.flytta_till_vektor2[0]
        self.pjäs.y=self.flytta_till_vektor2[1]
        self.pjäs.drag+=1
        
        if self.resultat_funktion!=None:
            self.resultat_funktion(self)

    def ta_tillbaka_flytt(self):
        flytta_tillbaka_position=self.schackbräde_matris[self.förra_positionen_vektor2[0]][self.förra_positionen_vektor2[1]]

        start_schack_position=self.schackbräde_matris[self.pjäs.x][self.pjäs.y]
        start_schack_position.pjäs=self.förra_positionen_pjäs

        flytta_tillbaka_position.pjäs=self.pjäs
        
        self.pjäs.x=self.förra_positionen_vektor2[0]
        self.pjäs.y=self.förra_positionen_vektor2[1]
        self.pjäs.drag-=1
        if self.resultat_funktion!=None:
            self.resultat_funktion(self,ta_tillbaka=True)

class SchackPosition:
    def __init__(self, färg=0, pjäs=None):

        self.färg = färg #0=Svart, 1=Vit
        self.pjäs = pjäs #None=Tom, annars pjäs

    def placera_pjäs(self, pjäs):
        self.pjäs = pjäs

    def ta_bort_pjäs(self):
        self.pjäs = None
        
    def hämta_utseende_sträng(self):
        if self.pjäs==None:
            return färg_katalog[self.färg]   
        return self.pjäs.hämta_utseende_sträng()


class Villkor:
    def __init__(self, villkors_funktion, **villkor_keyword_argument):
        self.villkors_funktion = villkors_funktion
        self.villkor_keyword_argument = villkor_keyword_argument
    
    def kolla_villkor(self, **extra_keyword_arguments):
        alla_keyword_argument = {**extra_keyword_arguments, **self.villkor_keyword_argument}
        return self.villkors_funktion(**alla_keyword_argument)

class FlyttGraf():
    
    def __init__(self, kx, ky, antal_steg):
        self.kx=kx
        self.ky=ky
        self.antal_steg=antal_steg
        
    def hitta_graf_punkter(self,start_vektor2, graf_villkor_lista):
        
        graf_punkter=[]
    
        x=start_vektor2[0]
        y=start_vektor2[1]
        
        for steg in range(self.antal_steg):
            
            x+=self.kx
            y+=self.ky
            steg+=1
            
            for graf_villkor in graf_villkor_lista:
                villkor_resultat=graf_villkor.kolla_villkor(vektor2=[x,y])
                
                if villkor_resultat==False:
                    return graf_punkter
                elif villkor_resultat==2:
                    graf_punkter.append((x,y))
                    return graf_punkter
                
            graf_punkter.append((x,y))
            
        return graf_punkter

class FlyttBeteende:
    def __init__(self, flytt_graf, kan_döda, beetende_villkor_lista, resultat_funktion):
        self.kan_döda=kan_döda
        self.flytt_graf= flytt_graf
        self.beetende_villkor_lista = beetende_villkor_lista
        self.resultat_funktion=resultat_funktion
        
    def ge_lista_på_möjliga_drag_med_krav(self,pjäs):

        for beetende_villkor in self.beetende_villkor_lista:
            if (beetende_villkor.kolla_villkor(pjäs=pjäs, schackbräde_matris=pjäs.förälder))==False:
                return []
        
        villkor_inanför_matris=Villkor(är_vektor2_i_matris, matris=pjäs.förälder)
        villkor_kollision=Villkor(är_vektor2_en_icke_valid_kollision_med_annan_pjäs,schackbräde_matris=pjäs.förälder, beteende=self, pjäs=pjäs)

        
        möjliga_flytt_punkter=self.flytt_graf.hitta_graf_punkter((pjäs.x,pjäs.y),[villkor_inanför_matris,villkor_kollision])
        lista_av_drag=[]
            
        for flytt_punk in möjliga_flytt_punkter:
            lista_av_drag.append(Drag(pjäs, pjäs.förälder, flytt_punk,resultat_funktion=self.resultat_funktion))
            #lista_av_drag.append(flytt_punk)
        return lista_av_drag
        
       
class Pjäs:
    def __init__(self, namn, karaktär, förälder, x, y, färg):
        self.namn = namn
        self.karaktär = karaktär
        self.förälder=förälder
        self.x=x
        self.y=y
        self.färg=färg
        self.beteende_lista=[]
        self.drag=0
        self.senaste_draget=0
    
    def hämta_utseende_sträng(self):
        return self.karaktär
    
    def lägg_till_flytt_beteende(self,flytt_graf,kan_döda,beetende_villkor=[],resultat_funktion=None):
        nytt_flytt_beteende=FlyttBeteende(flytt_graf,kan_döda,beetende_villkor,resultat_funktion)
        self.beteende_lista.append(nytt_flytt_beteende)
        
    def ge_lista_på_alla_möjliga_drag(self):
        alla_möjliga_drag=[]
        for beteende in self.beteende_lista:
            alla_möjliga_drag+=beteende.ge_lista_på_möjliga_drag_med_krav(self)
        return alla_möjliga_drag
