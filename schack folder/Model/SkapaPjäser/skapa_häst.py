from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs

def lägg_till_beetenden_för_häst(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -2, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, -1, 1),True)

def skapa_pjäs_häst(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        häst=Pjäs("Vit Häst","H", schack_bräde, x, y, 0) #♘
        lägg_till_beetenden_för_häst(häst)
    else:
        häst=Pjäs("Svart Häst","h", schack_bräde, x, y,1) #♞
        lägg_till_beetenden_för_häst(häst)
        
    schack_bräde[x][y].pjäs=häst