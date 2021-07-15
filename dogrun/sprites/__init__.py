#! usr/bin/env python
# dogrun/sprites/__init__.py

import os
import random

from dogrun import *


BORDER_COLOR = pygame.Color("white")


def load_images(directory, dimensions):
    """
    :param directory:
    :param dimensions:
    :return:
    """
    image_objects = []

    for file in os.listdir(directory):
        image = pygame.transform.scale(
            pygame.image.load(os.path.join(directory, file)),
            dimensions
        )
        image_objects.append(image)

    return tuple(image_objects)


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

        self.directory = os.path.join("dogrun", "sprites", self.name)

        directories = []
        for d in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory, d)):
                directories.append(os.path.join(self.directory, d))
        directories = sorted(directories)

        images = []
        for d in directories:
            images.append(load_images(d, self.image_dimensions))
        images = tuple(images)

        (self.resting, self.running, self.sitting_front, self.sitting_right,
         self.walking_back, self.walking_front, self.walking_left,
         self.walking_right) = images

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
        self.directory = os.path.join("dogrun", "sprites", "squirrel")

        directories = []
        for d in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory, d)):
                directories.append(os.path.join(self.directory, d))
        directories = sorted(directories)

        images = []
        for d in directories:
            images.append(load_images(d, self.image_dimensions))
        images = tuple(images)

        (self.inspecting_left, self.inspecting_right, self.looking_back,
         self.looking_front, self.looking_left, self.looking_right,
         self.resting, self.running_back, self.running_front,
         self.running_left, self.running_right, self.sitting_back,
         self.sitting_front, self.sitting_left, self.sitting_right) = images

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
    images = load_images(
        os.path.join("dogrun", "sprites", "bushes"),
        image_dimensions
    )

    def __init__(self, start):
        """
        :param start:
        """
        self.image = random.choice(self.images)

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
        surface.blit(self.image, (self.posx, self.posy))


class BoneSprite:
    """
    """
    # Sprite speed constant
    speed = SPEED

    # Image constants
    interval = 3
    factor = 1
    image_dimensions = (int(SCALE * factor), int(SCALE * factor))
    image = pygame.transform.scale(
        pygame.image.load(
            os.path.join("dogrun", "sprites", "bone.png")
        ), image_dimensions
    )

    def __init__(self, start):
        """
        :param start:
        """
        self.images = []
        for angle in range(0, 360, 45):
            self.images.append(
                pygame.transform.rotate(
                    self.image, angle
                )
            )
        self.images = tuple(self.images)

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
    image = pygame.transform.scale(
        pygame.image.load(
            os.path.join("dogrun", "sprites", "puddle.png")
        ), image_dimensions
    )

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
        surface.blit(self.image, (self.posx, self.posy))


# TODO: Define class for duck sprites

# TODO: Define class for pigeon sprites

# TODO: Define class for goose sprites
