def rita_schack_bräde(schackbräde_matris):
    bräde_sträng=""
    for iy in range(len(schackbräde_matris[0])):
        for ix in range(len(schackbräde_matris)):
            schack_position=schackbräde_matris[ix][iy]
            bräde_sträng+=schack_position.hämta_utseende_sträng()+" "
        bräde_sträng+="\n"            
    print(bräde_sträng)
