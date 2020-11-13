import tkinter as tk
import time
import random 
from random_txt import randomTXT
import tkinter.font as tkFont
from functools import partial

window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("600x400")


def display_result(entry, ientity, window, ans, start_time):
    
    input_ans = entry.get()
    window.after_cancel(ientity)
    window.destroy()
    print(input_ans + "<--this is input")
    print(ans + "<--this is input")

    res_panel = tk.Tk()
    res_panel.title("Result")
    t_end = time.time() 
    total_t = t_end - start_time
    
    a = True
    if len(input_ans) != len(ans):
        a = False
    else:   
        for i in range(len(ans)):
            if ans[i]!=input_ans[i]:
                a = False
        
    if  a :
        res = tk.StringVar()
        speed = round(len(ans)/total_t,4)
        speed_str = str(speed)
        if speed <= 2:
            res.set("You slow as fuck! Your typing speed is " + speed_str + " words per second!")
        elif speed < 10 and total_t > 2:
            res.set("Your typing speed is " + speed_str + " words per second. You are just normal people") 
        else:
            res.set("You are a typing GODDDD! Your typing speed is " + speed_str + " words per second!") 
        
        label = tk.Label(res_panel, textvariable = res, fg='red', font=("Lucida Grande","15","bold"), wraplength=500, padx=40, pady=25)
        label.pack() 

    else:
        res = tk.StringVar()
        res.set("Are you blind or what? can you even type it right??? Try one more fucking time!")
        label = tk.Label(res_panel, textvariable = res, fg='red', font=("Lucida Grande","15","bold"), wraplength=500, padx=40, pady=25)
        label.pack() 

        #try_again
        try_again = tk.Button(res_panel, text="I'm stupid, I quit.", bg="white", fg="black", padx=20, pady=10, command = res_panel.destroy)
        try_again.pack()


def game_window(win):
    #time that input start
    t0 = time.time()   
    
    def close_app():
        game_pad.destroy()
    
    #assign sentence to string var
    def set_sentence():
        res = randomTXT()
        return res
    #reset time
    def show_count_down (count = 0):
        identity = 0
        identity = game_pad.after(1000, show_count_down, count + 1)  
        if count <= 5:
            countdown_label["text"] = str(count) + " s has been spent."
        
        elif count <= 20:
            countdown_label["text"] = str(count) + " s has been spent. Hurry the fuck up you pig"

        else:
            countdown_label["text"] = "Hopeless shit, go fuck your mom"
        return identity

    
    
    
    #close previous window
    win.destroy()
    #create a new window for typing speed test
    game_pad = tk.Tk()
    game_pad.title("Test")
    game_pad.geometry("600x300")
    
    #create entry widget for user input
    entry = tk.Entry(game_pad)
    entry.place(height = 50, width = 500, x = 50, y = 150)
    #initiate a var for sentence display
    sentence = tk.StringVar()
    s = set_sentence()
    sentence.set(s)
    #sentence label
    goal = tk.Label(game_pad, textvariable = sentence, fg='red', font=("Lucida Grande","15","bold"), wraplength=500, padx=40, pady=25)
    goal.pack() 
    #timer label  
    countdown_label = tk.Label(game_pad)
    countdown_label.pack(side = "bottom")
    identity = show_count_down(0)
    #finish button
    finish = tk.Button(game_pad, text="FINISH", bg="white", fg="black", padx=20, pady=10,command = partial(display_result, entry,identity, game_pad, s, t0))
    finish.place(x = 50, y = 225)
    #switch up button   
    switch = tk.Button(game_pad, text="SWITCH", bg="white", fg="black", padx=20, pady=10)
    switch.place(x = 245, y = 225)
    #quit button
    Quit = tk.Button(game_pad, text="QUIT", bg="white", fg="black", padx=20, pady=10, command =close_app)
    Quit.place(x = 460, y = 225)
    

    
    
    game_pad.mainloop()

start = tk.Button(window, text = "START!",font=("Lucida Grande","30","bold"), padx=50, pady=50, command = partial(game_window, window))
start.pack(side = tk.LEFT)

frameCnt = 15
frames = [tk.PhotoImage(file='simplegif.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind, root = window):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


label = tk.Label(window)
label.pack()
window.after(0, update, 0)

window.mainloop()





