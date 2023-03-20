import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text = "Red button", width=40)
button.pack(padx=10, pady=10)
clickCount = 0
    
def onClick(event):
    global clickCount
    textBleat="Bleat "
    clickCount += 1
    button.configure(text=textBleat*clickCount if clickCount<4 else None)
    if clickCount == 4:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
"""
import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text = "Red button", width=40)
button.pack(padx=10, pady=10)

clickCount = 0

def onClick(event):
    global clickCount
    textBleat="Bleat "
    clickCount = clickCount+1
    if clickCount == 1:
        button.configure(text=textBleat)
    elif clickCount == 2:
        button.configure(text=textBleat*2)
    elif clickCount == 3:
        button.configure(text=textBleat*3)
    else:
        button.pack_forget()

button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
"""