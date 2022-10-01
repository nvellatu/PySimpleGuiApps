# try and make a version that uses time out to create new frames rather than time - so that it updates when direction changes as well

import PySimpleGUI as sg
from time import time
from random import randint

def cell_pos__to_pixel(cell_pos):
    tl = (cell_pos[0] * CELL_SIZE, cell_pos[1] * CELL_SIZE + CELL_SIZE)
    br = (tl[0] + CELL_SIZE, tl[1] - CELL_SIZE)
    return(tl,br)

# Game Constants:
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

# apple
apple_pos = (0,0)
apple_eaten = False

# snake
snake_body = [(4,4), (3,4), (2,4)]
DIRECTIONS = {'left':(-1,0), 'right':(1,0), 'up':(0,1), 'down':(0,-1)}
direction = DIRECTIONS['up']

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

    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED: break

    if event == 'Left:37' and direction != DIRECTIONS['right']: direction = DIRECTIONS['left']
    if event == 'Up:38' and direction != DIRECTIONS['down']: direction = DIRECTIONS['up']
    if event == 'Right:39' and direction != DIRECTIONS['left']: direction = DIRECTIONS['right']
    if event == 'Down:40' and direction != DIRECTIONS['up']: direction = DIRECTIONS['down']

    # tl= (apple_pos[0]*CELL_SIZE,apple_pos[1]*CELL_SIZE)
    # br= (tl[0] + CELL_SIZE,tl[1]+CELL_SIZE)

    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()

        #apple snake collision
        if snake_body[0] == apple_pos:
            apple_pos = (randint(0, CELL_NUM-1), randint(0, CELL_NUM-1))
            while apple_pos in snake_body:
                apple_pos = (randint(0, CELL_NUM-1), randint(0, CELL_NUM-1))
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
