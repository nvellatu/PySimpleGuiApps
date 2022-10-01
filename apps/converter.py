#learned basics; how to make a gui, what it returns, how to keep one going, read events and vals, etc.

import PySimpleGUI as sg

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

layout = [[sg.Input(key='-INPUT-'), sg.Spin(['km to miles', 'kg to pounds', 'sec to min'], key='-UNIT-'), sg.Button('Convert', key='-CONVERT-')],
          [sg.Text('', key='-OUTPUT-')]]

window = sg.Window('Converter', layout)    #make the window with (title, layout);

while True:
    # print(window.read())
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        if not isfloat(values['-INPUT-']):
            window['-OUTPUT-'].update('Input must be a number.')
        elif values['-UNIT-'] == 'km to miles':
            window['-OUTPUT-'].update(str(round(float(values['-INPUT-']) * .6214, 3)) + " miles")
        elif values['-UNIT-'] == 'kg to pounds':
            window['-OUTPUT-'].update(str(float(values['-INPUT-']) * 2.20462) + " pounds")
        elif values['-UNIT-'] == 'sec to min':
            window['-OUTPUT-'].update(str(float(values['-INPUT-']) /60) + " minutes")


window.close()


