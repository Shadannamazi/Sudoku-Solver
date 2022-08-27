import tkinter as tk
from tkinter import *
from tkinter import messagebox
win = tk.Tk()
win.title("Sudoku")
win.configure(bg="#EEDFCC")
win.geometry("450x450")
mode_sudoku = tk.Label(text="Easy Mode",
fg="#8B8378",  
bg="#EEDFCC",
)
mode_sudoku.pack()

""""
frame = tk.LabelFrame(win,text="Mode:Easy")
frame.pack()
label_frame = tk.Label(win,text="hello")
label_frame.pack(padx=270,pady=270)
"""
#entry_num = tk.Entry(win,width=3)
#entry_num.pack()
def make_grid():
    pass
w = Canvas(win, width=450, height=450,bg="#EEDFCC")
w.create_rectangle(0, 0, 100, 100, fill="#EEDFCC", outline = "#8B8378")
w.create_rectangle(50, 50, 100, 100, fill="#EEDFCC", outline = "#8B8378")
w.pack()
#make a grid of buttens 
#button = tk.Button(width=10,height=10)
#button.pack()

win["bg"]="#EEDFCC"
#tk.tix.ButtonBox










win.mainloop()