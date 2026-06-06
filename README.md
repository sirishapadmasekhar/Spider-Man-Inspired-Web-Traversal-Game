<img width="972" height="676" alt="Screenshot 2026-06-06 at 08 27 50" src="https://github.com/user-attachments/assets/7aa22343-bd5d-4250-a6db-98f6f84cb9ad" />
# Spider-Man Inspired Web Traversal Game

A 2D game developed using Python and Pygame that implements target-based movement, gravity simulation, collision detection, and sprite rendering in a city environment.

## Overview

This project simulates character movement through a cityscape using mouse-selected target points. The player can click on buildings to create a web connection, causing the character to move toward the selected location while being affected by gravity and velocity updates.

The environment includes buildings, animated vehicles, and a dynamically rendered night background.

## Features

* Mouse-based target selection
* Web line rendering between player and target
* Velocity-based character movement
* Gravity simulation
* Motion damping
* Building collision detection
* Character rotation based on movement direction
* Animated vehicle movement
* Procedurally generated building lights
* Night-time city environment

## Technologies

* Python
* Pygame

## Controls

<img width="972" height="676" alt="Screenshot 2026-06-06 at 08 27 50" src="https://github.com/user-attachments/assets/ca6f0145-f955-498f-b758-f01721827f5f" />


* Left Click on a building: Set a web target point

## Implementation Details

The project uses:

* Pygame event handling for user input
* Velocity and acceleration updates for movement
* Mathematical calculations for rotation and distance measurement
* Collision checks for rooftop landing
* Continuous rendering through a game loop

## Installation

```bash
pip install pygame
python main.py
```

## Repository Structure

```text
.
├── main.py
├── spiderman.png
└── README.md
```

## Learning Outcomes

* Event-driven programming
* Game loop implementation
* Collision detection
* Sprite transformation and rendering
* Physics-inspired movement systems
* Interactive application development using Pygame

```
```

