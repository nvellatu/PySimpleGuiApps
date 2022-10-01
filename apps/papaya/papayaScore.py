import PySimpleGUI as sg
from datetime import datetime, date
from pathlib import Path

format = "%m/%d/%Y"
POINTS_ADDED_PER_DAY = 5
P = -30
FP = -10


#get current date to update streak and set default input value
today = date.today()
today = list(str(today).split("-"))
today = today[1] + "/" + today[2] + '/' + today[0]


#get recorded info: [score,failed habit date, current date, highest streak]
file_path = 'scorekeeper.txt'
if file_path:
    file = Path(file_path)
else:
    print("Score keeper not found")
    exit()
data = file.read_text().split(',')
data[0] = int(data[0])

#add points and update streak
currDate = datetime.strptime(today, format)
mostRecentDate = datetime.strptime(data[2], format)
failedHabitDate = datetime.strptime(data[1], format)        #streak = currDate-fhd      #added score = currDate-mrd
streak = (currDate - failedHabitDate).days
if streak > int(data[3]): data[3] = streak
data[0] += (currDate - mostRecentDate).days * POINTS_ADDED_PER_DAY     #add score
data[2] = today


sg.theme('LightBrown13')
layout = [
    [sg.B("P", expand_x=True),sg.B("FP",expand_x=True)],
    [sg.T(today, justification='center', key="-DATE-", enable_events=True, expand_x=True, font="Young 15")],
    [sg.VPush()],
    [sg.T(data[0],key='-SCORE-', expand_x=True, expand_y=True, justification="center", font="Young 50")],
    [sg.VP()],
    [sg.T("Current Streak: "), sg.T(streak, key='-STREAK-')],
    [sg.T("Highest Streak: "), sg.T(data[3])]
]



window = sg.Window("Papaya Score", layout, size=(300,300), return_keyboard_events=True)
# values = {'-DATE-': None}
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:break

    if event == 'P':
        data[0] += P
        data[1] = today

    if event == 'FP':
        data[0] += FP
        data[1] = today

    window['-SCORE-'].update(data[0])


data = [str(x) for x in data]
print(",".join(data))
if file_path:
    file = Path(file_path)
    file.write_text(",".join(data))



