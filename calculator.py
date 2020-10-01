from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()

    elif text=="c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()
