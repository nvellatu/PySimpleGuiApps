import tkinter as tk        #create gui
from tkinter import filedialog, Text        #pick apps, display text
import os       #lets us run apps

root = tk.Tk()
apps = []       #tuples: (fileName, selected?)

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read().split(',')
        # apps = [(x, False, lambda: select(x)) for x in tempApps if x.strip()]
        tempApps = [x for x in tempApps if x.strip()]
        for i in range (0, len(tempApps)):
            filename = tempApps[i]
            apps.append((filename, False, lambda: select(filename)))


        # print(apps)

def addApp():

    for widget in frame.winfo_children():   #you can also solve the removal issue by just not repetively placing them
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"),("all files", "*.*")))
    apps.append((filename, False, lambda: select(filename)))
    # print(filename)
    # for app in apps:
    #     if app[1]:
    #         label = tk.Button(frame, text=app[0], bg="blue", fg="black", command=lambda: select(app[0]))
    #     else:
    #         label = tk.Button(frame, text=app[0], bg="grey", fg="black", command=lambda: select(app[0]))
    for i in range(0, len(apps)):
        if apps[i][1]:
            label = tk.Button(frame, text=apps[i][0], bg="blue", fg="black", command=apps[i][2])
        else:
            label = tk.Button(frame, text=apps[i][0], bg="grey", fg="black", command=apps[i][2])
        # label = tk.Label(frame, text=app, bg="grey")
        # tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app[0])

def select(fileName):
    print(fileName)



canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,
                    fg="white", bg="#263D42", command=runApps)
runApps.pack()

# for app in apps:
#     label = tk.Button(frame, text=app[0], bg="grey", fg="black", command=lambda: select(apps[i][0]))
#     label.pack()
for i in range(0, len(apps)):
    label = tk.Button(frame, text=apps[i][0], bg="grey", fg="black", command=apps[i][2])
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app[0] + ',')

