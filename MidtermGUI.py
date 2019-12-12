from tkinter import *
from tkinter import messagebox
import requests


window = Tk()
window.geometry('600x300')
window.title("Programming with a Purpose Midterm")

lbl = Label(window, text="Welcome to the PWP Midterm GUI", font=("Arial Bold", 15))

lbl.place(x=125, y=50)




def clickedfwd():

    URL = "http://192.168.1.108:8080/fwd/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Forward")

def clickedbwd():

    URL = "http://192.168.1.108:8080/bwd/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Back")

def clickedlt():

    URL = "http://192.168.1.108:8080/lt/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Left")

def clickedrt():

    URL = "http://192.168.1.108:8080/rt/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Right")

def clickedser():
    URL = "http://192.168.1.108:8080/fwd/1"
    r = requests.get(url=URL)
    URL = "http://192.168.1.108:8080/rt/1"
    r = requests.get(url=URL)
    URL = "http://192.168.1.108:8080/fwd/1"
    r = requests.get(url=URL)
    URL = "http://192.168.1.108:8080/lt/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Through the Series")


fwdbtn = Button(window, text="Forward", bg="Pink", fg="white", command=clickedfwd, height=5, width=10)
fwdbtn.place(x=100, y=150, anchor='center')

bckbtn = Button(window, text="Backward", bg="Pink", fg="white", command=clickedbwd, height=5, width=10)
bckbtn.place(x=200, y=150, anchor='center')

ltbtn = Button(window, text="Left", bg="Pink", fg="white", command=clickedlt, height=5, width=10)
ltbtn.place(x=300, y=150, anchor='center')

rtbtn = Button(window, text="Right", bg="Pink", fg="white", command=clickedrt, height=5, width=10)
rtbtn.place(x=400, y=150, anchor='center')

serbtn = Button(window, text="Series", bg="Pink", fg="white", command=clickedser, height=5, width=10)
serbtn.place(x=500, y=150, anchor='center')

window.mainloop()
