import sys
import os
from tkinter import *

window = Tk()

window.title("Running Python Script")
window.geometry('300x100')


def run():
    os.system('python')


btn = Button(window, text=" Real Time object detection ", bg="black", fg="white", command=run)
btn.grid(column=0, row=0)


def run1():
    os.system(' python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel')


btn = Button(window, text="Run project  ", bg="blue", fg="white", command=run1)
btn.grid(column=0, row=60)


 

window.mainloop()
