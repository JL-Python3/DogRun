#! usr/bin/env python
# dogrun/game/__init__.py

import os
import random

from dogrun import *
from dogrun import sprites


class GameScreen:
    """
    """
    speed = SPEED

    num_lanes = 4

    background = pygame.transform.scale(
        pygame.image.load(
            os.path.join("dogrun", "sprites", "grass.png")
        ), (4 * SCALE, 4 * SCALE)
    )

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
        self.exit_button = ExitButton()
        self.playpause_button = PlayPauseButton()

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

        # Update dog sprite border
        self.dog_sprite.update_rect(self.surface)

        # Update lane items sprite borders
        for lane in self.lanes:
            lane.update_rect(self.surface)

        self.update_background()

        # Update dog sprite image
        self.dog_sprite.update(self.surface, self.dog_sprite.running)

        # Update lane items sprite images
        for lane in self.lanes:
            lane.update(self.surface)

        # Update widgets
        self.score_display.update(self.surface)
        self.exit_button.update(self.surface)
        self.playpause_button.update(self.surface)

        display_fps(self.surface, self.clock)

    def update_background(self):
        """
        """
        # Repeatedly blit background image to surface
        for x in range(self.displacement, WINWIDTH - self.displacement, SCALE * 4):
            for y in range(0, WINHEIGHT, SCALE * 4):
                self.surface.blit(self.background, (x, y))
                pass

        if not self.paused:
            self.displacement = self.displacement - self.speed

    def run(self):
        """
        """
        while self.running:
            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_click(event.pos)

            # Check for collisions between dog sprite and lane items sprites
            for lane in self.lanes:
                collided = self.check_collision(lane)
                if collided:
                    self.running = False
                    write_highscores(
                        self.username, self.score_display.score
                    )
                    break

            if not self.paused:
                self.dog_sprite.move()

                for lane in self.lanes:
                    lane.move()

                self.score_display.score = self.score_display.score + 1

            self.update_screen()
            pygame.display.update()
            self.clock.tick(FPS)

    def handle_click(self, pos):
        """
        :param pos:
        """
        # Check for click on exit button
        if self.exit_button.box.collidepoint(pos):
            self.running = False

        # Check for click on play/pause button
        elif self.playpause_button.box.collidepoint(pos):
            self.paused = not self.paused

    def check_collision(self, lane):
        """
        :param lane:
        :return:
        """
        # Check fo collision with modifier
        for mod in lane.modifiers:
            obs_bounds = (
                mod.box.bottomleft, mod.box.bottomright,
                mod.box.topleft, mod.box.topright,
                mod.box.midleft, mod.box.midright,
                mod.box.midtop, mod.box.midbottom
            )
            for point in obs_bounds:
                if self.dog_sprite.box.collidepoint(point):
                    if isinstance(mod, sprites.BoneSprite):
                        self.score_display.score += 500
                    elif isinstance(mod, sprites.PuddleSprite):
                        self.score_display.score -= 250
                    lane.modifiers.remove(mod)
                    break

        # Check for collision with obstacle
        for obs in lane.obstacles:
            obs_bounds = (
                obs.box.bottomleft, obs.box.bottomright,
                obs.box.topleft, obs.box.topright,
                obs.box.midleft, obs.box.midright,
                obs.box.midtop, obs.box.midbottom
            )
            for point in obs_bounds:
                if self.dog_sprite.box.collidepoint(point):
                    return True

        return False


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


class ExitButton:
    """
    """
    # Box constants
    border_color = pygame.Color("black")

    # Image constants
    factor = 1.5
    image_dimensions = (
        int(SCALE * factor), int(SCALE * factor)
    )
    image = pygame.transform.scale(
        pygame.image.load("exit.png"), image_dimensions
    )

    def __init__(self):
        """
        """
        self.coordinates = (
            int((WIDTH - self.factor) * SCALE), 0
        )

        self.box = pygame.Rect(
            self.coordinates, self.image_dimensions
        )

    def update_rect(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        pygame.draw.rect(surface, self.border_color, self.box, 1)

    def update(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        surface.blit(self.image, self.coordinates)


class PlayPauseButton:
    """
    """
    # Box constants
    border_color = pygame.Color("black")

    # Image constants
    factor = ExitButton.factor
    image_dimensions = ExitButton.image_dimensions
    image = pygame.transform.scale(
        pygame.image.load("play pause.png"), image_dimensions
    )

    def __init__(self):
        """
        """
        self.coordinates = (
            int((WIDTH - 2 * self.factor) * SCALE), 0
        )

        self.box = pygame.Rect(
            self.coordinates, self.image_dimensions
        )

    def update_rect(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        pygame.draw.rect(
            surface, self.border_color, self.box, 1
        )

    def update(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        surface.blit(self.image, self.coordinates)


class Lane:
    """
    """
    # Obstacles
    dynamic_obstacles = (
        sprites.SquirrelSprite,
    )
    static_obstacles = (
        sprites.BushSprite,
    )
    obstacle_opts = dynamic_obstacles + static_obstacles

    # Modifiers
    dynamic_modifiers = (
        sprites.BoneSprite,
    )
    static_modifiers = (
        sprites.PuddleSprite,
    )
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

        self.obstacles.append(obstacle(position))

    def add_modifier(self):
        """
        """
        # Select random modifier class
        modifier = random.choice(self.modifier_opts)

        # Generate random starting coordinates
        position = (
            WINWIDTH, random.randint(self.yrange[0], self.yrange[1])
        )

        self.modifiers.append(modifier(position))

    def move(self):
        """
        """
        objects = self.obstacles + self.modifiers

        for item in objects:
            item.move()

            # Remove item if sprite position is outside the window bounds
            if item.box.right < 0 or item.box.left > WINWIDTH:
                if item in self.obstacles:
                    self.obstacles.remove(item)
                elif item in self.modifiers:
                    self.modifiers.remove(item)

    def update_rect(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        # Update sprite borders
        for item in self.obstacles + self.modifiers:
            item.update_rect(surface)

    def update(self, surface):
        """
        :param surface: A PyGame 'Surface' object
        """
        # Update sprite images (obstacles)
        for item in self.obstacles:
            if type(item) in self.dynamic_obstacles:
                try:
                    item.update(surface, item.running_left)
                except AttributeError:
                    item.update(surface, item.flying_left)
            elif type(item) in self.static_obstacles:
                item.update(surface)

        # Update sprite images (modifiers)
        for item in self.modifiers:
            item.update(surface)

        # Add obstacle
        if len(self.obstacles) < self.obstacle_limit:
            if random.randint(1, self.obstacle_freq) == 1:
                self.add_obstacle()

        # Add modifier
        if len(self.modifiers) < self.modifier_limit:
            if random.randint(1, self.modifier_freq) == 1:
                self.add_modifier()
