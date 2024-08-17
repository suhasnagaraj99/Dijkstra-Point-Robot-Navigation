## GIthub repo link: https://github.com/suhasnagaraj99/ENPM661_Project2
## I have created a private repo to prevent plagarism 

import pygame
import numpy as np
from matplotlib.patches import Polygon
import heapq
import time

# Generating Map

# Creating a 2d array of size 1200X500 and initially filling it as inf
map=np.full((1200, 500), np.inf)

# Clearance from obstacle
offset=5

# Describing the obstacles using boundary limits
for x in range(1200):
    for y in range(500):
        x_bound = (x<=offset or x>=1200-offset)
        y_bound = (y<=offset or y>=500-offset)
        rec1_offset = (x>=100-offset and x<=175+offset) and (y>=100-offset and y<=500)
        rec1 = (x>=100 and x<=175) and (y>=100 and y<=500)
        rec2_offset = (x>=275-offset and x<=350+offset) and (y>=0 and y<=400+offset)
        rec2 = (x>=275 and x<=350) and (y>=0 and y<=400)
        poly_rec1_offset = (x>=900-offset and x<=1020+offset) and (y>=50-offset and y<=125+offset)
        poly_rec2_offset = (x>=900-offset and x<=1020+offset) and (y>=375-offset and y<=450+offset)
        poly_rec3_offset = (x>=1020-offset and x<=1100+offset) and (y>=50-offset and y<=450+offset)
        poly_rec1 = (x>=900 and x<=1020) and (y>=50 and y<=125)
        poly_rec2 = (x>=900 and x<=1020) and (y>=375 and y<=450)
        poly_rec3 = (x>=1020 and x<=1100) and (y>=50 and y<=450)
        hexa_offset=(((0.57736*x)+24.72232+offset)>=y) and (x>=520.096-offset) and (x<=779.9038+offset) and (((-0.57736*x)+475.27767-offset)<=y) and (((-0.57736*x)+775.27767+offset)>=y) and (((0.57736*x)-277.2776-offset)<=y)
        hexa=(((0.57736*x)+24.72232)>=y) and (x>=520) and (x<=779.9038) and (((-0.57736*x)+475.27767)<=y) and (((-0.57736*x)+775.27767)>=y) and (((0.57736*x)-277.2776)<=y)
        if(rec1_offset or rec2_offset or poly_rec1_offset or poly_rec2_offset or poly_rec3_offset or hexa_offset or x_bound or y_bound):
            map[x,y] = -1
        if(rec1 or rec2 or poly_rec1 or poly_rec2 or poly_rec3 or hexa):
            map[x,y] = -2

# Taking the initial node values from the user
while True:
    initial_x = int(input("Enter the initial x : "))
    initial_y = int(input("Enter the initial y : "))
    # If the given input is beyond the map dimensions, the input is asked for again 
    if initial_x>=1200 or initial_x<0 or initial_y<0 or initial_y>=500:
        print("Please enter valid initial node value")
        continue
    # If the given input is in the obstacle space or clearance space of the map, the input is asked for again 
    if map[initial_x,initial_y] < 0:
        print("Please enter valid initial node value")
        continue
    break

# Taking the initial node values from the user
while True:
    goal_x = int(input("Enter the goal x : "))
    goal_y = int(input("Enter the goal y : "))
    # If the given input is beyond the map dimensions, the input is asked for again 
    if goal_x>=1200 or goal_x<0 or goal_y<0 or goal_y>=500:
        print("Please enter valid goal node value")
        continue
    # If the given input is in the obstacle space or clearance space of the map, the input is asked for again 
    if map[goal_x,goal_y] < 0:
        print("Please enter valid goal node value")
        continue
    break

# storing the initial node as a list of tuples
# Here the 0 index represents the current node and the 1 index represents the path
## (0,0) is given as the initial/firsst path value, which is ignored later on. 
initial_node=[(initial_x,initial_y),[(0,0)]]

# storing the final node values as a tuple
goal_node=(goal_x,goal_y)


# Defining Action Set
## In each function, a new node is generated, the current node is updated to the path and the new cost to come is computed. 

# function to move up (0,1)
def move_up(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x,y+1),path]
  new_c2c=c2c+1
  return new_node,new_c2c

# function to move down (0,-1)
def move_down(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x,y-1),path]
  new_c2c=c2c+1
  return new_node,new_c2c

# function to move right (1,0)
def move_right(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x+1,y),path]
  new_c2c=c2c+1
  return new_node,new_c2c

# function to move left (-1,0)
def move_left(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x-1,y),path]
  new_c2c=c2c+1
  return new_node,new_c2c

# function to move diagonally up and left (-1,1)
def move_up_left(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x-1,y+1),path]
  new_c2c=c2c+1.4
  return new_node,new_c2c

# function to move diagonally up and right (1,1)
def move_up_right(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x+1,y+1),path]
  new_c2c=c2c+1.4
  return new_node,new_c2c

# function to move diagonally down and left (-1,-1)
def move_down_left(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x-1,y-1),path]
  new_c2c=c2c+1.4
  return new_node,new_c2c

# function to move diagonally down and right (1,-1)
def move_down_right(node,c2c):
  (x,y)=node[0]
  path = node[1].copy()
  path.append((x, y))
  new_node=[(x+1,y-1),path]
  new_c2c=c2c+1.4
  return new_node,new_c2c

# Creating an empty open list and converting it to heapq
open_list = []
heapq.heapify(open_list)
# Creating an empty closed list and closed set
# Closed set is used for comparison/searching as comparing/searching list is computationally expensive
closed_list = []
closed_set = set()
# adding the initial node to open list
heapq.heappush(open_list, (0, initial_node))
searching = True
possible_actions = [move_left, move_right, move_up, move_down, move_up_left, move_up_right, move_down_right, move_down_left]

while searching:
    # extracting the node with lowest c2c from the open list
    c2c, node = heapq.heappop(open_list)
    # adding the extracted node to the closed list and closed set
    closed_list.append(node[0])
    closed_set.add(node[0])
    # Conditional statement to check if goal node is reached
    if node[0] == goal_node:
        print("Solution reached")
        searching = False
        final_node = node
    else:
        # Performing actions on the extracted node
        for move_function in possible_actions:
            new_node, new_c2c = move_function(node, c2c)
            (new_x, new_y) = new_node[0]
            # If the new node is in obstacle space or clearence space, the node is skipped from further computation
            if map[new_x, new_y] < 0:
                continue
            # If the new node is in closed set, the node is skipped from further computation
            if new_node[0] in closed_set:
                continue
            found = False
            # Searching if the new node is in open list
            for i, (old_c2c, old_node) in enumerate(open_list):
                if old_node[0] == new_node[0]:
                    found = True
                    # if the new node is in open list, the node is updated id new c2c is lesser than the old c2c of the node
                    if new_c2c < old_c2c:
                        open_list[i] = (new_c2c, new_node)
                        heapq.heapreplace(open_list, (new_c2c, new_node))
                        break
            # if the new node is not in open list, the it is added to the open list along with c2c
            if not found:
                heapq.heappush(open_list, (new_c2c, new_node))

        # if the open list is empty, there are no more nodes to continue, hence the solution cannot be reached
        if not open_list:
            print("No solution found")



print(c2c)

## Initializing pygame for animation                    
pygame.init()
# index to skip frames for speeding up the animation
n=0
# creating a pygame screen
screen = pygame.display.set_mode((1200, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Creating a map on the screen based on the index value and color coding them accordingly
    ## The obstacles are represnted in red color
    ## The clearance is represented in yellow color
    ## Free space is represented in white color
    for y in range(map.shape[1]):
        for x in range(map.shape[0]):
            if map[x, y] == np.inf:
                pygame.draw.rect(screen, (255, 255, 255), (x , 500-y , 1, 1))
            elif map[x, y] == -2:
                pygame.draw.rect(screen, (255, 0, 0), (x , 500-y , 1, 1))
            elif map[x, y] == -1:
                pygame.draw.rect(screen, (255, 255, 0), (x, 500-y , 1, 1))
    
    # Initial and final node is plotted on the screen as a single pixel black dot
    pygame.draw.rect(screen, (0, 0, 0), (goal_node[0] , 500-goal_node[1] , 1, 1))
    pygame.draw.rect(screen, (0, 0, 0), (initial_node[0][0] , 500-initial_node[0][1] , 1, 1))
    
    # Loop to plot the node exploration on the screen
    ## Node exploration is plotted in blue
    for i in closed_list:
        (x,y) = i
        pygame.draw.rect(screen, (173, 216, 230), (x , 500-y , 1, 1))
        n=n+1
        if n%5==0:
            pygame.display.update()
            
    # Loop to plot the optimal path/solution on the screen
    ## The solution is plotted in black
    for i in final_node[1]:
        (x,y)=i
        if n==0:
            n=n+1
            continue
        # The path is plotted with size 3X3 for better visibility
        pygame.draw.rect(screen, (0, 0, 0), (x , 500-y , 1, 1))
    pygame.display.update()
    # Sleep for 10 seconds to freeze the solution screen
    time.sleep(10)
pygame.quit()
