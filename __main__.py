import os
import hasteApi as haste
import tkinter as tk
import json

root = tk.Tk()

def get():
    key = KeyBar.get("1.0", 'end-1c')
    Editor.delete("1.0", 'end-1c')

    a = haste.get(key)
    b = json.loads(str(a))
    data = b['data']

    Editor.insert('end-1c', data)

def post():
    data = Editor.get("1.0", 'end-1c')
    KeyBar.delete("1.0", 'end-1c')

    a = haste.post(data)
    b = json.loads(a)
    key = b['key']

    KeyBar.insert('end-1c', key)

def save():
    key = KeyBar.get("1.0", 'end-1c')
    file = open('saved.txt', 'a')
    file.write(key + '\n')
    file.close()

def load():
    Editor.delete("1.0", 'end-1c')
    Editor.insert('end-1c', 'here are your saved keys:\n')
    Editor.insert('end-1c', 'copy one and paste it to the keybar \n')
    file = open('saved.txt', 'r')
    lines = file.readlines()
    for a in lines:
        Editor.insert('end-1c', f'{a}')

root.title("HasteClient By BLINMATIC")
root.geometry("460x290")
root.resizable(width=False, height=False)
root.iconbitmap('icon.ico')

PostButton = tk.Button(root, text="Post", width=15, height=1, command=lambda: post())
GetButton = tk.Button(root, text="Get", width=15, height=1, command=lambda: get())
SaveButton = tk.Button(root, text="Save Key", width=15, height=1, command=lambda: save())
OpenSavesButton = tk.Button(root, text="Open Saved Keys", width=15, height=1, command=lambda: load())

KeyBar = tk.Text(root, width=57, height=1, padx=2)
Editor = tk.Text(root, width=57, height=15, padx=2)

PostButton.place(x=0, y=0)
GetButton.place(x=115, y=0)
SaveButton.place(x=230, y=0)
OpenSavesButton.place(x=345, y=0)

KeyBar.place(x=0, y=25)
Editor.place(x=0, y=45)

KeyBar.insert('end-1c', 'kidakigaza')
get()

root.mainloop()
