#! usr/bin/env python
# dogrun/__init__.py

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

# TODO: Define default fill color (PyGame 'Color' object)

# TODO: Define function to read highscore data

# TODO: Define function to write highscore data

# TODO: Define function to display framerate onto surface
