from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs
from Controller.SpecialDrag.rockad import resultat_funktion_kort_rockad,resultat_funktion_lång_rockad
from Controller.SpecialDrag.rockad import flytt_beetende_krav_kort_rockad,flytt_beetende_krav_lång_rockad
from Controller.allmäna_flytt_beetende_krav import flytt_beetende_krav_är_detta_pjäsens_första_drag

def lägg_till_beetenden_för_kung(pjäs):
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 0, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 0, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 1),True)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(2, 0, 1),True,[Villkor(flytt_beetende_krav_kort_rockad),Villkor(flytt_beetende_krav_är_detta_pjäsens_första_drag)],resultat_funktion_kort_rockad)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-2, 0, 1),True,[Villkor(flytt_beetende_krav_lång_rockad),Villkor(flytt_beetende_krav_är_detta_pjäsens_första_drag)],resultat_funktion_lång_rockad)
def skapa_pjäs_kung(schack_bräde,x,y,vit): #Skirv inte schackbräde här
    if vit==True:
        kung=Pjäs("Vit Kung","K","wK", schack_bräde, x, y, 0,0) #♔
        lägg_till_beetenden_för_kung(kung)
    else:
        kung=Pjäs("Svart Kung","k","bK", schack_bräde, x, y,1,0) #♚
        lägg_till_beetenden_för_kung(kung)
        
    schack_bräde[x][y].pjäs=kung