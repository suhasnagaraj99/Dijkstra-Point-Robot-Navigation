# Dijkstra-Point-Robot-Navigation

## Project Description
This repository contains the implementation of the Dijkstra Algorithm for point robot navigation, developed as part of ENPM661 Project 2.

![Video GIF](https://github.com/suhasnagaraj99/Dijkstra-Point-Robot-Navigation/blob/main/dijkstra_suhas_nagaraj.gif)

## Assumptions and Map Description
- The robot is assumed to be a point robot
- The robot has a clearance of 5 mm. 
- The workspace is an 8-connected space
  - The robot can move UP, DOWN, LEFT, RIGHT (Cost: 1.0)
  - It can also move diagonally between UP-LEFT, UP-RIGHT, DOWN-LEFT, and DOWN-RIGHT (Cost: 1.4)
- Actions Set = {(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)}
- The map is as given below:
![alt text](https://github.com/suhasnagaraj99/Dijkstra-Point-Robot-Navigation/blob/main/661p2_map.png?raw=true)
- The above map represents the space for clearance = 0 mm. For a clearance of 5 mm, the
obstacles (including the walls) should be bloated by 5 mm distance on each side.

## Required Libraries
Before running the code, ensure that the following Python libraries are installed:

- `pygame`
- `numpy`
- `matplotlib.patches`
- `heapq`
- `time`

You can install them using pip if they are not already installed:

```bash
pip install pygame numpy matplotlib
```

## Running the Code
Follow these steps to run the code:

### Run the Python Script:

1. Execute the dijkstra_suhas_nagaraj.py file by running the following command in your terminal:

```bash
python3 dijkstra_suhas_nagaraj.py
```
2. The script will prompt you to input the coordinates for the initial and goal nodes.
3. First, enter the x-coordinate, followed by the y-coordinate, for both the initial and goal nodes.
4. Ensure that the entered coordinates are valid within the environment.
5. After entering the coordinates, the script will display an animation showing the node exploration and the optimal path found by the Dijkstra algorithm.

### Demo Inputs

You can use the following demo inputs to test the code:

- **Initial Node:**
  - x-coordinate: 6
  - y-coordinate: 6
- **Goal Node:**
  - x-coordinate: 1194
  - y-coordinate: 162

Simply enter these values when prompted to see the Dijkstra algorithm in action.
