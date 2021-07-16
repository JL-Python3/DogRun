#! usr/bin/env python
# dogrun/opening/dog_sprite_selection.py

import os

from dogrun import *


class DogSpriteSelection:
    """
    """
    # Popup constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 10

    def __init__(self, dog_sprites):
        """
        :param dog_sprites:
        """
        self.dog_sprites = dog_sprites

        self.box = pygame.Rect(
            4 * SCALE, 2 * SCALE, 24 * SCALE, 16 * SCALE
        )

        self.dogsprite_options = DogSpriteOptions(self.dog_sprites)
        self.dogsprite_display = DogSpriteDisplay(self.dog_sprites[0])
        self.select_button = SelectionButton()

        self.active = False

    def get_current_selection(self):
        """
        :return:
        """
        current = self.dogsprite_display.dog_sprite

        for index, sprite in enumerate(self.dogsprite_options.dog_sprites):
            if current == sprite:
                rect = self.dogsprite_options.rects[index]
                return rect

    def update(self, surface):
        """
        :param surface:
        """
        # Draw popup and popup border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Get box of current dog sprite and draw border onto surface
        highlight_rect = self.get_current_selection()
        pygame.draw.rect(surface, pygame.Color("dodgerblue1"), highlight_rect)

        # Update popup widgets
        self.dogsprite_display.update(surface)
        self.select_button.update(surface)
        self.dogsprite_options.update(surface)


class DogSpriteOptions:
    """
    """
    # Box constants
    border_color = pygame.Color("dimgray")
    border_width = 2

    # Text constants
    font = pygame.font.SysFont("segoeuisemibold", int(SCALE * 0.5))
    text_color = pygame.Color("black")

    def __init__(self, dog_sprites):
        """
        :param dog_sprites:
        """
        self.dog_sprites = dog_sprites

        self.rects = []
        self.text_surfs = []
        for i, sprite in enumerate(self.dog_sprites):
            rect = pygame.Rect(
                5 * SCALE, (i + 3) * SCALE, 9 * SCALE, SCALE
            )
            self.rects.append(rect)
            text_surf = self.font.render(sprite.name, True, self.text_color)
            self.text_surfs.append(text_surf)

    def update(self, surface):
        """
        :param surface:
        """
        for rect, text_surf in zip(self.rects, self.text_surfs):
            pygame.draw.rect(
                surface, self.border_color, rect, self.border_width
            )

            text_rect = text_surf.get_rect(center=rect.center)
            text_rect.x = rect.x + 10
            surface.blit(text_surf, text_rect)


class DogSpriteDisplay:
    """
    """
    # Box constants
    border_color = pygame.Color("dimgray")
    border_width = 4

    # Image constants
    factor = 3
    image_dimensions = (12 * SCALE, 12 * SCALE)
    image = pygame.transform.scale(
        pygame.image.load(os.path.join("dogrun", "sprites", "grass.png")),
        image_dimensions
    )

    def __init__(self, dog_sprite):
        self.dog_sprite = dog_sprite

        self.box = pygame.Rect(
            15 * SCALE, 3 * SCALE, 12 * SCALE, 12 * SCALE
        )

    def update(self, surface):
        """
        :param surface:
        """
        # Draw box onto surface
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Blit grass sprite image onto surface
        surface.blit(self.image, self.box.topleft)

        # Blit dog sprite image onto surface
        image = pygame.transform.scale(
            self.dog_sprite.sitting_right[0],
            (4 * SCALE * self.factor, 3 * SCALE * self.factor)
        )
        surface.blit(image, (15 * SCALE, int(4.5 * SCALE)))


class SelectionButton:
    """
    """
    # Box constants
    border_color = pygame.Color("dimgray")
    border_width = 4

    # Text constants
    font = pygame.font.SysFont("segoeuiblack", SCALE)
    text_color = pygame.Color("black")
    text = "Select Dog"

    def __init__(self):
        """
        """
        self.box = pygame.Rect(
            15 * SCALE, 15 * SCALE, 12 * SCALE, 2 * SCALE
        )

        self.text_surf = self.font.render(self.text, True, self.text_color)

    def update(self, surface):
        """
        :param surface:
        """
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        text_rect = self.text_surf.get_rect(center=self.box.center)
        surface.blit(self.text_surf, text_rect)
