# SpaceShooter, A Pyglet Game

This is a simple game developed using the Pyglet library in Python. The game features a player-controlled spaceship that can move and shoot bullets. The game also includes enemies (asteroids) that break into smaller pieces upon collision.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Gameplay](#gameplay)
- [Contributing](#contributing)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Bilal-Ahmad102/SpaceShooter
   
   ```

2. **Install the required libraries:**
   Make sure you have Python installed. It's recommended to use a virtual environment.
   ```sh
   pip install pyglet
   ```

## Usage
To run the game, navigate to version_1 folder

```sh
cd version_1
```

execute the game script:
```sh
python game.py
```

## Code Structure

- **game.py**: This is the main entry point of the game. It initializes the game window, sets up the game objects, and handles the game loop.

- **player.py**: Contains the `Player` class, which defines the player's spaceship, its movement, and shooting mechanics.

- **physicalObject.py**: Defines the `PhysicalObject` class, a base class for all moving objects in the game, including the player, bullets, and asteroids.

- **asteroid.py**: Contains the `Asteriod` class, which defines the behavior of the asteroids, including their movement and how they break into smaller pieces.

- **bullets.py**: Defines the `Bullets` class, which handles the behavior of bullets fired by the player.

- **reset.py**: Contains the `Reset` class, which is initialized when game is restarted to get back to initial state game objects
 
- **functions.py**: Contains various utility functions for handling collisions, centering images, and generating enemies and player lives.

## Gameplay
   For Gameplay, check out [Youtube Video](https://www.youtube.com/watch?v=7it_vIdLGqk).

- **Movement**: Use the arrow keys to move the player's spaceship. 
  - `LEFT` and `RIGHT` keys to rotate the spaceship.
  - `UP` key to move forward in the direction the spaceship is facing.
  - `R`  key to restart the game 
- **Shooting**: Press the `SPACE` key to shoot bullets.

- **Enemies**: The game includes asteroids that break into smaller pieces when hit by bullets.
- **Background** : upon restart a different Background will be there.
## Contributing

Contributions are welcome! If you have suggestions or bug fixes, feel free to create a pull request or open an issue.

This `README.md` file provides a clear overview of the project, how to set it up, and how to use it. You can customize it further based on your specific requirements and add more details as needed.
