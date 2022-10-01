# learned about downloading and using fonts and images
# learned about putting in attributes for the window
# learned about setting a timeout for the read
# learned about more customization

import PySimpleGUI as sg
from time import time
from random import choice

faces = ['(◑‿◐)', '( ͡~ ͜ʖ ͡°)', '(͡• ͜໒ ͡• )', '◕‿↼', '(▀̿Ĺ̯▀̿ ̿)', '(ง ͠° ͟ل͜ ͡°)ง']
def create_window():
    sg.theme('black')
    layout = [
        [sg.P(), sg.Image("icons8-close-window-50.png", enable_events=True, pad=0, k='-CLOSE-')],
        [sg.VP()],
        [sg.Text(choice(faces), font='Young 50', k='-TIME-')],
        [sg.Button('Start', button_color=('#FFFFFF','#FF0000'), border_width=0, k='-STARTSTOP-'), sg.Button('Lap', k='-LAP-', visible=False, button_color=('#FFFFFF','#FF0000'), border_width=0)],
        [sg.Column([[]], k='-LAPS-')],
        [sg.VP()]
    ]

    return sg.Window('Stopwatch',
                       layout,
                       size=(300,300),
                       no_titlebar=True,
                       element_justification='center')

window = create_window()

start_time = 0
active = False
lap_num = 1
while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:                              #if stop is pressed: turn off active, remove lapB, and change stop to reset
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            if start_time>0:                    #if reset is pressed: reset start time and make a new window
                start_time= 0
                window= create_window()
                lap_num= 1
            else:                               #if start is pressed: save start time, active = true, change start to stop, add lapB
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)
# we are able to check for the different states of the program and operate accordingly by
    # checking for certain distinct conditions that pertain to the separate states
    if active == True:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.T(lap_num),sg.VSep(), sg.T(elapsed_time)]])
        lap_num+=1

window.close()