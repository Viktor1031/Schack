from Controller.matris_funktioner import är_vektor2_i_matris

def flytt_beetende_krav_är_detta_pjäsens_första_drag(pjäs,schackbräde_matris):
    if pjäs.drag==0:
        return True
    return False

def flytt_beetende_krav_finns_det_en_fiende_pjäs_på_vektor2_position_relativt_till_pjäs(schackbräde_matris,pjäs,vektor2_position):
    x=vektor2_position[0]+pjäs.x
    y=vektor2_position[1]+pjäs.y
    
    if är_vektor2_i_matris([x,y],schackbräde_matris)==True:
        fiende_pjäs=schackbräde_matris[x][y].pjäs
        if fiende_pjäs!=None:
            if fiende_pjäs.färg!=pjäs.färg:
                return True
        return False

def flytt_beetende_krav_finns_det_en_vän_pjäs_på_vektor2_position_relativt_till_pjäs(schackbräde_matris,pjäs,vektor2_position):
    x=vektor2_position[0]+pjäs.x
    y=vektor2_position[1]+pjäs.y
    
    if är_vektor2_i_matris([x,y],schackbräde_matris)==True:
        vän_pjäs=schackbräde_matris[x][y].pjäs
        if vän_pjäs!=None:
            if vän_pjäs.färg==pjäs.färg:
                return True
        return False