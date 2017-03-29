import os
import tkMessageBox
from Tkinter import *
root = None

def insbuttonPushed():
	root.destroy()
	os.system("stuinst.exe")
	
def delbuttonPushed():
	root.destroy()
	os.system("studel.exe")

def updtbuttonPushed():
	root.destroy()
	os.system("stuupt.exe")
	

def Qbuttonclicked():
	tkMessageBox.showinfo("From Programmers","Thank You For Using Our Software")
	root.destroy()
	
def main():
	global root
	root = Tk() 
	root.title("Student DataBase Entry")
	Insbutton = Button(root, text="Insert",command=insbuttonPushed)
	Insbutton.pack()
	Delbutton = Button(root, text="Delete",command=delbuttonPushed)
	Delbutton.pack()
	Uptbutton = Button(root, text="Update",command=updtbuttonPushed)
	Uptbutton.pack()
	Qbutton = Button(root, text="Quit",command=Qbuttonclicked)
	Qbutton.pack()
	root.mainloop()



main()
