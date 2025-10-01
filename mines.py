import tkinter as tk
from tkinter import messagebox
import random

def build(rows, columns, difficulty):
    root = tk.Tk()
    root.title("Minesweeper")
    buttonState = []

    def show(si, sj):
        if buttonState[buttonDictIndex(si, sj)].get("mineNeighs") == 0:
            buttonState[buttonDictIndex(si, sj)].get("object").config(text = " ")
        elif buttonState[buttonDictIndex(si, sj)].get("mineNeighs") == -1:
            buttonState[buttonDictIndex(si, sj)].get("object").config(text = "B")
        else:
            buttonState[buttonDictIndex(si, sj)].get("object").config(text = checkState(si, sj, "mineNeighs"))
        buttonState[buttonDictIndex(si, sj)]["revealed"] = True
        buttonState[buttonDictIndex(si, sj)].get("object").config(bg = "#808080")

    def dig(arr: list):
        si = arr[0]
        sj = arr[1]

        show(si, sj)
        if checkState(si, sj, "mineNeighs") == 0:
            if si - 1 >= 0 and sj - 1 >= 0:
                if checkState(si-1, sj-1, "revealed") == False or isCellBomb(si-1, sj-1):
                    dig([si-1, sj-1])
            if si - 1 >= 0 and sj >= 0:
                if checkState(si-1, sj, "revealed") == False or isCellBomb(si-1, sj):
                    dig([si-1, sj])
            if si - 1 >= 0 and sj + 1 <= columns - 1:
                if checkState(si-1, sj+1, "revealed") == False or isCellBomb(si-1, sj+1):
                    dig([si-1, sj+1])
            if si >= 0 and sj - 1 >= 0:
                if checkState(si, sj-1, "revealed") == False or isCellBomb(si, sj-1):
                    dig([si, sj-1])
            if si >= 0 and sj + 1 <= columns - 1:
                if checkState(si, sj+1, "revealed") == False or isCellBomb(si, sj+1):
                    dig([si, sj+1])
            if si + 1 <= rows - 1 and sj - 1 >= 0:
                if checkState(si+1, sj-1, "revealed") == False or isCellBomb(si+1, sj-1):
                    dig([si+1, sj-1])
            if si + 1 <= rows - 1 and sj >= 0:
                if checkState(si+1, sj, "revealed") == False or isCellBomb(si+1, sj):
                    dig([si+1, sj])
            if si + 1 <= rows - 1 and sj + 1 <= columns - 1:
                if checkState(si+1, sj+1, "revealed") == False or isCellBomb(si+1, sj+1):
                    dig([si+1, sj+1])
        elif isCellBomb(si, sj):
            messagebox.showinfo("GAME OVER", "You lost!")
        checkWon()

    def createGrid():
        for i in range(0, rows):
            for j in range(0, columns):
                buttons = {}
                button = tk.Button(root, text=" ", height=1, width=1, font=("Helvetica", 30), command= lambda arr = [i, j]: dig(arr))
                button.grid(row=i, column=j)

                buttons["name"] = [i, j]
                buttons["object"] = button
                buttons["isBomb"] = False
                buttons["mineNeighs"] = -1
                buttons["revealed"] = False
                buttonState.append(buttons)

    randomPos = []
    upper = 0
    if difficulty == 1:
    	upper = 0.1
    elif difficulty ==2:
    	upper = 0.2
    else:
    	upper = 0.3
    	
    upper_lim = int(upper*rows*columns)
    for i in range(0, upper_lim):
        ranPosStr = [random.randint(0, rows - 1), random.randint(0, columns - 1)]
        if ranPosStr not in randomPos:
            randomPos.append(ranPosStr)

    createGrid()

    for i in range(0, len(buttonState)):
        if buttonState[i].get("name") in randomPos:
            buttonState[i]["isBomb"] = True

    def buttonDictIndex(si, sj):
        for i in range(0, len(buttonState)):
            if buttonState[i].get("name") == [si, sj]:
                return i
            
    def isCellBomb(si, sj):
        state = buttonState[buttonDictIndex(si, sj)].get("isBomb")
        return state

    def checkState(si, sj, prop):
        ind = buttonDictIndex(si, sj)
        val = buttonState[ind].get(prop)
        return val

    def calcNeighbours(si, sj):
        neigh = 0
        if not isCellBomb(si, sj):
            if si - 1 >= 0 and sj - 1 >= 0:
                if isCellBomb(si - 1, sj - 1):
                    neigh += 1
            if si - 1 >= 0 and sj >= 0:
                if isCellBomb(si - 1, sj):
                    neigh += 1
            if si - 1 >= 0 and sj + 1 <= columns - 1:
                if isCellBomb(si - 1, sj + 1):
                    neigh += 1
            if si >= 0 and sj - 1 >= 0:
                if isCellBomb(si, sj - 1):
                    neigh += 1
            if si >= 0 and sj + 1 <= columns - 1:
                if isCellBomb(si, sj + 1):
                    neigh += 1
            if si + 1 <= rows - 1 and sj - 1 >= 0:
                if isCellBomb(si +1, sj - 1):
                    neigh += 1
            if si + 1 <= rows - 1 and sj >= 0:
                if isCellBomb(si + 1, sj):
                    neigh += 1
            if si + 1 <= rows - 1 and sj + 1 <= columns - 1:
                if isCellBomb(si + 1, sj + 1):
                    neigh += 1
        else:
            neigh = -1
        return neigh

    for i in range(0, len(buttonState)):
        arr = buttonState[i].get("name")
        neighs = calcNeighbours(arr[0], arr[1])
        buttonState[i]["mineNeighs"] = neighs

    def checkWon():
        count = 0
        for i in range(0, len(buttonState)):
            if buttonState[i].get("revealed") == False:
                count += 1
        if count == len(randomPos):
            messagebox.showinfo("GAME OVER", "You Won!")

    root.mainloop()

rows = int(input("Enter the number of rows (min 10): "))
columns = int(input("Enter the number of columns (min 10): "))
difficulty = int(input("Select game difficulty (1/2/3): \n1.Easy\n2.Medium\n3.Hard\n"))

if rows >= 10 and columns >= 10:
	if difficulty == 1 or difficulty == 2 or difficulty == 3:
		build(rows, columns, difficulty)
