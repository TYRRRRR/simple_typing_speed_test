import tkinter as tk
import time
import random 
from random_txt import randomTXT
import tkinter.font as tkFont
from functools import partial
import os




root = tk.Tk()

frameCnt = 30
frames = [tk.PhotoImage(file='simplegif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = tk.Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()