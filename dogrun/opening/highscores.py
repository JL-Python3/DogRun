#! usr/bin/env python
# dogrun/opening/highscores.py

from dogrun import *


class Highscores:
    """
    """
    # Popup constants
    fill_color = pygame.Color("white")
    border_color = pygame.Color("dimgray")
    border_width = 10

    def __init__(self):
        """
        """
        self.scores = read_highscores()

        self.box = pygame.Rect(
            4 * SCALE, 2 * SCALE, 24 * SCALE, 16 * SCALE
        )

        self.title_text = TitleText()
        self.highscores_display = HighscoresDisplay(self.scores)

        self.active = False

    def update(self, surface):
        """
        :param surface:
        """
        # Draw popup and popup border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Update popup widgets
        self.title_text.update(surface)
        self.highscores_display.update(surface)


class TitleText:
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
            10 * SCALE, 3 * SCALE, 12 * SCALE, 2 * SCALE
        )

        self.text_surf = self.font.render(self.text, True, self.text_color)

    def update(self, surface):
        """
        :param surface:
        """
        # Draw box and box border onto surface
        pygame.draw.rect(surface, self.fill_color, self.box)
        pygame.draw.rect(surface, self.border_color, self.box, self.border_width)

        # Blit text surface onto surface
        text_rect = self.text_surf.get_rect(center=self.box.center)
        surface.blit(self.text_surf, text_rect)


class HighscoresDisplay:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeui", SCALE)
    text_color = pygame.Color("black")
    text_columns = ("#", "Name" + 20 * " ", "Score")

    def __init__(self, scores):
        """
        :param scores:
        """
        self.scores = scores

        self.text_surfs = []
        for text in self.text_columns:
            text_surf = self.font.render(text, True, self.text_color)
            self.text_surfs.append(text_surf)
        self.text_surfs = tuple(self.text_surfs)

    def update(self, surface):
        """
        :param surface:
        """
        coordinates = (
            (6 * SCALE, 6 * SCALE), (7 * SCALE, 6 * SCALE),
            (22 * SCALE, 6 * SCALE)
        )

        for i, text_surf in enumerate(self.text_surfs):
            surface.blit(text_surf, coordinates[i])

        for i, (score, name) in enumerate(self.scores[:10], 1):
            text_columns = (str(i), name, str(score))
            for j, text in enumerate(text_columns):
                text_surf = self.font.render(
                    text, True, self.text_color
                )
                surface.blit(
                    text_surf, (coordinates[j][0], (6 + i) * SCALE)
                )
