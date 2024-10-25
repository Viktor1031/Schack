from .matris_funktioner import välj_vektor2_position_i_matris
from .schack_funktionalitet import ta_bort_drag_som_leder_till_egen_kung_i_schack

def välj_position_och_få_drag_lista_i_schackbräde_matris(schackbräde_matris, nuvarande_spelare_färg):
    while True:
        print("Välj en pjäs genom att skriva in bokstav(kolumn) och siffra(rad), t.ex. e2:")
        vald_vektor = välj_vektor2_position_i_matris(schackbräde_matris)
        if vald_vektor != None:
            vald_position = schackbräde_matris[vald_vektor[0]][vald_vektor[1]]

            if vald_position.pjäs != None:
                if vald_position.pjäs.färg != nuvarande_spelare_färg:
                   # print("Du kan inte flytta motståndarens pjäs!")
                    continue
                drag_alternativ = vald_position.pjäs.ge_lista_på_alla_möjliga_drag()
                drag_alternativ = ta_bort_drag_som_leder_till_egen_kung_i_schack(drag_alternativ)
                #print(drag_alternativ)
                if len(drag_alternativ)<1:
                    ("Inga giltiga drag för denna pjäs.")
                    continue
                return drag_alternativ
            else:
                print("Ingen pjäs på vald position.")
        else:
            print("Ogiltig position, försök igen.")
