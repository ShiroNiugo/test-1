import tkinter
import random

gameOver = False
score = 0
squaresToClear = 0

bombfield = []
def createBombfield(bombfield):
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)
    printfield(bombfield)

def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

def layoutWindow(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text = "    ", bg="darkgreen")
            elif random.randint(1,100) > 75:
                square = tkinter.Label(window, text = "    ", bg="seagreen")
            else:
                square = tkinter.Label(window, text = "    ", bg="green")
            square.grid(row = rowNumber, column=columnNumber)
            square.bind("<Button-1>", onClick)

def onClick(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver = True
            square.config(bg="red")
            print("Game Over Bleat!")
            print("You score was:", score)
        elif currentText == "    ":
            square.config(bg = "brown")
            totalBombs = 0
            if row < 9:
                if bombfield[row+1][column] == 1:
                    totalBombs = totalBombs + 1
            if row > 0:
                if bombfield[row-1][column] == 1:
                    totalBombs = totalBombs + 1
            if column > 0:
                if bombfield[row][column-1] == 1:
                    totalBombs = totalBombs + 1
            if column < 9:
                if bombfield[row][column+1] == 1:
                    totalBombs = totalBombs + 1
            if row > 0 and column > 0:
                if bombfield[row-1][column-1] == 1:
                    totalBombs = totalBombs + 1
            if row < 9 and column > 0:
                if bombfield[row+1][column-1] == 1:
                    totalBombs = totalBombs + 1
            if row > 0 and column < 9:
                if bombfield[row-1][column+1] == 1:
                    totalBombs = totalBombs + 1
            if row < 9 and column < 9:
                if bombfield[row+1][column+1] == 1:
                    totalBombs = totalBombs + 1
            square.config(text =" "+str(totalBombs)+" ")
            squaresToClear-=1
            score+=1
            if(squaresToClear==0):
                gameOver = True
                print("Well done!")
                print("You score was:", score)

def playBombdodger():
    createBombfield(bombfield)
    window = tkinter.Tk()
    layoutWindow(window)
    window.mainloop()

playBombdodger()