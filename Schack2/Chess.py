import pygame
import sys



from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_SIZE, SQUARE_SIZE, WHITE, GREEN, BLACK, COLOR_INACTIVE, COLOR_ACTIVE
from View.rita_schack_bräde import rita_schack_bräde
from Controller.välj_position_och_få_drag_lista_i_schackbräde_matris import få_drag_lista_från_vald_sträng_position_i_schackbräde_matris, få_drag_lista_från_vektor2_i_schackbräde_matris
from Controller.schack_funktionalitet import är_kung_i_schack, är_schackmatt
from Model.skapa_schack_bräde_funktioner import skapa_standard_schackbräde_matris
from Controller.matris_funktioner import sträng_position_till_vektor2
from Controller.vektor2_sträng_konverterings_funktioner import konvertera_vektor2_lista_till_sträng_position_lista
from Controller.vektor2_sträng_konverterings_funktioner import vektor2_till_sträng_position
from Model.kataloger import pjäs_bild_katalog
pygame.init()


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Board with Input")

# Fonts
FONT = pygame.font.Font(None, 32)

def rita_brädet():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def rita_pjäser(matris):
    for row in range(8):
        for col in range(8):
            schack_position = matris[row][col]
            if schack_position.pjäs != None:
                screen.blit(pjäs_bild_katalog[schack_position.pjäs.bild_nyckel], (row * SQUARE_SIZE, col * SQUARE_SIZE))

def rita_drag_alternativ(drag_lista):
    for drag in drag_lista:
        pygame.draw.circle(screen,BLACK, ((drag.flytta_till_vektor2[0]+0.5) * SQUARE_SIZE, (drag.flytta_till_vektor2[1]+0.5) * SQUARE_SIZE),10.0)


def rita_input_box(text, input_rect, active):
    # Set color based on active state
    color = COLOR_ACTIVE if active else COLOR_INACTIVE
    pygame.draw.rect(screen, color, input_rect, 2)
    
    # Render the text
    txt_surface = FONT.render(text, True, BLACK)
    
    # Adjust text position if it overflows the box
    if txt_surface.get_width() > input_rect.w - 10:  # 10 pixels padding
        # Create a cropped surface to simulate scrolling text
        cropped_text = text[-(input_rect.w // FONT.size(' ')[0]):]  # Adjust text to fit within box
        txt_surface = FONT.render(cropped_text, True, BLACK)
    
    # Blit the text at adjusted position within the box
    screen.blit(txt_surface, (input_rect.x + 5, input_rect.y + (input_rect.h - txt_surface.get_height()) // 2))
    
    # Draw the rect around the input box
    pygame.draw.rect(screen, color, input_rect, 2)



class SchackSpelTillstånd():
    def __init__(self):
        self.match_pågår = True
        self.game_state_index = 0
        self.nuvarande_spelare_färg=0
        self.totala_antal_drag=0
        self.drag_alternativ_lista=[]
        self.flytt_sträng_alternativ_lista=[]
        self.text_input=''
        self.alla_drag_gjorda_lista=[]

def processa_drag_alternativ_lista(spel_tillstånd):
    if spel_tillstånd.drag_alternativ_lista==None:
        spel_tillstånd.text_input = ''
        spel_tillstånd.drag_alternativ_lista=[]
    elif len(spel_tillstånd.drag_alternativ_lista)==0:
        print("Inga giltiga drag för denna pjäs.")
        spel_tillstånd.text_input = ''
    else:
        pjäs=spel_tillstånd.drag_alternativ_lista[0].pjäs

        print(f"Du har valt att flytta {vektor2_till_sträng_position([pjäs.x,pjäs.y])} {pjäs.namn}, detta är dina flyttalternativ:")
        
        spel_tillstånd.flytt_sträng_alternativ_lista=[]
        for x in spel_tillstånd.drag_alternativ_lista:
            spel_tillstånd.flytt_sträng_alternativ_lista.append(x.flytta_till_vektor2)
        
        spel_tillstånd.flytt_sträng_alternativ_lista=konvertera_vektor2_lista_till_sträng_position_lista(spel_tillstånd.flytt_sträng_alternativ_lista)
        print("Välj ditt drag:")
        print(spel_tillstånd.flytt_sträng_alternativ_lista)
        spel_tillstånd.game_state_index=1
        spel_tillstånd.text_input=''

def utför_drag(schackbräde_matris, spel_tillstånd, vald_sträng_position, vald_vektor2_position):
    if vald_sträng_position not in spel_tillstånd.flytt_sträng_alternativ_lista:
        gå_tillbaka_till_game_state_att_välja_drag(spel_tillstånd)
        return
    
    pjäs=spel_tillstånd.drag_alternativ_lista[0].pjäs

    print(f"Du flyttade {vektor2_till_sträng_position([pjäs.x,pjäs.y])} {pjäs.namn} till {vald_sträng_position}")
    for drag in spel_tillstånd.drag_alternativ_lista:
        if drag.flytta_till_vektor2[0]==vald_vektor2_position[0] and drag.flytta_till_vektor2[1]==vald_vektor2_position[1]:
            drag.utför_flytt()
            spel_tillstånd.alla_drag_gjorda_lista.append(drag)
            break
    spel_tillstånd.totala_antal_drag+=1

    # Kolla schackcmatt

    motståndare_färg = 1 - spel_tillstånd.nuvarande_spelare_färg
    if är_kung_i_schack(schackbräde_matris, motståndare_färg):
        if är_schackmatt(schackbräde_matris, motståndare_färg):
            print(f"{'Vit' if spel_tillstånd.nuvarande_spelare_färg == 0 else 'Svart'} vinner! Schackmatt!")

        else:
            print(f"{'Vit' if motståndare_färg == 0 else 'Svart'} kung är i schack!")
    

    spel_tillstånd.nuvarande_spelare_färg = motståndare_färg
    gå_tillbaka_till_game_state_att_välja_drag(spel_tillstånd)

def gå_tillbaka_till_game_state_att_välja_drag(spel_tillstånd):
    spel_tillstånd.game_state_index=0
    spel_tillstånd.drag_alternativ_lista=[]
    spel_tillstånd.flytt_sträng_alternativ_lista=[]
    print(f"{'Vit' if spel_tillstånd.nuvarande_spelare_färg == 0 else 'Svart'} spelar")
    spel_tillstånd.text_input = ''

# Summerar alla pjäsers värde för båda färgerna för att ge båda lagens poäng eller hur bra deras position är
def evaluera_position(schackbräde_matris,färg):
    poäng=0
    for x in range(8):
        for y in range(8):
            if schackbräde_matris[x][y].pjäs!=None:
                if schackbräde_matris[x][y].pjäs.färg==färg:
                    poäng+=schackbräde_matris[x][y].pjäs.värde
                else:
                    poäng-=schackbräde_matris[x][y].pjäs.värde
    return poäng

class drag_kandidat:
    def __init__(self, poäng, drag_lista):
        self.poäng=poäng
        self.drag_lista=drag_lista

#Glömde helt bort att simulera andra spelarens drag. Alltså två färg variabler en för vem som ska göra draget och en för huvudfärg som ska hitta bästa draget.    
def simulera_alla_möjliga_drag_för_en_färg_och_evaluera_på_max_djup(schackbräde_matris,färg,max_djup,spara_mängd_drag,drag_lista,drag_kandidat_lista,nuvarande_djup):
    for x in range(8):
        for y in range(8):
            if schackbräde_matris[x][y].pjäs!=None:
                if schackbräde_matris[x][y].pjäs.färg==färg:
                    pjäs_drag_lista=få_drag_lista_från_vektor2_i_schackbräde_matris(schackbräde_matris, färg, [x,y])
                    for drag in pjäs_drag_lista:
                        nyaste_drag_lista=drag_lista+[drag]
                        #print(nyaste_drag_lista)
                        drag.utför_flytt()
                        if max_djup>nuvarande_djup:
                            simulera_alla_möjliga_drag_för_en_färg_och_evaluera_på_max_djup(schackbräde_matris,färg,max_djup,spara_mängd_drag,drag_lista=nyaste_drag_lista,drag_kandidat_lista=drag_kandidat_lista,nuvarande_djup=nuvarande_djup+1)
                        else:
                            positions_värde=evaluera_position(schackbräde_matris,färg)
                            if positions_värde>drag_kandidat_lista[0].poäng:
                               # print("------------")
                                #print(positions_värde)
                                #print(vektor2_till_sträng_position(nyaste_drag_lista[0].flytta_till_vektor2))
                                #print("------------")
                                drag_kandidat_lista[0]=drag_kandidat(positions_värde,nyaste_drag_lista)
                        drag.ta_tillbaka_flytt()
    if nuvarande_djup==1:
        return drag_kandidat_lista

def spela_schack_match(schackbräde_matris,spel_tillstånd):

    clock = pygame.time.Clock()
    input_box = pygame.Rect(50, SCREEN_HEIGHT - 50, 500, 32)
    active = False
    rev_amount=0

    default_rev_spd=2
    rev_spd=default_rev_spd

    print(f"{'Vit' if spel_tillstånd.nuvarande_spelare_färg == 0 else 'Svart'} spelar")

    while spel_tillstånd.match_pågår:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spel_tillstånd.match_pågår = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                active = input_box.collidepoint(event.pos)
                
                mus_position = pygame.mouse.get_pos()
                mus_i_grid_position = (mus_position[0] // SQUARE_SIZE, mus_position[1] // SQUARE_SIZE) 
                if mus_i_grid_position[1]<8:
                    if spel_tillstånd.game_state_index==0: #Välj pjäs med mus
                        spel_tillstånd.drag_alternativ_lista = få_drag_lista_från_vektor2_i_schackbräde_matris(schackbräde_matris, spel_tillstånd.nuvarande_spelare_färg ,mus_i_grid_position)
                        processa_drag_alternativ_lista(spel_tillstånd)
                        continue
                    if spel_tillstånd.game_state_index==1: #Välj och utför drag med mus
                        utför_drag(schackbräde_matris, spel_tillstånd, vektor2_till_sträng_position(mus_i_grid_position), mus_i_grid_position)
                        continue

                    
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    if spel_tillstånd.text_input=="score":
                        score=evaluera_position(schackbräde_matris,spel_tillstånd.nuvarande_spelare_färg)
                        print(f"{'Vit' if spel_tillstånd.nuvarande_spelare_färg == 0 else 'Svart'} poäng: {score}")
                        spel_tillstånd.text_input = ''
                        continue
                    if spel_tillstånd.text_input[0:2]=="ai":
                        djup=int(spel_tillstånd.text_input[2:])
                        bästa_drag=simulera_alla_möjliga_drag_för_en_färg_och_evaluera_på_max_djup(schackbräde_matris,spel_tillstånd.nuvarande_spelare_färg,djup,1,[],[drag_kandidat(-100,None)],1)
                        
                        spel_tillstånd.drag_alternativ_lista = [bästa_drag[0].drag_lista[0]]
                        processa_drag_alternativ_lista(spel_tillstånd)
                        vald_vektor2_position=bästa_drag[0].drag_lista[0].flytta_till_vektor2
                        vald_sträng_position=vektor2_till_sträng_position(vald_vektor2_position)
                        print(f'Bästa draget:{bästa_drag[0].drag_lista[0].flytta_till_vektor2}')

                        utför_drag(schackbräde_matris, spel_tillstånd, vald_sträng_position, vald_vektor2_position)
                        continue

                    if spel_tillstånd.text_input[0:3]=="rev":
                        rev_number=spel_tillstånd.text_input[3:]
                        rev_amount=int(rev_number)
                        print(rev_amount)
                        rev_spd=default_rev_spd
                        spel_tillstånd.text_input = ''
                        continue

                    if spel_tillstånd.game_state_index==0: #Välj pjäs med text
                        print(spel_tillstånd.nuvarande_spelare_färg)
                        spel_tillstånd.drag_alternativ_lista = få_drag_lista_från_vald_sträng_position_i_schackbräde_matris(schackbräde_matris, spel_tillstånd.nuvarande_spelare_färg, spel_tillstånd.text_input)
                        processa_drag_alternativ_lista(spel_tillstånd)
                        continue

                    if spel_tillstånd.game_state_index==1: #Välj och utför drag med text
                        vald_sträng_position = spel_tillstånd.text_input
                        vald_vektor2_position = sträng_position_till_vektor2(vald_sträng_position)
                        utför_drag(schackbräde_matris, spel_tillstånd, vald_sträng_position, vald_vektor2_position)
                        continue

                elif event.key == pygame.K_BACKSPACE:
                    spel_tillstånd.text_input = spel_tillstånd.text_input[:-1]
                else:
                    spel_tillstånd.text_input += event.unicode

        if rev_amount>0:
            print("REVV")
            if len(spel_tillstånd.alla_drag_gjorda_lista)>0:
                spel_tillstånd.alla_drag_gjorda_lista[-1].ta_tillbaka_flytt()
                spel_tillstånd.totala_antal_drag-=1
                spel_tillstånd.nuvarande_spelare_färg = 1 - spel_tillstånd.nuvarande_spelare_färg
                spel_tillstånd.alla_drag_gjorda_lista.pop()

                rev_spd=rev_spd*1.4

                clock.tick(rev_spd)
            rev_amount-=1
            if rev_amount==0:
                rev_spd=default_rev_spd

        screen.fill(WHITE)
        rita_brädet()
        rita_pjäser(schackbräde_matris)
        rita_drag_alternativ(spel_tillstånd.drag_alternativ_lista)
        rita_input_box(spel_tillstånd.text_input, input_box, active)
        pygame.display.flip()
        clock.tick(30)
    
            
spel_tillstånd = SchackSpelTillstånd()
standard_schackbräde_matris=skapa_standard_schackbräde_matris(spel_tillstånd)
spela_schack_match(standard_schackbräde_matris,spel_tillstånd)
