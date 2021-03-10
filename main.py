import tkinter as tk
from tkinter import Message, Text
import cv2,os
import csv
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyrebase
from firebase import firebase
from google.cloud import storage
from google.cloud.storage.blob import Blob



window = tk.Tk()
window.title("GUI programe")
window.configure(background='black')
window.geometry('1200x600')

lbl = tk.Label(window, text="Face Recognition Based Attendance System", bg="white", fg="black", width=50, height=3, font=('times', 30, 'italic bold'))
lbl.place(x=100, y=20)

lbl1 = tk.Label(window, text="↓  List Of Present Students  ↓", width=25, fg="black", bg="white", height=2, font=('times', 15, ' bold'))
lbl1.place(x=540, y=320)

message = tk.Label(window, text="", fg="black", bg="white", activeforeground = "green", width=35, height=7, font=('times', 15, ' bold '))
message.place(x=470, y=400)






window.mainloop()