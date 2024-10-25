from Model.huvud_klasser import FlyttGraf,Villkor,Pjäs
from Controller.SpecialDrag.bonde_promotion import resultat_funktion_gör_bonde_till_drottning
from Controller.SpecialDrag.en_passant import resultat_funktion_en_passant,flytt_beetende_krav_en_passant
from Controller.allmäna_flytt_beetende_krav import flytt_beetende_krav_är_detta_pjäsens_första_drag,flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs

def lägg_till_beetenden_för_bonde(pjäs, vit):
    if vit==True:
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -1, 1),False,[],resultat_funktion_gör_bonde_till_drottning)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, -2, 1),False,[Villkor(flytt_beetende_krav_är_detta_pjäsens_första_drag)])
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 1),True,[Villkor(flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs,vektor2_position=[-1, -1])],resultat_funktion_gör_bonde_till_drottning)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 1),True,[Villkor(flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs,vektor2_position=[1, -1])],resultat_funktion_gör_bonde_till_drottning)

        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, -1, 1), True, [Villkor(flytt_beetende_krav_en_passant, vektor2_position=[-1, -1])], resultat_funktion_en_passant)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, -1, 1), True, [Villkor(flytt_beetende_krav_en_passant, vektor2_position=[1, -1])], resultat_funktion_en_passant)

    else:
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 1, 1),False)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(0, 2, 1),False,[Villkor(flytt_beetende_krav_är_detta_pjäsens_första_drag)])
        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 1),True,[Villkor(flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs,vektor2_position=[-1, 1])])
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 1),True,[Villkor(flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs,vektor2_position=[1, 1])])

        pjäs.lägg_till_flytt_beteende(FlyttGraf(-1, 1, 1), True, [Villkor(flytt_beetende_krav_en_passant, vektor2_position=[-1, 1])], resultat_funktion_en_passant)
        pjäs.lägg_till_flytt_beteende(FlyttGraf(1, 1, 1), True, [Villkor(flytt_beetende_krav_en_passant, vektor2_position=[1, 1])], resultat_funktion_en_passant)

def skapa_pjäs_bonde(schack_bräde,x,y,vit):
    if vit==True:
        bonde=Pjäs("Vit Bonde","B", schack_bräde, x, y, 0,) #♙
        lägg_till_beetenden_för_bonde(bonde,vit)
    else:
        bonde=Pjäs("Svart Bonde","b", schack_bräde, x, y,1) #♟
        lägg_till_beetenden_för_bonde(bonde,vit)
        
    schack_bräde[x][y].pjäs=bonde