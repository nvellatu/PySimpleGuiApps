# learned about how much I don't know about both tkinter and matplotlib
# learned about tables and how they work just like the layout of a window

import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    axes[0].plot(x,y,'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()


sg.theme('Dark')
table_content = []

layout = [
    [sg.Table(
        headings=['Observation', 'Result'],
        values= table_content,
        expand_x=True,
        key='-TABLE-'
    )],
    [sg.I(expand_x=True, key='-INPUT-'), sg.B('Submit')],
    [sg.Canvas(key='-CANVAS-')]
]

window = sg.Window('Grapher', layout, return_keyboard_events=True, finalize=True)

# matplotlib
fig = matplotlib.figure.Figure(figsize = (5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break

    if event in ['Submit', '\r']:
        if isfloat(values['-INPUT-']):
            table_content: table_content.append([len(table_content)+1, float(values['-INPUT-'])])
            window['-TABLE-'].update(table_content)
            update_figure(table_content)
        window['-INPUT-'].update(value = '')

window.close()