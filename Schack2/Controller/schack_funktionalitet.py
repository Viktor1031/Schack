def är_kung_i_schack(schackbräde_matris, färg):
    kung_position = None
    for ix in range(len(schackbräde_matris)):
        for iy in range(len(schackbräde_matris[0])):
            pjäs = schackbräde_matris[ix][iy].pjäs
            if pjäs and pjäs.namn == ("Vit Kung" if färg == 0 else "Svart Kung"):
                kung_position = (ix, iy)
                break
        if kung_position:
            break  

    if not kung_position:
        return False 

    for ix in range(len(schackbräde_matris)):
        for iy in range(len(schackbräde_matris[0])):
            pjäs = schackbräde_matris[ix][iy].pjäs
            if pjäs and pjäs.färg != färg:
                möjliga_drag = pjäs.ge_lista_på_alla_möjliga_drag()

                möjliga_positioner=[]
                for drag in möjliga_drag:
                    möjliga_positioner.append(drag.flytta_till_vektor2)

                if kung_position in möjliga_positioner:
                    return True  # Kungen är i schack
    return False  # Kungen är inte i schack

def är_schackmatt(schackbräde_matris, färg):
    
    for ix in range(len(schackbräde_matris)):
        for iy in range(len(schackbräde_matris[0])):
            pjäs = schackbräde_matris[ix][iy].pjäs
            if pjäs and pjäs.färg == färg:
                möjliga_drag = pjäs.ge_lista_på_alla_möjliga_drag()
                möjliga_drag = ta_bort_drag_som_leder_till_egen_kung_i_schack(möjliga_drag)
                if len(möjliga_drag)>0:
                    print(möjliga_drag)
                    return False  # Det finns minst ett drag som kan undvika schack
    
    return True  # Ingen pjäs kan flyttas för att undvika schack, det är schackmatt

def ta_bort_drag_som_leder_till_egen_kung_i_schack(drag_lista):
    giltiga_drag= []

    for drag in drag_lista:

        drag.utför_flytt()

        if not är_kung_i_schack(drag.schackbräde_matris, drag.pjäs.färg):
            giltiga_drag.append(drag)

        drag.ta_tillbaka_flytt()

    return giltiga_drag
