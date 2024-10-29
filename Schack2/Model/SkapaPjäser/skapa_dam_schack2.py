from Model.huvud_klasser import Pjäs
from Model.SkapaPjäser.skapa_löpare import lägg_till_beetenden_för_löpare
from Model.SkapaPjäser.skapa_torn import lägg_till_beetenden_för_torn
from Model.SkapaPjäser.skapa_bonde_schack2 import lägg_till_beetenden_för_bonde_schack2
def skapa_pjäs_dam_schack2(schack_bräde,x,y,vit,alla_drag_gjorda_lista): #Skirv inte schackbräde här
    if vit==True:
        dam=Pjäs("Vit Dam","D","wQ", schack_bräde, x, y, 0,9) #D♕
        lägg_till_beetenden_för_bonde_schack2(dam,vit,alla_drag_gjorda_lista)
        lägg_till_beetenden_för_löpare(dam)
    else:
        dam=Pjäs("Svart Dam","d","bQ", schack_bräde, x, y,1,9) #♛
        lägg_till_beetenden_för_bonde_schack2(dam,vit,alla_drag_gjorda_lista)
        lägg_till_beetenden_för_löpare(dam)

    schack_bräde[x][y].pjäs=dam
