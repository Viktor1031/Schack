from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs
def lägg_till_beetenden_för_elefant(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, -2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, -2, 1),True)

def skapa_pjäs_elefant(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        elefant=Pjäs("Vit Elefant","E","wElefant", schack_bräde, x, y, 0,2) #♗
        lägg_till_beetenden_för_elefant(elefant)
        
    else:
        elefant=Pjäs("Svart Elefant","e","bElefant", schack_bräde, x, y,1,2) #♝
        lägg_till_beetenden_för_elefant(elefant)
        
    schack_bräde[x][y].pjäs=elefant