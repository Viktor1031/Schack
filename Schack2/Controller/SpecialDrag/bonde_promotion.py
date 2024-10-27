from Model.SkapaPjäser.skapa_dam import skapa_pjäs_dam

def resultat_funktion_gör_bonde_till_drottning(drag, ta_tillbaka=False):
    if ta_tillbaka == False:
        schackbräde_matris = drag.schackbräde_matris
        x, y = drag.flytta_till_vektor2
        
        if drag.pjäs.färg == 0:  # Vit
            if y == 0:
                skapa_pjäs_dam(schackbräde_matris, x, y, True)
        else:  # Svart
            if y == 7:
                skapa_pjäs_dam(schackbräde_matris, x, y, False)

    else:
        # Återställ bonden
        
        schackbräde_matris = drag.schackbräde_matris
        x, y = drag.förra_positionen_vektor2
        if drag.pjäs.färg == 0:  # Vit
            if y == 0:
                schackbräde_matris[x][y].pjäs=None
        else:  # Svart
            if y == 7:
                schackbräde_matris[x][y].pjäs=None

