# learned about multiline; more about element customization; about menu and how to make menu items
# learned about opening files, writing in them, saving them, naming them, and such with popups

import PySimpleGUI as sg
from pathlib import Path


faces_manu = [
    'Happy',['｡◕‿‿◕｡','\ (•◡•) /','ヽ༼ʘ̚ل͜ʘ̚༽ﾉ','㋡','ԅ། ^ ͜ʟ ^ །و','( ━☞´◔‿ゝ◔`)━☞'],
    'Sad', ['T ʖ̯ T','(   ͡°╭╮ʖ   ͡°)','(◞‸◟；)','(⌣́_⌣̀)','(͡๏̯͡๏)','(╯︵╰,)'],
    'Other',['───==≡≡ΣΣ((( つºل͜º)つ','༼ つ ✿◕‿◕✿༽つ (‿ˠ‿)','t(-_-t)','(｀㊥益㊥)Ψ','❚█══█❚','❤','(▀̿Ĺ̯▀̿ ̿)','╾━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)','¯\_(⊙_ʖ⊙)_/¯','( ͡°❥ ͡°)']
]
faces = faces_manu[1] + faces_manu[3] + faces_manu[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', faces_manu]
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.T('Untitled', k='-DOCNAME-')],
    [sg.Multiline(size=(69,30), key='-TEXTBOX-')]
]

window = sg.Window('Text Editor', layout)

while True:
    # print(window.read())
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        file_path = sg.popup_get_file('Choose file to open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1].replace('.txt', ''))


    if event == 'Save':
        file_path = sg.popup_get_file('the most useless mf to egzicte', no_window=True, save_as=True)
        if '.txt' not in file_path: file_path+= '.txt'
        if file_path:
            file = Path(file_path)
            file.write_text(values['-TEXTBOX-'])



    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        words_list = [word for word in full_text.replace('\n', ' ').split(' ') if word != '']
        word_count = len(words_list)
        char_count = len(''.join(words_list))
        sg.popup(f'Words: {word_count}\nCharacters: {char_count}')

    if event in faces:
        window['-TEXTBOX-'].update(values['-TEXTBOX-'] + ' ' + event)

    if event == 'Exit':
        break



window.close()