import random
import time
from tkinter import * 
from tkinter import messagebox  
phrases = open("phrases.txt", "r")
data = phrases.read()
listdata = data.split("\n")
k = 1
while k == 1:
    time.sleep(3)
    messagebox.showinfo("Your annoying friend says:", random.choice(listdata))
