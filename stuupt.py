from Tkinter import *
from stdfunc import chckupdt,updt,conclose
import os


root = None

idBox = None
nameBox = None



def checkbuttonPushed():
	global idBox
	global nameBox
	ids = int(idBox.get())
	txt = chckupdt(ids)
	nameBox.delete(0,END)
	nameBox.insert("0",txt)
	
def updatebuttonPushed():
	global idBox
	global nameBox
	id = int(idBox.get())
	name = nameBox.get()
	updt(id,name)

def RbuttonPushed():
	global idBox
	global nameBox
	idBox.delete(0,END)
	nameBox.delete(0,END)


def createTextBox(parent):
	global idBox
	global nameBox
	Label1 = Label(root,text="Enter Id")
	idBox = Entry(parent)
	Label2 = Label(root,text="Enter Name")
	nameBox = Entry(parent)
	Label1.pack()
	idBox.pack()
	Label2.pack()
	nameBox.pack()
	

def Mbuttonclicked():
	conclose()
	root.destroy()
	os.system("stumain.exe")
	

def main():
	global root
	root = Tk() 
	root.title("Student DataBase Entry")
	createTextBox(root)
	Cbutton = Button(root, text="Check",command=checkbuttonPushed)
	Cbutton.pack()
	Ubutton = Button(root, text="Update",command=updatebuttonPushed)
	Ubutton.pack()
	Revbutton = Button(root, text="Revert",command=RbuttonPushed)
	Revbutton.pack()
	Menubutton = Button(root, text="Menu",command=Mbuttonclicked)
	Menubutton.pack()
	root.mainloop()



main()
