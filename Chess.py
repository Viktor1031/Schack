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
    "i" : 8,
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
    8 : "i",
}

def sträng_position_till_vektor2(sträng):
    
    kolumn_sträng = sträng[0]  # Bokstaven, t.ex. "e"
    rad_sträng = sträng[1]     # Siffran, t.ex. "2"
    
    kolumn = sträng_till_kolumn_katalog[kolumn_sträng]
    rad = 8-int(rad_sträng)
    
    return [kolumn,rad]

def vektor2_till_sträng_position(vektor2):
    kolumn = vektor2[0]  # Ex. 4 för kolumn
    rad = vektor2[1]     # Ex. 6 för rad
    
    kolumn_sträng = kolumn_till_sträng_katalog[kolumn]
    rad_sträng = str(8 - rad)  # Omvandlar rad till motsvarande sträng
    
    return kolumn_sträng + rad_sträng

def konvertera_vektor2_lista_till_sträng_position_lista(vektor2_lista):
    sträng_position_lista=[]
    for vektor2 in vektor2_lista:
        sträng_position_lista.append(vektor2_till_sträng_position(vektor2))
    return sträng_position_lista

def är_vektor2_i_matris(vektor2, matris):
    if (vektor2[0] in range(len(matris))) and (vektor2[1] in range(len(matris[0]))):
        return True
    return False

def är_vektor2_en_icke_valid_kollision_med_annan_pjäs(vektor2, schackbräde_matris, beteende, pjäs):
    
    x=vektor2[0]
    y=vektor2[1]
    
    annan_pjäs=schackbräde_matris[x][y].pjäs
    
    if annan_pjäs!=None:
        if (beteende.kan_döda==True) and (annan_pjäs.färg!=pjäs.färg):
            return True
        else:
            return False
    return True
            
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
        graf_är_klar=False
    
        x=start_vektor2[0]
        y=start_vektor2[1]
        
        for steg in range(self.antal_steg):
            
            x+=self.kx
            y+=self.ky
            steg+=1
            
            for graf_villkor in graf_villkor_lista:
                if graf_villkor.kolla_villkor(vektor2=[x,y])==False:
                    return graf_punkter
                
            graf_punkter.append((x,y))
            
        return graf_punkter


class FlyttBeteende:
    def __init__(self, flytt_graf, kan_döda, krav_funktion=None):
        self.kan_döda=kan_döda
        self.flytt_graf= flytt_graf
        self.krav_funktion = krav_funktion
        
    def ge_vektor2_lista_på_möjliga_flyttar_med_krav(self,pjäs):
        if self.krav_funktion==None:
            villkor_inanför_matris=Villkor(är_vektor2_i_matris, matris=pjäs.förälder)
            villkor_kollision=Villkor(är_vektor2_en_icke_valid_kollision_med_annan_pjäs,schackbräde_matris=pjäs.förälder, beteende=self, pjäs=pjäs)
            return self.flytt_graf.hitta_graf_punkter((pjäs.x,pjäs.y),[villkor_inanför_matris,villkor_kollision])
        return None
       
class Pjäs:
    def __init__(self, namn, karaktär, förälder, x, y, färg):
        self.namn = namn
        self.karaktär = karaktär
        self.förälder=förälder
        self.x=x
        self.y=y
        self.färg=färg
        self.beteende_lista=[]
        self.moves=0

    
    def hämta_utseende_sträng(self):
        return self.karaktär
    
    def lägg_till_flytt_beteende(self,flytt_graf,kan_döda,krav_funktion=None):
        nytt_flytt_beteende=FlyttBeteende(flytt_graf,kan_döda,krav_funktion)
        self.beteende_lista.append(nytt_flytt_beteende)
        
    def ge_vektor2_lista_på_alla_möjliga_flyttar(self):
        alla_möjliga_flyttar=[]
        for beteende in self.beteende_lista:
            alla_möjliga_flyttar+=beteende.ge_vektor2_lista_på_möjliga_flyttar_med_krav(self)
        return alla_möjliga_flyttar


def lägg_till_beetenden_för_bonde(pjäs):
    pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 1),False)
    
def skapa_pjäs_bonde(schack_bräde,x,y,vit):
    if vit==True:
        bonde=Pjäs("Vit Bonde","♙", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_bonde(bonde)
    else:
        bonde=Pjäs("Svart Bonde","♟", schack_bräde, x, y,1)
        lägg_till_beetenden_för_bonde(bonde)
        
    schack_bräde[x][y].pjäs=bonde

def lägg_till_beetenden_för_löpare(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 8),True)

def skapa_pjäs_löpare(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        löpare=Pjäs("Vit Löpare","♗", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_löpare(löpare)
        
    else:
        löpare=Pjäs("Svart Löpare","♝", schack_bräde, x, y,1)
        lägg_till_beetenden_för_löpare(löpare)
        
    schack_bräde[x][y].pjäs=löpare

def lägg_till_beetenden_för_häst(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, -1, 1),True)

def skapa_pjäs_häst(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        häst=Pjäs("Vit Häst","♘", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_häst(häst)
    else:
        häst=Pjäs("Svart Häst","♞", schack_bräde, x, y,1)
        lägg_till_beetenden_för_häst(häst)
        
    schack_bräde[x][y].pjäs=häst
    
def lägg_till_beetenden_för_torn(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 8),True)
        
def skapa_pjäs_torn(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        torn=Pjäs("Vitt Torn","♖", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_torn(torn)
    else:
        torn=Pjäs("Svart Torn","♜", schack_bräde, x, y,1)
        lägg_till_beetenden_för_torn(torn)
        
    schack_bräde[x][y].pjäs=torn
    
    
def skapa_pjäs_dam(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        dam=Pjäs("Vit Dam","♕", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_torn(dam)
        lägg_till_beetenden_för_löpare(dam)
    else:
        dam=Pjäs("Svart Dam","♛", schack_bräde, x, y,1)
        lägg_till_beetenden_för_torn(dam)
        lägg_till_beetenden_för_löpare(dam)
    schack_bräde[x][y].pjäs=dam

def lägg_till_beetenden_för_kung(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 1),True)

def skapa_pjäs_kung(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        kung=Pjäs("Vit Kung","♔", schack_bräde, x, y, 0)
        lägg_till_beetenden_för_kung(kung)
    else:
        kung=Pjäs("Svart Kung","♚", schack_bräde, x, y,1)
        lägg_till_beetenden_för_kung(kung)
        
    schack_bräde[x][y].pjäs=kung
    

    
    
def placera_standard_pjäser_i_shack_position_matris(matris):
    
    for ix in range(8):
        skapa_pjäs_bonde(matris,ix,6,True) #Vit=True
        
    for iy in range(8):
        skapa_pjäs_bonde(matris,iy,1,False)
        
    skapa_pjäs_löpare(matris,5,7,True)
    skapa_pjäs_löpare(matris,2,7,True)
    skapa_pjäs_löpare(matris,2,0,False)
    skapa_pjäs_löpare(matris,5,0,False)
    
    skapa_pjäs_häst(matris,1,7,True)
    skapa_pjäs_häst(matris,6,7,True)
    skapa_pjäs_häst(matris,1,0,False)
    skapa_pjäs_häst(matris,6,0,False)
    
    
    skapa_pjäs_torn(matris,0,7,True)
    skapa_pjäs_torn(matris,7,7,True)
    skapa_pjäs_torn(matris,0,0,False)
    skapa_pjäs_torn(matris,7,0,False)
    
    skapa_pjäs_dam(matris,3,7,True)
    skapa_pjäs_dam(matris,3,0,False)
    
    skapa_pjäs_kung(matris,4,7,True)
    skapa_pjäs_kung(matris,4,0,False)
    
    
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
        
def skapa_2d_matris(kolumner,rader): #Returnar en X*X matris, X=storlek
    matris = [[0 for ix in range(rader)] for iy in range(kolumner)]
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

    
def skapa_standard_schackbräde_matris():
    schackbräde_matris=skapa_2d_matris(8,8)
    fyll_2d_matris_med_tomma_schack_positioner(schackbräde_matris)
    gör_shack_position_matris_mönstrad(schackbräde_matris)
    placera_standard_pjäser_i_shack_position_matris(schackbräde_matris)
    return schackbräde_matris
    
def rita_schack_bräde(schackbräde_matris):
    bräde_sträng=""
    for iy in range(len(schackbräde_matris[0])):
        for ix in range(len(schackbräde_matris)):
            schack_position=schackbräde_matris[ix][iy]
            bräde_sträng+=schack_position.hämta_utseende_sträng()
        bräde_sträng+="\n"            
    print(bräde_sträng)


def välj_vektor2_position_i_matris(matris):

        vald_sträng_position=input()
        
        max_bredd=len(matris)
        max_höjd=len(matris[0])
        
        try:
            if len(vald_sträng_position)>1:
                if vald_sträng_position[0] in sträng_till_kolumn_katalog:
                     if int(vald_sträng_position[1]) in range(1,max_bredd+1):
                         return sträng_position_till_vektor2(vald_sträng_position)
                     else:
                         print(f'Andra karaktären måste vara ett nummer {1}-{max_bredd}')
                else:
                    print(f'Första karaktären måste vara en liten bokstav {sträng_till_kolumn_katalog[0]}-{sträng_till_kolumn_katalog[max_höjd]}')
        except:
           print("Försök Igen!")

def välj_sträng_position_i_sträng_position_lista(sträng_position_lista):
        vald_sträng_position=input()
        try:
            if len(vald_sträng_position)==2:
                if vald_sträng_position in sträng_position_lista:
                    return(sträng_position_lista[sträng_position_lista.index(vald_sträng_position)])
                else:
                    print(f'Strängen du skrev in finns inte med i listan av alternativ')
            else:
                print(f'Strängen du skriver in ska vara 2 karaktärer lång')
        except:
           print("Fanns inget sådant drag att välja")

class FlyttObjekt():
        def __init__(self, pjäs, start_schack_position, schackbräde_matris, start_vektor2, vektor2_lista_flytt_alternativ, ):
            self.pjäs = pjäs
            self.start_schack_position=start_schack_position
            self.schackbräde_matris = schackbräde_matris
            self.start_vektor2 = start_vektor2
            self.vektor2_lista_flytt_alternativ = vektor2_lista_flytt_alternativ
            self.sträng_position_lista_flytt_alternativ=konvertera_vektor2_lista_till_sträng_position_lista(vektor2_lista_flytt_alternativ)
        
        def utför_flytt(self,vald_vektor2):
            vald_schack_position=self.schackbräde_matris[vald_vektor2[0]][vald_vektor2[1]]
            self.start_schack_position.pjäs=None
            vald_schack_position.pjäs=self.pjäs
            self.pjäs.x=vald_vektor2[0]
            self.pjäs.y=vald_vektor2[1]
            

def välj_position_och_få_flytt_objekt_i_schackbräde_matris(schackbräde_matris):
    while True:
        print("Välj en pjäs genom att skriva in bokstav(kolumn) och siffra(rad). T.ex. e2) \n")
        vald_vektor=välj_vektor2_position_i_matris(schackbräde_matris)
        if vald_vektor!=None: #Om man ej valt en position
            vald_position=schackbräde_matris[vald_vektor[0]][vald_vektor[1]]
            
            if vald_position.pjäs!=None:
                vektor2_lista_flytt_alternativ=vald_position.pjäs.ge_vektor2_lista_på_alla_möjliga_flyttar()
                return FlyttObjekt(vald_position.pjäs,vald_position,schackbräde_matris,vald_vektor,vektor2_lista_flytt_alternativ)



def spela_schack_match(schackbräde_matris):
    match_pågår=True

    
    while match_pågår:
        rita_schack_bräde(schackbräde_matris)
        flytt_objekt=välj_position_och_få_flytt_objekt_i_schackbräde_matris(schackbräde_matris)
        rita_schack_bräde(schackbräde_matris)
        
        print(f'Du har valt att flytta {vektor2_till_sträng_position(flytt_objekt.start_vektor2)} {flytt_objekt.pjäs.namn}, detta är dina flytt alternativ: ')
        print(flytt_objekt.sträng_position_lista_flytt_alternativ)
        vald_sträng_position=välj_sträng_position_i_sträng_position_lista(flytt_objekt.sträng_position_lista_flytt_alternativ)
        if vald_sträng_position!=None:
            vald_vektor2_position=sträng_position_till_vektor2(vald_sträng_position)
            print(f'Du flyttade {vektor2_till_sträng_position(flytt_objekt.start_vektor2)} {flytt_objekt.pjäs.namn} till {vald_sträng_position}')
            print(vald_vektor2_position)
            flytt_objekt.utför_flytt(vald_vektor2_position)
        
standard_schackbräde_matris=skapa_standard_schackbräde_matris()
spela_schack_match(standard_schackbräde_matris)

#Tänk kring att ha en lista på flyttkrav istället för att hardcoda saker i while. *check
#Snygga till kod, ta bort onödiga moment *check

#Kolla lag när man kan döda *check
#Flytt alternativ *check
#Flytt funktionalitet *check
#Skriv baser för pjäser
#Löpare *check
#Häst *check
#Torn *check
#Dam *check
#Bonde 1 fram *check
#Bonde 2 fram
#Bonde ta åt sidan

#kommentera lite.
#Positionera pjäser
#Varanan tur system
#Kan ej flytta motståndares pjäs under sin tur.

#Beetende utökning? Resultat funktion?
#Bonde till drottning
#Rookad
#Schack funktionalitet med kungen
#En passant