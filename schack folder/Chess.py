from View.rita_schack_bräde import rita_schack_bräde
from Controller.välj_position_och_få_drag_lista_i_schackbräde_matris import välj_position_och_få_drag_lista_i_schackbräde_matris
from Controller.schack_funktionalitet import är_kung_i_schack, är_schackmatt
from Model.skapa_schack_bräde_funktioner import skapa_standard_schackbräde_matris
from Controller.välj_sträng_position_i_sträng_position_lista import välj_sträng_position_i_sträng_position_lista
from Controller.matris_funktioner import sträng_position_till_vektor2
from Controller.vektor2_sträng_konverterings_funktioner import konvertera_vektor2_lista_till_sträng_position_lista
from Controller.vektor2_sträng_konverterings_funktioner import vektor2_till_sträng_position

def spela_schack_match(schackbräde_matris):
    global drag_gjorda_drag_lista

    match_pågår = True
    nuvarande_spelare_färg = 0  # 0 = vit, 1 = svart
    totala_antal_drag=0
    drag_gjorda_drag_lista=[]
    while match_pågår:
        rita_schack_bräde(schackbräde_matris)
        print(f"{'Vit' if nuvarande_spelare_färg == 0 else 'Svart'} spelar")
        drag_lista = välj_position_och_få_drag_lista_i_schackbräde_matris(schackbräde_matris, nuvarande_spelare_färg)
        pjäs=drag_lista[0].pjäs

        print(f"Du har valt att flytta {vektor2_till_sträng_position([pjäs.x,pjäs.y])} {pjäs.namn}, detta är dina flyttalternativ:")
        
        flytt_alternativ_lista=[]
        for x in drag_lista:
            flytt_alternativ_lista.append(x.flytta_till_vektor2)
        
        flytt_alternativ_lista=konvertera_vektor2_lista_till_sträng_position_lista(flytt_alternativ_lista)
        print("Välj ditt drag:")
        print(flytt_alternativ_lista)

        vald_sträng_position = välj_sträng_position_i_sträng_position_lista(flytt_alternativ_lista)
        if vald_sträng_position !=None:
            vald_vektor2_position = sträng_position_till_vektor2(vald_sträng_position)
            print(f"Du flyttade {vektor2_till_sträng_position([pjäs.x,pjäs.y])} {pjäs.namn} till {vald_sträng_position}")
            for drag in drag_lista:
                if drag.flytta_till_vektor2[0]==vald_vektor2_position[0] and drag.flytta_till_vektor2[1]==vald_vektor2_position[1]:
                    drag.utför_flytt()
                    drag_gjorda_drag_lista.append(drag)
                    break

            totala_antal_drag+=1

            # Kolla schackcmatt
            motståndare_färg = 1 - nuvarande_spelare_färg
            if är_kung_i_schack(schackbräde_matris, motståndare_färg):
                if är_schackmatt(schackbräde_matris, motståndare_färg):
                    print(f"{'Vit' if nuvarande_spelare_färg == 0 else 'Svart'} vinner! Schackmatt!")
                    match_pågår = False
                else:
                    print(f"{'Vit' if motståndare_färg == 0 else 'Svart'} kung är i schack!")

            rev=input()
            rev_first=rev[0:3]
            rev_number=rev[3:]
            if rev_first=="rev":
                for x in range(int(rev_number)):
                    if len(drag_gjorda_drag_lista)>0:
                        drag_gjorda_drag_lista[-1].ta_tillbaka_flytt()
                        totala_antal_drag-=1
                        drag_gjorda_drag_lista.pop()
            #Byt spelaretu tru
            nuvarande_spelare_färg = motståndare_färg
            
            
        
standard_schackbräde_matris=skapa_standard_schackbräde_matris()
spela_schack_match(standard_schackbräde_matris)
