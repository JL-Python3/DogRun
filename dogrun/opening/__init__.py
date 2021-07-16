#! usr/bin/env python
# dogrun/opening/__init__.py

import string
import sys

from dogrun import *
from dogrun import sprites


def load_dog_sprites():
    """
    :return:
    """
    dog_sprites = []
    for name in sprites.DogSprite.dogs:
        dog_sprites.append(sprites.DogSprite(name))
    return tuple(dog_sprites)


class OpeningScreen:
    """
    """

    def __init__(
            self, surface, clock,
            default_username="", default_dogsprite=None
    ):
        self.surface = surface
        self.clock = clock

        self.logo = pygame.transform.scale(
            pygame.image.load("logo.png").convert_alpha(),
            (20 * SCALE, 10 * SCALE)
        )

        self.dog_sprites = load_dog_sprites()
        if default_dogsprite is None:
            dog_sprite = self.dog_sprites[0]
        else:
            dog_sprite = default_dogsprite

        self.start_button = StartButton()
        self.selectdog_button = SelectDogButton()
        self.highscores_button = HighscoresButton()
        self.username_entry = UsernameEntry(default_username)
        self.dogsprite_display = DogSpriteDisplay(dog_sprite)

        # TODO: Create popup objects

        self.running = True

    def update_screen(self):
        """
        """
        self.surface.fill(FILL)

        # Blit logo image onto surface
        self.surface.blit(self.logo, (6 * SCALE, 2 * SCALE))

        # Update widgets
        self.start_button.update(self.surface)
        self.selectdog_button.update(self.surface)
        self.highscores_button.update(self.surface)
        self.username_entry.update(self.surface)
        self.dogsprite_display.update(self.surface)

        # TODO: Update popups

    def run(self):
        """
        """
        while self.running:
            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_click(event.pos)

                if event.type == pygame.KEYUP:
                    if self.username_entry.active:
                        self.handle_typing(event.key, event.unicode)

            self.update_screen()
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_click(self, pos):
        """
        """
        # TODO: Check for clicks in dog sprite selection popup

        # TODO: Check for clicks in highscores popup

        # Check for clicks in widgets
        self.username_entry.active = False
        self.username_entry.active = False
        if self.username_entry.box.collidepoint(pos):
            self.username_entry.active = True
            if self.username_entry.text == self.username_entry.default_text:
                self.username_entry.text = ""
        elif self.selectdog_button.box.collidepoint(pos):
            # TODO: Activate dog sprite selection popup
            pass
        elif self.highscores_button.box.collidepoint(pos):
            # TODO: Activate highscores popup
            pass
        elif self.start_button.box.collidepoint(pos):
            if self.username_entry.text != "":
                self.running = False

    def handle_typing(self, key, unicode):
        """
        """
        keyname = pygame.key.name(key)

        if keyname in string.printable:
            self.username_entry.text += unicode
            self.username_entry.text = self.username_entry.text[:20]
        elif key == pygame.K_BACKSPACE:
            self.username_entry.text = self.username_entry.text[:-1]
        elif key == pygame.K_DELETE:
            self.username_entry.text = ""


class DogSpriteDisplay:
    """
    """
    # Box surface constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 4

    # Frame interval constant
    interval = 4

    # Scale factor constant
    factor = 2

    def __init__(self, dog_sprite):
        """
        """
        self.dog_sprite = dog_sprite

        self.box = pygame.Rect(
            16 * SCALE, 8 * SCALE, 10 * SCALE, 8 * SCALE
        )

        self.resting = []
        for sprite in dog_sprite.resting:
            image = pygame.transform.scale(
                sprite,
                (4 * SCALE * self.factor, 3 * SCALE * self.factor)
            )
            self.resting.append(image)
        self.resting = tuple(self.resting)

        self.frame = 0

    def update(self, surface):
        """
        """
        # Draw box and box border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Blit appropriate sprite image onto surface
        index = (self.frame // self.interval) % len(self.resting)
        surface.blit(self.resting[index], (17 * SCALE, 9 * SCALE))

        self.frame += 1


class UsernameEntry:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeuisemibold", SCALE)
    active_color = pygame.Color("dodgerblue1")
    inactive_color = pygame.Color("orange")
    default_text = "username:"

    # Box constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 4

    def __init__(self, default_username=""):
        """
        """
        if default_username == "":
            self.text = self.default_text
        else:
            self.text = default_username

        self.box = pygame.Rect(
            6 * SCALE, 17 * SCALE, 20 * SCALE, 2 * SCALE
        )

        self.active = False

    def update(self, surface):
        """
        """
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Create text surface object with appropriate color
        if self.active:
            text_color = self.active_color
        else:
            text_color = self.inactive_color
        text_surf = self.font.render(self.text, True, text_color)

        # Blit text surface onto surface
        text_rect = text_surf.get_rect(center=self.box.center)
        text_rect.x = self.box.x + 10
        surface.blit(text_surf, text_rect)


class StartButton:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeuiblack", SCALE)
    text_color = pygame.Color("black")
    text = "Start"

    # Box constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 4

    def __init__(self):
        """
        """
        self.box = pygame.Rect(
            6 * SCALE, 8 * SCALE, 8 * SCALE, 2 * SCALE
        )

        self.text_surf = self.font.render(self.text, True, self.text_color)

    def update(self, surface):
        """
        """
        # Draw box and box border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Blit text surface onto surface
        text_rect = self.text_surf.get_rect(center=self.box.center)
        surface.blit(self.text_surf, text_rect)


class SelectDogButton:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeuiblack", SCALE)
    text_color = pygame.Color("black")
    text = "Select Dog"

    # Box constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 4

    def __init__(self):
        """
        """
        self.box = pygame.Rect(
            6 * SCALE, 14 * SCALE, 8 * SCALE, 2 * SCALE
        )

        self.text_surf = self.font.render(self.text, True, self.text_color)

    def update(self, surface):
        """
        """
        # Draw box and box border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Blit text surface onto surface
        text_rect = self.text_surf.get_rect(center=self.box.center)
        surface.blit(self.text_surf, text_rect)


class HighscoresButton:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeuiblack", SCALE)
    text_color = pygame.Color("black")
    text = "Highscores"

    # Box constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 4

    def __init__(self):
        """
        """
        self.box = pygame.Rect(
            6 * SCALE, 11 * SCALE, 8 * SCALE, 2 * SCALE
        )

        self.text_surf = self.font.render(self.text, True, self.text_color)

    def update(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        text_rect = self.text_surf.get_rect(center=self.box.center)
        surface.blit(self.text_surf, text_rect)
