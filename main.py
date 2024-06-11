import tkinter as tk

root = tk.Tk()
root.title("Super Tic-Tac-Toe")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
buttons = {}

isXturn = True

def toggle(): 
    global isXturn
    isXturn = not isXturn
    
def disableOthers(id: str):
    index = int(id[1])
    alpha = alphabets[index]
    for i in buttons:
        if not i[0] == alpha:
            buttons[i].config(state = tk.DISABLED)
            buttons[i].config(bg="#808080")
        else:
            buttons[i].config(state = tk.NORMAL)
            buttons[i].config(bg="#ffffff")


def changeText(id: str):
    if (isXturn):
        buttons[id].config(text = "X")
        toggle()
        disableOthers(id=id)
    else:
        buttons[id].config(text = "0")
        toggle()
        disableOthers(id=id)

def createGrid(alphabet, columnStart, rowStart):
    rowCounter = rowStart
    columnCounter = columnStart
    for i in range(0, 9):
        button = tk.Button(root, text=" ", height=4, width=8, command=lambda sid=f"{alphabet}{i}": changeText(sid))
        button.grid(row=rowCounter, column=columnCounter)
        buttons[f"{alphabet}{i}"] = button
        columnCounter = columnCounter + 1
        if columnCounter == columnStart + 3:
            rowCounter = rowCounter + 1
            columnCounter = columnStart
    
rCounter = 0
cCounter = 0

for i in alphabets:
    createGrid(alphabet=i, columnStart=cCounter, rowStart=rCounter)
    
    cCounter = cCounter + 3
    if cCounter == 9:
        cCounter = 0
        rCounter += 3

root.mainloop()