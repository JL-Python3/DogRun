#! usr/bin/env python
# dogrun/__main__.py

from dogrun import *
from dogrun import game


SURFACE = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
FPSCLOCK = pygame.time.Clock()

pygame.display.set_caption("Dog Run")

# Default user entries
DEFAULT_TEXT = ""
DEFAULT_DOG_SPRITE = None

# Screen sequence loop
while True:
    # TODO: Create opening screen object
    # TODO: Run opening screen

    # TODO: Rewrite text default
    # TODO: Rewrite dog sprite default

    GAME_SCREEN = game.GameScreen(
        SURFACE, FPSCLOCK, "Shiba Inu", "Username"
    )
    GAME_SCREEN.run()
