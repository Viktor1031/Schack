from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs

def lägg_till_beetenden_för_torn_schack2(pjäs, vit):
        if vit == True:
            pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 8),True)
            pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 8),True)
            pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 8),True)
        else:
            pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 8),True)
            pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 8),True)
            pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 8),True)
        
def skapa_pjäs_torn_schack2(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        torn=Pjäs("Vitt Torn","R","wR", schack_bräde, x, y, 0,4) #♖
        lägg_till_beetenden_för_torn_schack2(torn, vit)
    else:
        torn=Pjäs("Svart Torn","r","bR", schack_bräde, x, y,1,4) #♜
        lägg_till_beetenden_för_torn_schack2(torn, vit)
        
    schack_bräde[x][y].pjäs=torn