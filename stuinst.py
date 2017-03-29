from Tkinter import *
from stdfunc import insvall,conclose
import os


root = None

idBox = None
nameBox = None
ageBox = None




def buttonPushed():
	global idBox
	global nameBox
	global ageBox
	id = int(idBox.get())
	name = nameBox.get()
	age = int(ageBox.get())
	insvall(id,name,age)
	


def createTextBox(parent):
	global idBox
	global nameBox
	global ageBox
	Label1 = Label(root,text="Enter Id")
	Label2 = Label(root,text="Enter Name")
	Label3 = Label(root,text="Enter Age")
	idBox = Entry(parent,bg="blue",fg="yellow",relief="flat",bd="4")
	nameBox = Entry(parent)
	ageBox = Entry(parent)
	Label1.pack()
	idBox.pack()
	Label2.pack()
	nameBox.pack()
	Label3.pack()
	ageBox.pack()

def Mbuttonclicked():
	conclose()
	root.destroy()
	os.system("stumain.exe")
	

def RbuttonPushed():
	global idBox
	global nameBox
	global ageBox
	idBox.delete(0,END)
	nameBox.delete(0,END)
	ageBox.delete(0,END)

def main():
	global root
	root = Tk() 
	root.title("Student DataBase Entry")
	createTextBox(root)
	Insbutton = Button(root, text="Insert",command=buttonPushed)
	Insbutton.pack()
	Revbutton = Button(root, text="Revert",command=RbuttonPushed)
	Revbutton.pack()
	Menubutton = Button(root, text="Menu",command=Mbuttonclicked)
	Menubutton.pack()
	root.mainloop()



main()
