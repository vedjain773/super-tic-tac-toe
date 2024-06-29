import tkinter as tk

root = tk.Tk()
root.title("Super Tic-Tac-Toe")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
buttons = {}
claimed = {}

isXturn = True

def checkDiag(alpha, letter):
    if (aBT(f"{alpha}0") == aBT(f"{alpha}4") == aBT(f"{alpha}8") == letter):
        return True
    elif (aBT(f"{alpha}2") == aBT(f"{alpha}4") == aBT(f"{alpha}6") == letter):
        return True
    else:
        return False

def enableUnclaimed(abet):
    if abet in claimed:
        disableGrid(abet)
    else:
        for i in range (0, 9):
            id = f"{abet}{i}"
            buttons[id].config(state = tk.NORMAL)
            buttons[id].config(bg="#ffffff")

def disableGrid(alphabet):
    for i in range (0, 9):
        id = f"{alphabet}{i}"
        buttons[id].config(state = tk.DISABLED)
        buttons[id].config(bg="#808080")

def aBT(id: str):
    return buttons[id].cget("text")

def checkGrid(alpha):
    
    if checkDiag(alpha, "X"):
        claimed[f"{alpha}"] = "X"
        disableGrid(alpha)
    elif checkDiag(alpha, "O"):
        claimed[f"{alpha}"] = "O"
        disableGrid(alpha)
    
    rows = [0, 3, 6]
    columns = [0, 1, 2]
    for row in rows:
        if checkThree(alpha, row, "X", True):
            claimed[f"{alpha}"] = "X"
            disableGrid(alpha)
        elif checkThree(alpha, row, "O", True):
            claimed[f"{alpha}"] = "O"
            disableGrid(alpha)

    for col in columns:
        if checkThree(alpha, col, "X", False):
            claimed[f"{alpha}"] = "X"
            disableGrid(alpha)
        elif checkThree(alpha, col, "O", False):
            claimed[f"{alpha}"] = "O"
            disableGrid(alpha)

def checkAll():
    for i in alphabets:
        checkGrid(i)
    print(claimed)

def checkThree(alphabet, num, letter, row: bool):
    if (row):
        return aBT(f"{alphabet}{num}") == aBT(f"{alphabet}{num + 1}") == aBT(f"{alphabet}{num + 2}") == letter
    else:
        return aBT(f"{alphabet}{num}") == aBT(f"{alphabet}{num + 3}") == aBT(f"{alphabet}{num + 6}") == letter

def toggle(): 
    global isXturn
    isXturn = not isXturn
    
def disableOthers(id: str):
    index = int(id[1])
    alpha = alphabets[index]
    for i in buttons:
        if not i[0] == alpha or alpha in claimed:
            buttons[i].config(state = tk.DISABLED)
            buttons[i].config(bg="#808080")
            if alpha in claimed:
                for j in alphabets:
                    enableUnclaimed(j)
        else:
            buttons[i].config(state = tk.NORMAL)
            buttons[i].config(bg="#ffffff")


def changeText(id: str):
    if (isXturn):
        buttons[id].config(text = "X")
        toggle()
        checkAll()
        disableOthers(id=id)
    else:
        buttons[id].config(text = "O")
        toggle()
        checkAll()
        disableOthers(id=id)

def createGrid(alphabet, columnStart, rowStart):
    rowCounter = rowStart
    columnCounter = columnStart
    for i in range(0, 9):
        button = tk.Button(root, text=" ", height=1, width=3, font=("Helvetica", 30), command=lambda sid=f"{alphabet}{i}": changeText(sid))
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