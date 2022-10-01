#larned  about customizing elements through things like size, push, fonts, justification, etc;
#learned how to navigate docs
#learned how to group events based off of similar function

import PySimpleGUI as sg

current_output = []

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(6,3))
    button_size = (6,3)
    layout = [
        [sg.Frame('',layout=[[sg.T('Right Click Output to customize theme!', font='Franklin 8')]], element_justification='center', expand_x=True)],
        [sg.Text(''.join(current_output), key='-OUTPUT-', font='Franklin 26', expand_x=True, justification='right', right_click_menu=theme_menu)],
        # [sg.Push(), sg.Text(''.join(current_output), key='-OUTPUT-', font='Franklin 26', pad=(10,20),
        #                     right_click_menu=theme_menu)],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, s=button_size), sg.Button(8, s=button_size), sg.Button(9, s=button_size), sg.Button('/', s=button_size)],
        [sg.Button(4, s=button_size), sg.Button(5, s=button_size), sg.Button(6, s=button_size), sg.Button('*', s=button_size)],
        [sg.Button(1, s=button_size), sg.Button(2, s=button_size), sg.Button(3, s=button_size), sg.Button('-', s=button_size)],
        [sg.Button(0, expand_x=True), sg.Button('.', s=button_size), sg.Button('+', s=button_size)],]

    return sg.Window('Calculator', layout)

theme_menu = ['menu', ['DefaultNoMoreNagging', 'DarkGreen7', 'LightBrown7', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧RANDOM✧ﾟ･: *ヽ(◕ヮ◕ヽ)']]  #name, options layout list
window = create_window('d')

full_operation = []

while True:
    event, values = window.read()
    # window['-OUTPUT-'].update(''.join(current_output))
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_output.append(event)
        window['-OUTPUT-'].update(''.join(current_output))
    if event in ['+','-','/','*']:
        currentNum = ''.join(current_output)
        if isfloat(currentNum):     #if current num exists, it gets added to fullOP along with op
            full_operation.append(currentNum)
            current_output = []
            full_operation.append(event)
        elif len(full_operation):   #else if current num is empty, and full op is not empty, last op gets replaced; if last fullOP val is op
            full_operation.pop()
            full_operation.append(event)
        #                            if fullOP is empty then don't add an operation

    if event == 'Enter':
        if len(full_operation):
            full_operation.append(''.join(current_output))  #append current num-> get result and set as current output->clear fullOP-> update output
            current_output = [str(eval(''.join(full_operation)))]
            full_operation.clear()
            window['-OUTPUT-'].update(''.join(current_output))

    if event == 'Clear':
        full_operation.clear()
        current_output.clear()
        window['-OUTPUT-'].update(''.join(current_output))



window.close()