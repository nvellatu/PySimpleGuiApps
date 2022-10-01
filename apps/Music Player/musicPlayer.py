# learned about using the pygame docs on my own
# learned about tabs
# figured out how to put in gifs into image elements

import base64
from io import BytesIO
from random import choice

import PySimpleGUI as sg
from PIL import Image
from pygame import mixer, time

mixer.init()
clock = time.Clock()


def base64_image_import(path):
    image = Image.open(path)
    bio = BytesIO()
    image.save(bio, format='PNG')
    return bio.getvalue()


# Import song
path = sg.popup_get_file('Open', no_window=True)
song_name = path.split('/')[-1].split('.')[0]
song = mixer.Sound(path)
mixer.music.load(path)

# Timer
song_length = song.get_length()
# time_since_start = 0
# pause_amount = 0
# playing = False

gifs = []
with open("dance-infinite-loop.gif", "rb") as img_file:
    gif = base64.b64encode(img_file.read())
    gifs.append(gif)
with open("200w.gif", "rb") as img_file:
    gif = base64.b64encode(img_file.read())
    gifs.append(gif)
with open("F3qm.gif", "rb") as img_file:
    gif = base64.b64encode(img_file.read())
    gifs.append(gif)

selected_gif = choice(gifs)

sg.theme('reddit')
play_layout = [
    [sg.VP()],
    [sg.Text(song_name, font='Times_New_Roman 20')],
    [sg.VP()],
    [
        sg.B(image_data=base64_image_import('play.png'), button_color='white', border_width=0, pad=(20, 5),
             key='-PLAY-'),
        sg.B(image_data=base64_image_import('pause.png'), button_color='white', border_width=0, pad=(20, 5),
             key='-PAUSE-')
    ],  # try and see if you can make do with a single button
    [sg.VP()],
    [sg.Progress(100, size=(20, 20), key='-PROGRESS-')],
    [sg.Image(data=selected_gif, key='_IMAGE_')]
]

volume_layout = [
    [sg.VP()],
    [sg.Slider(range=(0, 100), default_value=69, orientation='h', key='-VOLUME-', enable_events=True)],
    [sg.VP()]
]

layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout, element_justification='center'),
                   sg.Tab('Volume', volume_layout, element_justification='center')]])]
]

window = sg.Window('Music Player', layout)

while True:
    event, values = window.read(timeout=40)
    if event == sg.WIN_CLOSED: break
    window.Element('_IMAGE_').UpdateAnimation(selected_gif)

    if event == '-PLAY-':
        if mixer.music.get_pos() > 0:
            # mixer.unpause()
            mixer.music.unpause()
        else:
            # song.play()
            mixer.music.play()
        # window['-PROGRESS-'].update(50)
    if event == '-PAUSE-':
        # mixer.pause()
        mixer.music.pause()
    if event == '-VOLUME-': mixer.music.set_volume(values['-VOLUME-'] / 100)

    window['-PROGRESS-'].update(mixer.music.get_pos() / (song.get_length() * 10))

window.close()
