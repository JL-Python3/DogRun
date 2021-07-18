# DogRun

*For participants of the **Python with PyGame** workshop, see the [Installation](#Installation) section for setting up your project.*

## Requirements

This project requires **Python 3.6+**.

Package dependencies:

- `pygame`


## Installation

*For Students:*

1. Navigate to the [Releases][1]. Find the [v0.0.0][2] release.
2. Under **Assets**, click *[Source Code (.zip)][3]* to download the necessary files as a compressed file.
3. One the *.zip* file has been downloaded, decompress the file.
    - For Mac OS X users, this step typically will be performed automatically.
    - The extracted folder will be titled *DogRun-0.0.0*.
      Optionally, the folder can be renamed to simply *DogRun*.
      The remainder of the tutorial will use the name *DogRun* to refer to the extracted folder.
4. Open a Command Line Interface (CLI) in the *DogRun* folder.
    - Windows: Command Prompt
    - Mac OS X: Terminal
    - REPL: Shell
5. To install all the packages listed under [Requirements](#Requirements), in a CLI, run:
    ```cmd
   $ pip install -r requirements.txt
    ```

## Usage

In a CLI, run:

```cmd
$ python -m dogrun
```

---

# Game Instructions

The *DogRun* game is composed of two different screens:

- [Opening Screen](#Opening-Screen)
- [Game Screen](#Game-Screen)

## Opening Screen

![Opening Screen](https://user-images.githubusercontent.com/86578588/126079968-98fb541e-5dc8-4005-96f8-335e5189ad2b.png)

*Button Widgets:*

- [Start](#Start)
- [Highscores](#Highscores)
- [Select Dog](#Select-Dog)

*Entry Widgets:*

- [Username](#Username)

*Display Widgets:*

- [Dog Sprite](#Dog-Sprite)

Opening Screen popups:

- [Highscores](#Highscores-Popup)
- [Dog Sprite Selection](#Dog-Sprite-Selection-Popup)

### Start

![Start](https://user-images.githubusercontent.com/86578588/126080065-0adc23f7-d04d-4929-9aa4-61e089a5ac5c.png)

Start the game, entering the [Game Screen](#Game-Screen).

### Highscores

![Highscores](https://user-images.githubusercontent.com/86578588/126080093-93e194b1-73ca-4f9e-97cd-d8947f7fb82c.png)

Opens the [Highscores popup](#Highscores-Popup).

### Select Dog

![Select Dog](https://user-images.githubusercontent.com/86578588/126080125-d052aa31-4a11-4163-b6b6-a5c6ab5dd7b8.png)

Opens the [Dog Sprite Selection Popup](#Dog-Sprite-Selection-Popup).

### Username

![Username](https://user-images.githubusercontent.com/86578588/126080139-48257d31-d5d3-426f-8383-92f164794da7.png)

Allows the user to type a username to play under.
Highscores will be saved under the username entered.

### Dog Sprite

![Dog Sprite](https://user-images.githubusercontent.com/86578588/126080153-66810184-b1cf-425f-b42e-c2d88fe8fdc7.png)

Displays and animation of the currently selected dog sprite.

### Highscores Popup

![Highscores popup](https://user-images.githubusercontent.com/86578588/126082390-de2d32a3-c1ec-465b-8353-ecd1caf77e71.png)

Displays the top ten scores saved locally.

To exit the popup, click in the window outside of the popup.

### Dog Sprite Selection Popup

![Dog Sprite Selection popup](https://user-images.githubusercontent.com/86578588/126082377-cb9f071d-8bfb-4db8-982d-088909b5873f.png)

Displays a list of the supported dog sprite names.
The selected dog sprite is displayed on the right and the name of the selected dog sprite is highlighted.
To confirm a dog sprite selection, click the **Select Dog** button widget.

To exit the popup, canceling the selection, click in the window outside of the popup.
Additionally, confirming a selection (with the **Select Dog** button) will exit the popup.

## Game Screen

![Game Screen](https://user-images.githubusercontent.com/86578588/126082699-275d7dc9-1335-465f-8b69-998ee9db9c9f.png)

*Button Widgets*:

- [Play/Pause](#Play/Pause)
- [Exit](#Exit)

*Display Widgets*:

- [Score](#Score)

*Sprites*:

- [Dog](#Dog)
- [Obstacles](#Obstacles)
- [Modifiers](#Modifiers)

### Play/Pause

![Play/Pause](https://github.com/JL-Python3/DogRun/blob/master/play%20pause.png?raw=true)

If the game is running, the game will be paused; if the game is paused, the game will be run.
When paused, sprite animations will continue.
However, the sprites will not move and points cannot be accumulated.

### Exit

![Exit](https://github.com/JL-Python3/DogRun/blob/master/exit.png?raw=true)

Exits the game screen, returning to the [Opening Screen](#Opening-Screen).
The user's score is not saved to the highscores list.

### Score

![Score](https://user-images.githubusercontent.com/86578588/126084472-72240a83-93d4-42e0-b95f-c433643ba9bd.png)

Displays the user's current game score.
Points are constantly accumulated during the game.
Colliding with [Modifiers](#Modifiers) can either increase or decrease the user's score.

### Dog

![Dog](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/Pomeranian%20(Ash%20Blonde)/Walking%20(Right)/004.png?raw=true)

The dog is the sprite which the user controls.
The user can use the arrow keys or the AWSD keys to move the dog sprite up, down, left, or right.

### Obstacles

If the dog sprite collides with any obstacle, the game ends.
The score obtained by the user is saved locally under the username entered.
The application then returns to the [Opening Screen](#Opening-Screen).

**Dynamic Obstacles:**

![Squirrel](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/Squirrel/036.png?raw=true)
![Duck](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/ducks/Ash/Right/024.png?raw=true)
![Pigeon](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/pigeons/Blue/Flying%20(Right)/078.png?raw=true)
![Goose](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/geese/Brown/Right/030.png?raw=true)

- Squirrel
- Duck
- Pigeon
- Goose

**Static Obstacles:**

![Bush](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/bushes/000.png?raw=true)

- Bush

### Modifiers

If the dog sprite collides with any modifier, the user's score is altered.
The point change values are as listed below:

| Modifier | Point Value |
| :------: | :---------: |
| Bone     | +500        |
| Puddle   | -250        |

![Bone](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/bone.png?raw=true)

![Puddle](https://github.com/JL-Python3/DogRun/blob/master/dogrun/sprites/puddle.png?raw=true)

[1]: https://github.com/JL-Python3/DogRun/releases
[2]: https://github.com/JL-Python3/DogRun/releases/tag/v0.0.0
[3]: https://github.com/JL-Python3/DogRun/archive/refs/tags/v0.0.0.zip