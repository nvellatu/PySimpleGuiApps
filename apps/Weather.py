import PySimpleGUI as sg

image_col = sg.Column()
info_col = sg.Column()

layout = [
    [sg.I(expand_x=True, key='-INPUT-'), sg.B('Enter')],
    [image_col, info_col]
]

window = sg.Window('Weather', layout, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break

window.close()


# if 'M' in s:
#             section = s[0:s.rfind('M', 0)+1]
#             value = section.count('M')*1000
#             value -= section.count('D')*500
#             value -= section.count('C')*100
#             value -= section.count('L')*50
#             value -= section.count('X')*10
#             value -= section.count('V')*5
#             value -= section.count('I')
#             return value