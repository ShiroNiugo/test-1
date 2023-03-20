import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=500, bg="light green")
canvas.pack()

lastX, lastY = 0, 0
colour = "red"

def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

def onClick(event):
    store_position(event)

def onDrag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=3)
    store_position(event)

canvas.bind("<Button-1>", onClick)
canvas.bind("<B1-Motion>", onDrag)

redId = canvas.create_rectangle(10,10,30,30,fill="red")
blueId = canvas.create_rectangle(10,35,30,55,fill="blue")
greenId = canvas.create_rectangle(10,60,30,80,fill="green")
yellowId = canvas.create_rectangle(10,85,30,105,fill="yellow")

def setColourRed(event):
    global colour
    colour="red"
def setColourBlue(event):
    global colour
    colour="blue"
def setColourGreen(event):
    global colour
    colour="green"
def setColourYellow(event):
    global colour
    colour="yellow"

canvas.tag_bind(redId, "<Button-1>", setColourRed)
canvas.tag_bind(blueId, "<Button-1>", setColourBlue)
canvas.tag_bind(greenId, "<Button-1>", setColourGreen)
canvas.tag_bind(yellowId, "<Button-1>", setColourYellow)

window.mainloop()