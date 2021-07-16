#! usr/bin/env python
# dogrun/opening/__init__.py

from dogrun import sprites


def load_dog_sprites():
    """
    :return:
    """
    dog_sprites = []
    for name in sprites.DogSprite.dogs:
        dog_sprites.append(sprites.DogSprite(name))
    return tuple(dog_sprites)

# TODO: Define class for the opening screen

# TODO: Define class for a display widget for the selected dog sprite

# TODO: Define class for an entry widget for the username

# TODO: Define class for a button widget to start the game

# TODO: Define class for a button widget to select the dog sprite

# TODO: Define class for a button widget to view the highscore list
