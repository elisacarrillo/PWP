from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('600x300')
window.title("Programming with a Purpose Midterm")

lbl = Label(window, text="Welcome to the PWP Midterm GUI", font=("Arial Bold", 15))
#.grid(column=0, row=0)
lbl.place(x=125, y=50)


def clickedfwd():
    messagebox.showinfo("Status", "Working... Moving Forward")

def clickedbwd():
    messagebox.showinfo("Status", "Working... Moving Backward")

def clickedlt():
    messagebox.showinfo("Status", "Working... Moving Left")

def clickedrt():
    messagebox.showinfo("Status", "Working... Moving Right")

def clickedser():
    messagebox.showinfo("Status", "Working... Moving Through the Series")


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
