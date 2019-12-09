from tkinter import *
from tkinter import messagebox
import requests
#from flaskCode import *

window = Tk()
window.geometry('600x300')
window.title("Programming with a Purpose Midterm")

lbl = Label(window, text="Welcome to the PWP Midterm GUI", font=("Arial Bold", 15))
#.grid(column=0, row=0)
lbl.place(x=125, y=50)




def clickedfwd():
    #AA3000.front(1)
    URL = "http://192.168.1.108:8080/fwd/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Forward")

def clickedbwd():
    #AA3000.back(1)
    URL = "http://192.168.1.108:8080/bwd/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Back")

def clickedlt():
    #AA3000.left(1)
    URL = "http://192.168.1.108:8080/lt/1"
    r = requests.get(url=URL)
    messagebox.showinfo("Status", "Successfully Moved Left")

def clickedrt():
    #AA3000.right(1)
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
#fwdbtn.grid(column=1, row=20)
fwdbtn.place(x=100, y=150, anchor='center')

bckbtn = Button(window, text="Backward", bg="Pink", fg="white", command=clickedbwd, height=5, width=10)
#bckbtn.grid(column=2, row=20)
bckbtn.place(x=200, y=150, anchor='center')

ltbtn = Button(window, text="Left", bg="Pink", fg="white", command=clickedlt, height=5, width=10)
#ltbtn.grid(column=3, row=20)
ltbtn.place(x=300, y=150, anchor='center')

rtbtn = Button(window, text="Right", bg="Pink", fg="white", command=clickedrt, height=5, width=10)
#rtbtn.grid(column=4, row=20)
rtbtn.place(x=400, y=150, anchor='center')

serbtn = Button(window, text="Series", bg="Pink", fg="white", command=clickedser, height=5, width=10)
#serbtn.grid(column=5, row=20)
serbtn.place(x=500, y=150, anchor='center')

window.mainloop()
