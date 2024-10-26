def flytt_beetende_krav_kort_rockad(schackbräde_matris,pjäs):
    if pjäs.färg==0:
        if pjäs.x==4 and pjäs.y==7:
            if schackbräde_matris[5][7].pjäs==None and schackbräde_matris[6][7].pjäs==None:
                if schackbräde_matris[7][7].pjäs!=None:
                    if schackbräde_matris[7][7].pjäs.drag==0:
                        return True
    else:
        if pjäs.x==4 and pjäs.y==0:
            if schackbräde_matris[5][0].pjäs==None and schackbräde_matris[6][0].pjäs==None:
                if schackbräde_matris[7][0].pjäs!=None:
                    if schackbräde_matris[7][0].pjäs.drag==0:
                        return True
    return False

def flytt_beetende_krav_lång_rockad(schackbräde_matris,pjäs):
    if pjäs.färg==0:
        if pjäs.x==4 and pjäs.y==7:
            if schackbräde_matris[3][7].pjäs==None and schackbräde_matris[2][7].pjäs==None and schackbräde_matris[1][7].pjäs==None:
                if schackbräde_matris[0][7].pjäs!=None:
                    if schackbräde_matris[0][7].pjäs.drag==0:
                        return True
    else:
        if pjäs.x==4 and pjäs.y==0:
            if schackbräde_matris[3][0].pjäs==None and schackbräde_matris[2][0].pjäs==None and schackbräde_matris[1][0].pjäs==None:
                if schackbräde_matris[0][0].pjäs!=None:
                    if schackbräde_matris[0][0].pjäs.drag==0:
                        return True
    return False


def resultat_funktion_kort_rockad(drag,ta_tillbaka=False):
    if ta_tillbaka==False:
        if drag.pjäs.färg==0:

            torn = drag.schackbräde_matris[7][7].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[7][7].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[5][7].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 5  # Uppdatera tornets koordinater
            torn.y = 7
            torn.drag += 1
        else:
            torn = drag.schackbräde_matris[7][0].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[7][0].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[5][0].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 5  # Uppdatera tornets koordinater
            torn.y = 0
            torn.drag += 1
    else:
        if drag.pjäs.färg==0:
            torn = drag.schackbräde_matris[5][7].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[5][7].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[7][7].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 7  # Uppdatera tornets koordinater
            torn.y = 7
            torn.drag -= 1
        else:
            torn = drag.schackbräde_matris[5][0].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[5][0].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[7][0].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 7  # Uppdatera tornets koordinater
            torn.y = 0
            torn.drag -= 1


def resultat_funktion_lång_rockad(drag,ta_tillbaka=False):
    if ta_tillbaka==False:
        if drag.pjäs.färg==0:
            torn = drag.schackbräde_matris[0][7].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[0][7].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[3][7].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 3  # Uppdatera tornets koordinater
            torn.y = 7
            torn.drag += 1
        else:
            torn = drag.schackbräde_matris[0][0].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[0][0].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[3][0].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 3  # Uppdatera tornets koordinater
            torn.y = 0
            torn.drag += 1
    else:
        if drag.pjäs.färg==0:
            torn = drag.schackbräde_matris[3][7].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[3][7].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[0][7].pjäs = torn  # Flytta tornet till nya positionen
            torn.x = 0  # Uppdatera tornets koordinater
            torn.y = 7
            torn.drag -= 1
        else:
            torn = drag.schackbräde_matris[3][0].pjäs  # Hämta referensen till tornet
            drag.schackbräde_matris[3][0].pjäs = None  # Sätt gamla positionen till None
            drag.schackbräde_matris[0][0].pjäs = torn  # Flytta tornet till
