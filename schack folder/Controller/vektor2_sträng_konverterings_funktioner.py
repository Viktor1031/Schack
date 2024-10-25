
from Model.kataloger import kolumn_till_sträng_katalog, sträng_till_kolumn_katalog
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
