#! usr/bin/env python
# dogrun/__main__.py

from dogrun import *
from dogrun import game
from dogrun import opening


SURFACE = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
FPSCLOCK = pygame.time.Clock()

pygame.display.set_caption("Dog Run")

# Default user entries
DEFAULT_TEXT = ""
DEFAULT_DOG_SPRITE = None

# Screen sequence loop
while True:
    OPENING_SCREEN = opening.OpeningScreen(
        SURFACE, FPSCLOCK, DEFAULT_TEXT, DEFAULT_DOG_SPRITE
    )
    OPENING_SCREEN.run()

    USERNAME = OPENING_SCREEN.username_entry.text
    DOG_SPRITE = OPENING_SCREEN.dogsprite_display.dog_sprite

    DEFAULT_TEXT = USERNAME
    DEFAULT_DOG_SPRITE = DOG_SPRITE

    GAME_SCREEN = game.GameScreen(
        SURFACE, FPSCLOCK, DOG_SPRITE.name, USERNAME
    )
    GAME_SCREEN.run()
