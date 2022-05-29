from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from att import Face_Recognition
import numpy as np
import cv2 
import os
import sys 
import csv
import mysql.connector


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("430x200+400+200")
        self.root.title("Help")
        
        #background image
        img=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\bb.jpg")
        img=img.resize((430,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=200)
        
        title_lbl=Label(self.root,text="       Queries?",font=("Calibri Light",15),fg="black")
        title_lbl.place(x=1,y=10,width=150,height=30)
        
        email=Label(self.root,text="Contact: golishrija@gmail.com",font=("Calibri Light",15),fg="black")
        email.place(x=60,y=80,width=300,height=30)
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()