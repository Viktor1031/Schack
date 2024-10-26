from Controller.matris_funktioner import är_vektor2_i_matris

def flytt_beetende_krav_en_passant(schackbräde_matris, pjäs, vektor2_position,alla_drag_gjorda_lista):



    x = pjäs.x + vektor2_position[0]
    y = pjäs.y + vektor2_position[1]

    if not är_vektor2_i_matris([x, y], schackbräde_matris):
        return False

    # Kontrollera att målrutan är tom
    if schackbräde_matris[x][y].pjäs is not None:
        return False

    # Kontrollera om det finns en motståndarbonde bredvid som kan fångas en passant
    enemy_x = x
    enemy_y = pjäs.y

    if not är_vektor2_i_matris([enemy_x, enemy_y], schackbräde_matris):
        return False

    enemy_pjäs = schackbräde_matris[enemy_x][enemy_y].pjäs

    if enemy_pjäs is None:
        return False

    if enemy_pjäs.namn != ("Svart Bonde" if pjäs.färg == 0 else "Vit Bonde"):
        return False

    # Kontrollera om motståndarbonden just har flyttat två steg framåt
    if len(alla_drag_gjorda_lista) == 0:
        return False

    senaste_drag = alla_drag_gjorda_lista[-1]

    if senaste_drag.pjäs != enemy_pjäs:
        return False

    if abs(senaste_drag.förra_positionen_vektor2[1] - senaste_drag.flytta_till_vektor2[1]) != 2:
        return False

    # Alla villkor för en passant är uppfyllda
    return True


# Lägg till denna funktion för att hantera resultatet av en passant-draget
def resultat_funktion_en_passant(drag, ta_tillbaka=False):
    x = drag.flytta_till_vektor2[0]
    y = drag.flytta_till_vektor2[1]

    if drag.pjäs.färg == 0:  # Vit bonde
        enemy_y = y + 1
    else:  # Svart bonde
        enemy_y = y - 1

    enemy_pawn_position = drag.schackbräde_matris[x][enemy_y]

    if not ta_tillbaka:
        # Ta bort motståndarens bonde
        drag.fångad_pjäs = enemy_pawn_position.pjäs
        enemy_pawn_position.pjäs = None
    else:
        # Återställ motståndarens bonde
        enemy_pawn_position.pjäs = drag.fångad_pjäs
        drag.fångad_pjäs = None