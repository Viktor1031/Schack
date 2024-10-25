from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs

def lägg_till_beetenden_för_torn(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 8),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 8),True)
        
def skapa_pjäs_torn(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        torn=Pjäs("Vitt Torn","T", schack_bräde, x, y, 0) #♖
        lägg_till_beetenden_för_torn(torn)
    else:
        torn=Pjäs("Svart Torn","t", schack_bräde, x, y,1) #♜
        lägg_till_beetenden_för_torn(torn)
        
    schack_bräde[x][y].pjäs=torn