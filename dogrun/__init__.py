#! usr/bin/env python
# dogrun/__init__.py

import json

import pygame

pygame.init()

# Aspect ratio constants: 16 x 10 aspect ratio (recommended)
WIDTH = 32      # Pixels
HEIGHT = 20     # Pixels
# Scale constant
SCALE = 30      # No unit

# Surface dimensions constants
WINWIDTH = WIDTH * SCALE        # Pixels
WINHEIGHT = HEIGHT * SCALE      # Pixels

# Framerate constant
FPS = 30        # Frames per Second

# Base movement speed constant
SPEED = int(SCALE * 0.1)        # Pixels per Frame

# Define default fill color
FILL = pygame.Color("dodgerblue4")


def read_highscores():
    """
    :return:
    """
    with open("highscores.txt", "r") as file:
        data = json.load(file)
    return data


def write_highscores(name, score):
    """
    :param name:
    :param score:
    """
    data = read_highscores()

    def sort_data(item):
        """
        :param item:
        :return:
        """
        return item[0]

    data.append((score, name))
    data = sorted(data, key=sort_data, reverse=True)

    with open("highscores.txt", "w") as file:
        json.dump(data, file)


def display_fps(surface, clock, digits=1):
    """
    :param surface:
    :param clock:
    :param digits:
    """
    text_color = pygame.Color("black")
    fps = round(clock.get_fps(), digits)
    percent_fps = round(fps / FPS * 100, digits)

    text = f"{fps} FPS ({percent_fps}%)"
    font = pygame.font.SysFont(
        "couriernew", int(SCALE * 0.5)
    )
    text_surf = font.render(
        text, True, text_color
    )
    surface.blit(text_surf, (0, 0))
