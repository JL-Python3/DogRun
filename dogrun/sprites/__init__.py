#! usr/bin/env python
# dogrun/sprites/__init__.py

from dogrun import *


BORDER_COLOR = pygame.Color("white")


def load_images(directory, dimensions):
    """
    :param directory:
    :param dimensions:
    :return:
    """
    pass


class DogSprite:
    """
    """
    dogs = (
        "Pomeranian (Ash Blonde)", "Pomeranian (Black)",
        "Pomeranian (Blonde)", "Pomeranian (Chocolate)",
        "Pomeranian (Classic)", "Pomeranian (Cream)", "Pomeranian (Fawn)",
        "Pomeranian (Grey)", "Pomeranian (Red)", "Pug", "Shiba Inu",
        "Shiba Inu (Black)", "Shiba Inu (Classic)", "Shiba Inu (Grey)"
    )

    # Frame interval constant
    interval = 2

    # Sprite speed constant
    speed = int(SCALE * 0.2)

    # Image constants
    factor = 0.75
    image_dimensions = (
        int(4 * SCALE * factor), int(3 * SCALE * factor)
    )
    xbound, ybound = (
        (0, WINWIDTH - image_dimensions[0]),
        (0, WINHEIGHT - image_dimensions[1])
    )

    def __init__(self, name, start=(4 * SCALE, 4 * SCALE)):
        """
        :param name:
        :param start:
        """
        self.name = name

        # TODO: Get directory containing sprite images

        # TODO: Load all sprite images from directory

        self.posx, self.posy = start
        self.frame = 0

        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )

    def move(self):
        """
        :return:
        """
        keys = pygame.key.get_pressed()

        # TODO: Check key presses (AWSD, arrows) and move sprite

        # TODO: Set sprite coordinates if position exceeds window bounds

    def update_rect(self, surface):
        """
        :param surface:
        """
        # TODO: Draw sprite border onto surface

    def update(self, surface, sprites):
        """
        :param surface:
        :param sprites:
        """
        # TODO: Blit appropriate sprite image onto surface

        self.frame = self.frame + 1


# TODO: Define class for squirrel sprites

# TODO: Define class for bush sprites

# TODO: Define class for bone sprites

# TODO: Define class for puddle sprites

# TODO: Define class for duck sprites

# TODO: Define class for pigeon sprites

# TODO: Define class for goose sprites
