from Tkinter import *
from stdfunc import delvall,conclose
import os


root = None

idBox = None




def buttonPushed():
	global idBox
	id = int(idBox.get())
	delvall(id)
	


def createTextBox(parent):
	global idBox
	Label1 = Label(root,text="Enter Id")
	idBox = Entry(parent)
	Label1.pack()
	idBox.pack()

def Mbuttonclicked():
	conclose()
	root.destroy()
	os.system("stumain.exe")
	

def RbuttonPushed():
	global idBox
	idBox.delete(0,END)
	
def main():
	global root
	root = Tk() 
	root.title("Student DataBase Entry")
	createTextBox(root)
	Button1 = Button(root, text="Delete",command=buttonPushed)
	Button1.pack()
	Revbutton = Button(root, text="Revert",command=RbuttonPushed)
	Revbutton.pack()
	Menubutton = Button(root, text="Menu",command=Mbuttonclicked)
	Menubutton.pack()
	root.mainloop()



main()
