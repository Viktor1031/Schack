from .vektor2_sträng_konverterings_funktioner import sträng_position_till_vektor2
from Model.kataloger import sträng_till_kolumn_katalog

def skapa_2d_matris(kolumner,rader): #Returnar en X*X matris, X=storlek
    matris = [[0 for ix in range(rader)] for iy in range(kolumner)]
    return matris


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
            return 2 #Sluta grafen, men lägg till pjäs
        else:
            return False
    return True


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