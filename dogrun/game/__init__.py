#! usr/bin/env python
# dogrun/game/__init__.py

from dogrun import *


class GameScreen:
    """
    """
    speed = SPEED

    num_lanes = 4

    # TODO: Load background image

    def __init__(self, surface, clock, dog_sprite, username):
        """
        :param surface:
        :param clock:
        :param dog_sprite:
        :param username:
        """
        self.surface = surface
        self.clock = clock

        self.dog_sprite = dog_sprite
        self.username = username

        self.score_display = ScoreDisplay()

        # TODO: Create dog sprite object

        # TODO: Create lane objects

        self.displacement = 0

        self.running = True
        self.paused = False

    def update_screen(self):
        """
        """
        self.surface.fill(pygame.Color("black"))

        # TODO: Update dog sprite border

        # TODO: Update lane items sprite borders

        self.update_background()

        # TODO: Update dog sprite image

        # TODO: Update lane items sprite images

        # Update widgets
        self.score_display.update(self.surface)

        display_fps(self.surface, self.clock)

    def update_background(self):
        """
        """
        # Repeatedly blit background image to surface
        for x in range(self.displacement, WINWIDTH - self.displacement, SCALE * 4):
            for y in range(0, WINHEIGHT, SCALE * 4):
                # TODO: Blit background image to surface
                pass

        if not self.paused:
            self.displacement = self.displacement - self.speed

    def run(self):
        """
        """
        while self.running:
            # TODO: Check events

            # TODO: Check for collisions between dog sprite and lane items sprites

            if not self.paused:
                # TODO: Move dog sprite

                # TODO: Move lanes

                self.score_display.score = self.score_display.score + 1

            self.update_screen()
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_click(self, pos):
        """
        :param pos:
        """
        # TODO: Check for click on exit button

        # TODO: Check for clock on play/pause button

    def check_collision(self, lane):
        """
        :param lane:
        :return:
        """
        # TODO: Check for collision with modifier

        # TODO: Check for collision with obstacle


class ScoreDisplay:
    """
    """
    # Text constants
    font = pygame.font.SysFont("segoeuiblack", SCALE)
    text_color = pygame.Color("black")

    def __init__(self):
        """
        """
        self.score = 0

    def update(self, surface):
        """
        :param surface:
        """
        # Create text surface
        text = "SCORE: " + str(self.score)
        text_surf = self.font.render(
            text, True, self.text_color
        )

        # TODO: Blit text surface onto surface

# TODO: Define class for a button widget to exit the game screen

# TODO: Define class for a button widget to play/pause the game

# TODO: Define class to handle the obstacle/modifier sprites in a lane
