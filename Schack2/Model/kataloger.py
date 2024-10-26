import sys
import pygame
from settings import SQUARE_SIZE
färg_katalog= {
  0: "□",
  1: "■",
}
sträng_till_kolumn_katalog={
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7,
    "i" : 8,
}
kolumn_till_sträng_katalog={
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
}

pjäs_bild_katalog = {
    'bR': pygame.image.load(sys.path[0]+'/Image/black_rook.png'),
    'bN': pygame.image.load(sys.path[0]+'/Image/black_knight.png'),
    'bB': pygame.image.load(sys.path[0]+'/Image/black_bishop.png'),
    'bQ': pygame.image.load(sys.path[0]+'/Image/black_queen.png'),
    'bK': pygame.image.load(sys.path[0]+'/Image/black_king.png'),
    'bP': pygame.image.load(sys.path[0]+'/Image/black_pawn.png'),
    'wR': pygame.image.load(sys.path[0]+'/Image/white_rook.png'),
    'wN': pygame.image.load(sys.path[0]+'/Image/white_knight.png'),
    'wB': pygame.image.load(sys.path[0]+'/Image/white_bishop.png'),
    'wQ': pygame.image.load(sys.path[0]+'/Image/white_queen.png'),
    'wK': pygame.image.load(sys.path[0]+'/Image/white_king.png'),
    'wP': pygame.image.load(sys.path[0]+'/Image/white_pawn.png'),
}

for key in pjäs_bild_katalog:
    pjäs_bild_katalog[key] = pygame.transform.scale(pjäs_bild_katalog[key], (SQUARE_SIZE, SQUARE_SIZE))