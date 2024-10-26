from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs
def lägg_till_beetenden_för_löpare(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 8),True)

def skapa_pjäs_löpare(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        löpare=Pjäs("Vit Löpare","L","wB", schack_bräde, x, y, 0) #♗
        lägg_till_beetenden_för_löpare(löpare)
        
    else:
        löpare=Pjäs("Svart Löpare","l","bB", schack_bräde, x, y,1) #♝
        lägg_till_beetenden_för_löpare(löpare)
        
    schack_bräde[x][y].pjäs=löpare