from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs
from Model.SkapaPjäser.skapa_häst import lägg_till_beetenden_för_häst
from Model.SkapaPjäser.skapa_löpare import lägg_till_beetenden_för_löpare

def lägg_till_beetenden_för_torn(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 8),True)

        
def skapa_pjäs_knook(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        torn=Pjäs("Vitt Knook","R","wKnook", schack_bräde, x, y, 0,7) #♖
        lägg_till_beetenden_för_torn(torn)
        lägg_till_beetenden_för_häst(torn)
    else:
        torn=Pjäs("Svart Knook","r","bKnook", schack_bräde, x, y,1,7) #♜
        lägg_till_beetenden_för_torn(torn)
        lägg_till_beetenden_för_häst(torn)

    schack_bräde[x][y].pjäs=torn