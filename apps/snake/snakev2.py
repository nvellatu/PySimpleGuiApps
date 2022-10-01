# Learned about the Graph element and setting up cells inside of it
# Learned about accepting keyboard inputs
# Split the functions that need to be carried out in each frame/iteration and work on each one idividually
# In this case the functions were split into: (update all info; clear board; draw new info)check apple snake collis and update apple pos;
# update snake head based off of direction; change direction based off of input; check if game over; draw apple and snake


import PySimpleGUI as sg
from time import time
from random import randint

def getApplePos():
    apple_pos = (randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1))
    while apple_pos in snake_body:
        apple_pos = (randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1))
    return apple_pos


def cell_pos__to_pixel(cell_pos):
    tl = (cell_pos[0] * CELL_SIZE, cell_pos[1] * CELL_SIZE + CELL_SIZE)
    br = (tl[0] + CELL_SIZE, tl[1] - CELL_SIZE)
    return(tl,br)

# Game Constants:
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

# snake
snake_body = [(4,4), (3,4), (2,4)]
DIRECTIONS = {'left':(-1,0), 'right':(1,0), 'up':(0,1), 'down':(0,-1)}
direction = DIRECTIONS['up']

# apple
apple_pos = getApplePos()
apple_eaten = False

sg.theme('green')
field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color='black'
)

layout = [
    [field]
]

window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()
while True:

    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED: break

    if event in ['Left:37', 'a'] and direction != DIRECTIONS['right']: direction = DIRECTIONS['left']
    if event in ['Up:38', 'w'] and direction != DIRECTIONS['down']: direction = DIRECTIONS['up']
    if event in ['Right:39', 'd'] and direction != DIRECTIONS['left']: direction = DIRECTIONS['right']
    if event in ['Down:40', 's'] and direction != DIRECTIONS['up']: direction = DIRECTIONS['down']

    # tl= (apple_pos[0]*CELL_SIZE,apple_pos[1]*CELL_SIZE)
    # br= (tl[0] + CELL_SIZE,tl[1]+CELL_SIZE)

    # time_since_start = time() - start_time
    # if time_since_start >= 0.5:
    #     start_time = time()

    #apple snake collision
    if snake_body[0] == apple_pos:
        apple_pos = getApplePos()
        apple_eaten = True

    #update snake
    new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
    snake_body.insert(0,new_head)
    if not apple_eaten:
        snake_body.pop()
    apple_eaten = False

    #check death
    if not 0 <= snake_body[0][0] < CELL_NUM or not 0 <= snake_body[0][1] < CELL_NUM or snake_body[0] in snake_body[1:]:
        break

    field.erase()
    #draw apple
    tl, br = cell_pos__to_pixel(apple_pos)
    field.draw_rectangle(tl, br, 'red')
    #draw snake
    for index, part in enumerate(snake_body):
        tl,br = cell_pos__to_pixel(part)
        color = 'yellow' if index==0 else 'green'
        field.draw_rectangle(tl,br,color)

window.close()
