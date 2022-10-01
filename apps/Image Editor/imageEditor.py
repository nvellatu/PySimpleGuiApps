# learned about how much I don't know about PIL and image storage
# learned about using columns and frames
# learned about taking input from values and using it to continually alter an image

import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO


def update_image(original, values):
    global image
    image = original.filter(ImageFilter.GaussianBlur(values['-BLUR-']))
    image = image.filter(ImageFilter.UnsharpMask(values['-CONTRAST-']))
    image = image.rotate(values['-ROTATION-'])
    if values['-EMBOSS-']: image = image.filter(ImageFilter.EMBOSS)
    if values['-CONTOUR-']: image = image.filter(ImageFilter.CONTOUR)
    if values['-FLIPY-']: image = ImageOps.flip(image)
    if values['-FLIPX-']: image = ImageOps.mirror(image)
    bio = BytesIO()
    image.save(bio, format='PNG')

    window['-IMAGE-'].update(data= bio.getvalue())

sg.theme('DarkAmber')

image_path = sg.popup_get_file('Choose Image',file_types=(('PNG Image','*.png'),), no_window=True)

control_column = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-', resolution=.1, enable_events=True)]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0,10), orientation='h', key='-CONTRAST-', resolution=.1, enable_events=True)]])],
    [sg.Frame('Rotation', layout=[[sg.Slider(range=(0,360), orientation='h', key='-ROTATION-', enable_events=True)]])],
    [sg.Check('Flip X', k='-FLIPX-', enable_events=True), sg.Check('Flip Y', k='-FLIPY-', enable_events=True)],
    [sg.Check('Emboss', k='-EMBOSS-', enable_events=True), sg.Check('Contour', k='-CONTOUR-', enable_events=True)],
    [sg.B('Save', k='-SAVE-')]
])
original = Image.open(image_path)

layout = [
    [control_column, sg.Image(image_path, key='-IMAGE-')]
]

window = sg.Window('Image Editor', layout)

while True:
    # print(window.read())
    event, values = window.read()
    if event == sg.WIN_CLOSED: break

    update_image(original, values)

    if event == '-SAVE-':
        save_path = sg.popup_get_file('Save as', save_as=True, no_window=True)
        if '.png' not in save_path: save_path += '.png'
        if save_path:
            image.save(save_path, 'PNG')

window.close()