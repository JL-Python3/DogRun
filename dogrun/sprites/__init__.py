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
        # Draw sprite border onto surface
        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )
        pygame.draw.rect(surface, BORDER_COLOR, self.box, 1)

    def update(self, surface, sprites):
        """
        :param surface:
        :param sprites:
        """
        # TODO: Blit appropriate sprite image onto surface

        self.frame = self.frame + 1


class SquirrelSprite:
    """
    """
    # Frame interval constant
    interval = 2

    # Sprite speed constant
    speed = int(SPEED * 4)

    # Image constants
    factor = 1.5
    image_dimensions = (
        int(SCALE * factor), int(SCALE * factor)
    )

    def __init__(self, start):
        """
        :param start:
        """
        # TODO: Get directories containing sprite images

        # TODO: Load all sprite images

        self.posx, self.posy = start
        self.frame = 0

        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )

    def move(self):
        """
        """
        self.posx = self.posx - self.speed

    def update_rect(self, surface):
        """
        :param surface:
        """
        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )
        pygame.draw.rect(surface, BORDER_COLOR, self.box, 1)

    def update(self, surface, sprites):
        """
        :param surface:
        :param sprites:
        """
        # TODO: Blit appropriate sprite image onto surface

        self.frame = self.frame + 1


class BushSprite:
    """
    """

    # Sprite speed constant
    speed = SPEED

    # Image constants
    factor = 0.25
    image_dimensions = (
        int(16 * SCALE * factor), int(9 * SCALE * factor)
    )
    # TODO: Load all sprite images

    def __init__(self, start):
        """
        :param start:
        """
        # TODO: Select random sprite image

        self.posx, self.posy = start

        self.box = pygame.Rect((self.posx, self.posy), self.image_dimensions)

    def move(self):
        """
        """
        self.posx = self.posx - self.speed

    def update_rect(self, surface):
        """
        :param surface:
        """
        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )
        pygame.draw.rect(surface, BORDER_COLOR, self.box, 1)

    def update(self, surface):
        """
        :param surface:
        """
        # TODO: Blit sprite image onto surface


class BoneSprite:
    """
    """
    # Sprite speed constant
    speed = SPEED

    # Image constants
    interval = 3
    factor = 1
    image_dimensions = (int(SCALE * factor), int(SCALE * factor))
    # TODO: Load sprite image

    def __init__(self, start):
        """
        :param start:
        """
        # TODO: Generate rotations of sprite image

        self.posx, self.posy = start
        self.frame = 0

        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )

    def move(self):
        """
        """
        self.posx -= self.speed

    def update_rect(self, surface):
        """
        :param surface:
        """
        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )
        pygame.draw.rect(surface, BORDER_COLOR, self.box, 1)

    def update(self, surface):
        """
        :param surface:
        """
        # TODO: Blit appropriate sprite image onto surface

        self.frame = self.frame + 1


class PuddleSprite:
    """
    """
    # Sprite speed constants
    speed = SPEED

    # Image constants
    factor = 0.25
    image_dimensions = (
        int(16 * SCALE * factor), int(9 * SCALE * factor)
    )
    # TODO: Load sprite image

    def __init__(self, start):
        """
        :param start:
        """
        self.posx, self.posy = start

        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )

    def move(self):
        """
        """
        self.posx = self.posx - self.speed

    def update_rect(self, surface):
        """
        :param surface:
        """
        self.box = pygame.Rect(
            (self.posx, self.posy), self.image_dimensions
        )
        pygame.draw.rect(surface, BORDER_COLOR, self.box, 1)

    def update(self, surface):
        """
        :param surface:
        """
        # TODO: Blit sprite image onto surface


# TODO: Define class for duck sprites

# TODO: Define class for pigeon sprites

# TODO: Define class for goose sprites
