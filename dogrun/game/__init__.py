#! usr/bin/env python
# dogrun/game/__init__.py

import random

from dogrun import *
from dogrun import sprites


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

        self.username = username

        self.score_display = ScoreDisplay()

        self.dog_sprite = sprites.DogSprite(dog_sprite)

        lane_width = WINHEIGHT // self.num_lanes
        self.lanes = []
        for i in range(self.num_lanes):
            self.lanes.append(
                Lane((i * lane_width, (i + 1) * lane_width))
            )
        self.lanes = tuple(self.lanes)

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
        text_surf = self.font.render(
            f"SCORE: {self.score}", True, self.text_color
        )

        # Blit text surface onto surface
        surface.blit(text_surf, (0, WINHEIGHT - text_surf.get_height()))

# TODO: Define class for a button widget to exit the game screen

# TODO: Define class for a button widget to play/pause the game


class Lane:
    """
    """
    # Obstacles
    dynamic_obstacles = ()
    static_obstacles = ()
    obstacle_opts = dynamic_obstacles + static_obstacles

    # Modifiers
    dynamic_modifiers = ()
    static_modifiers = ()
    modifier_opts = dynamic_modifiers + static_modifiers

    def __init__(
            self, yrange,
            obstacle_limit=1, obstacle_freq=128,
            modifier_limit=1, modifier_freq=1024
    ):
        """
        :param yrange:
        :param obstacle_limit:
        :param obstacle_freq:
        :param modifier_limit:
        :param modifier_freq:
        """
        self.yrange = yrange

        self.obstacle_limit = obstacle_limit
        self.obstacle_freq = obstacle_freq
        self.obstacles = []

        self.modifier_limit = modifier_limit
        self.modifier_freq = modifier_freq
        self.modifiers = []

    def add_obstacle(self):
        """
        """
        # Select random obstacle class
        obstacle = random.choice(self.obstacle_opts)

        # Generate random starting coordinates
        position = (
            WINWIDTH, random.randint(self.yrange[0], self.yrange[1])
        )

        # TODO: Append new object of selected class to obstacles

    def add_modifier(self):
        """
        """
        # Select random modifier class
        modifier = random.choice(self.modifier_opts)

        # Generate random starting coordinates
        position = (
            WINWIDTH, random.randint(self.yrange[0], self.yrange[1])
        )

        # TODO: Append new object of selected class to modifiers

    def move(self):
        """
        """
        objects = self.obstacles + self.modifiers

        for item in objects:
            # TODO: Move item sprite

            # TODO: Remove item if sprite position is outside the window bounds
            pass

    def update_rect(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        # TODO: Update items sprite borders

    def update(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        # TODO: Update sprite images (obstacles)

        # TODO: Update sprite images (modifiers)

        # Add obstacle
        if len(self.obstacles) < self.obstacle_limit:
            if random.randint(1, self.obstacle_freq) == 1:
                self.add_obstacle()

        # Add modifier
        if len(self.modifiers) < self.modifier_limit:
            if random.randint(1, self.modifier_freq) == 1:
                self.add_modifier()
