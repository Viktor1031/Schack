from Model.huvud_klasser import Pjäs
from Model.SkapaPjäser.skapa_löpare import lägg_till_beetenden_för_löpare
from Model.SkapaPjäser.skapa_torn import lägg_till_beetenden_för_torn

def skapa_pjäs_dam(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        dam=Pjäs("Vit Dam","D","wQ", schack_bräde, x, y, 0,9) #D♕
        lägg_till_beetenden_för_torn(dam)
        lägg_till_beetenden_för_löpare(dam)
    else:
        dam=Pjäs("Svart Dam","d","bQ", schack_bräde, x, y,1,9) #♛
        lägg_till_beetenden_för_torn(dam)
        lägg_till_beetenden_för_löpare(dam)
    schack_bräde[x][y].pjäs=dam
