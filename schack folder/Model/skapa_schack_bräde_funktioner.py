from Model.huvud_klasser import SchackPosition
from Model.SkapaPjäser.skapa_bonde import skapa_pjäs_bonde
from Model.SkapaPjäser.skapa_torn import skapa_pjäs_torn
from Model.SkapaPjäser.skapa_häst import skapa_pjäs_häst
from Model.SkapaPjäser.skapa_löpare import skapa_pjäs_löpare
from Model.SkapaPjäser.skapa_dam import skapa_pjäs_dam
from Model.SkapaPjäser.skapa_kung import skapa_pjäs_kung
from Controller.matris_funktioner import skapa_2d_matris

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

def placera_standard_pjäser_i_shack_position_matris(matris):
    
    for ix in range(2,8):
        skapa_pjäs_bonde(matris,ix,3,True) #Vit=True
        
   # for iy in range(8):
     #   skapa_pjäs_bonde(matris,iy,1,False)

    skapa_pjäs_bonde(matris,1,1,False)

    #skapa_pjäs_löpare(matris,5,7,True)
    #skapa_pjäs_löpare(matris,2,7,True)
    #skapa_pjäs_löpare(matris,2,0,False)
    #skapa_pjäs_löpare(matris,5,0,False)
    
    #skapa_pjäs_häst(matris,1,7,True)
    #skapa_pjäs_häst(matris,6,7,True)
    #skapa_pjäs_häst(matris,1,0,False)
   # skapa_pjäs_häst(matris,6,0,False)
    
    
    skapa_pjäs_torn(matris,0,7,True)
    skapa_pjäs_torn(matris,7,7,True)
    skapa_pjäs_torn(matris,0,0,False)
    skapa_pjäs_torn(matris,7,0,False)
    
    #skapa_pjäs_dam(matris,3,7,True)
    #skapa_pjäs_dam(matris,3,0,False)
    
    skapa_pjäs_kung(matris,4,7,True)
    skapa_pjäs_kung(matris,4,0,False)
    