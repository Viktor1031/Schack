färg_katalog= {
  0: "□",
  1: "■",
}
sträng_till_kolumn_katalog={
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
}
kolumn_till_sträng_katalog={
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
}

def sträng_position_till_vektor2(sträng):
    kolumn_sträng = sträng[0]  # Bokstaven, t.ex. "e"
    rad_sträng = sträng[1]     # Siffran, t.ex. "2"
    
    kolumn = sträng_till_kolumn_katalog[kolumn_sträng]
    rad = 8-int(rad_sträng)
    
    return (kolumn,rad)



#flyttfunktion förflyttning x, y per steg sen stopvärde så häst (+-1,+-2,1) (+-2,+-1,1)
#Bonde start 2 steg, krav moves=0. Flytt funktion (0,2,1)
#Bonde fram 1 steg, flytt funktion (0,1,1)
#Bonde sida krav(pjäs.x,pjäs.y)  

#Y mirror x mirror

def är_vektor2_i_matris(vektor2,matris):
    if (vektor2[0] in range(len(matris))) and (vektor2[1] in range(len(matris[0]))):
        return True
    return False

class FlyttGraf():
    def __init__(self, x, y, steg):
        self.x=x
        self.y=y
        self.steg=steg


class FlyttBeteende:
    def __init__(self, förälder, flytt_graf, kan_döda, krav_funktion=None):
        self.förälder=förälder
        self.kan_döda=kan_döda
        self.flytt_graf= flytt_graf
        self.krav_funktion = krav_funktion
    def ge_lista_på_möjliga_flyttar_med_krav(self):
        if self.krav_funktion==None:
            return self.ge_lista_på_möjliga_flyttar()
        return None
    
    def ge_lista_på_möjliga_flyttar(self):
        
        möjliga_flyttar=[]

        pjäs=self.förälder
        schack_position_matris=pjäs.förälder
        flytt_graf=self.flytt_graf
        
        x=pjäs.x
        y=pjäs.y
        
        steg=0
        kolliderat_med_pjäs=False
        utanför_matris=False
        
        while((utanför_matris==False) and (steg<flytt_graf.steg) and kolliderat_med_pjäs==False):
            print(f'x{x}:y{y}')
            x+=flytt_graf.x
            y+=flytt_graf.y
            steg+=1
            
            if är_vektor2_i_matris([x,y],schack_position_matris)==False:
                utanför_matris=True
                continue
                                   
            print(schack_position_matris[x][y].pjäs)
            
            if schack_position_matris[x][y].pjäs!=None:
                kolliderat_med_pjäs=True
                print(f'x{x}:y{y}')
                print("crash")
                if self.kan_döda==True:
                    möjliga_flyttar.append((x,y))
                continue
            
            möjliga_flyttar.append((x,y))
        return möjliga_flyttar
            
    
        
class Pjäs:
    def __init__(self, namn, karaktär, förälder, x, y, team):
        self.namn = namn
        self.karaktär = karaktär
        self.förälder=förälder
        self.x=x
        self.y=y
        self.team=team
        self.beteende_lista=[]
        self.moves=0

    
    def hämta_utseende_sträng(self):
        return self.karaktär
    
    def lägg_till_flytt_beteende(self,flytt_graf,kan_döda,krav_funktion=None):
        nytt_flytt_beteende=FlyttBeteende(self,flytt_graf,kan_döda,krav_funktion)
        self.beteende_lista.append(nytt_flytt_beteende)
        
    def ge_lista_på_alla_möjliga_flyttar(self):
        alla_möjliga_flyttar=[]
        for beteende in self.beteende_lista:
            alla_möjliga_flyttar+=beteende.ge_lista_på_möjliga_flyttar_med_krav()
        return alla_möjliga_flyttar
    
def skapa_pjäs_bonde(schack_bräde,x,y,vit):
    if vit==True:
        bonde=Pjäs("Vit Bonde","♙", schack_bräde, x, y, 0)
        bonde.lägg_till_flytt_beteende(FlyttGraf(0, -1, 1),False)
    else:
        bonde=Pjäs("Svart Bonde","♟", schack_bräde, x, y,1)
        bonde.lägg_till_flytt_beteende(FlyttGraf(0, 1, 1),False)
        
    schack_bräde[x][y].pjäs=bonde

def skapa_pjäs_löpare(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        löpare=Pjäs("Vit Löpare","♗", schack_bräde, x, y, 0)
        löpare.lägg_till_flytt_beteende(FlyttGraf(1, 1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(1, -1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 8),True)
        
    else:
        löpare=Pjäs("Svart Löpare","♝", schack_bräde, x, y,1)
        löpare.lägg_till_flytt_beteende(FlyttGraf(1, 1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(1, -1, 8),True)
        löpare.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 8),True)
        
    schack_bräde[x][y].pjäs=löpare
#♔	♕	♖	♗	♘	♙	♚	♛	♜	♝	♞	♟
    
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
        
def skapa_2d_matris(storlek): #Returnar en X*X matris, X=storlek
    matris = [[0 for ix in range(storlek)] for iy in range(storlek)]
    return matris

def fyll_2d_matris_med_tomma_schack_positioner(matris):
    for ix in range(len(matris)):
        for iy in range(len(matris[0])):
            matris[ix][iy]=SchackPosition()
    return matris

def gör_shack_position_matris_mönstrad(matris):
    for ix in range(len(matris)):
        for iy in range(len(matris[0])):
            matris[ix][iy].färg=(ix+iy)%2
    return matris
 
def placera_standard_pjäser_i_shack_position_matris(matris):
    skapa_pjäs_bonde(matris,0,6,True)
    skapa_pjäs_bonde(matris,0,5,False)
    skapa_pjäs_löpare(matris,3,3,False)
    
def skapa_standard_schackbräde_matris():
    schackbräde_matris=skapa_2d_matris(8)
    fyll_2d_matris_med_tomma_schack_positioner(schackbräde_matris)
    gör_shack_position_matris_mönstrad(schackbräde_matris)
    placera_standard_pjäser_i_shack_position_matris(schackbräde_matris)
    return schackbräde_matris

class SchackBräde():
    matris=skapa_standard_schackbräde_matris()
    
def rita_schack_bräde(schack_bräde):
    bräde_sträng=""
    for iy in range(len(schack_bräde.matris[0])):
        for ix in range(len(schack_bräde.matris)):
            schack_position=schack_bräde.matris[ix][iy]
            bräde_sträng+=schack_position.hämta_utseende_sträng()
        bräde_sträng+="\n"            
    print(bräde_sträng)

def välj_vektor_position_i_shack_bräde(schack_bräde):
    while True:
        print("Välj en pjäs genom att skriva in bokstav(kolumn) och siffra(rad). T.ex. e2) \n")
        vald_sträng_position=input()
        
        #try:
        if vald_sträng_position=="exit":
            exit()
        if len(vald_sträng_position)>1:
            if vald_sträng_position[0] in sträng_till_kolumn_katalog:
                 if int(vald_sträng_position[1]) in range(1,len(schack_bräde.matris)+1):
                     return sträng_position_till_vektor2(vald_sträng_position)
                 else:
                     print(f'Andra karaktären måste vara ett nummer {1}-{len(schack_bräde.matris)}')
            else:
                print("Första karaktären måste vara en liten bokstav a-h")
       # except:
           # print("Försök Igen!")
        
 

def spela_schack_match(schack_bräde):
    rita_schack_bräde(schack_bräde)
    match_pågår=True
    vald_position=None
    
    while match_pågår:
        vald_vektor=välj_vektor_position_i_shack_bräde(schack_bräde)
        vald_position=schack_bräde.matris[vald_vektor[0]][vald_vektor[1]]
        if vald_position.pjäs==None:
            vald_position=None     
        else:
            print(vald_position.pjäs.ge_lista_på_alla_möjliga_flyttar())
        print(vald_position)
    


spela_schack_match(SchackBräde())


