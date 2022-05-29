from tkinter import*
import tkinter
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
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x660+0+0")
        self.root.title("Face Recognition System")

        #background image
        img=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\bg.jpeg")
        img=img.resize((1270,660),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1270,height=660)


        title_lbl=Label(text="     ATTENDANCE TRACKER",font=("arial",25),fg="black")
        title_lbl.place(x=1,y=10,width=500,height=50)

        #register button
        img1=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\rg.jpg")
        img1=img1.resize((150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1= Button(image=self.photoimg1,command=self.student_details,cursor="hand2") 
        b1.place(x=100,y=200,width=150,height=150)

        b1_2= Button(text = "REGISTER HERE",command= self.student_details ,font=("arial",10),fg="black", cursor="hand2") 
        b1_2.place(x=100,y=350,width=150,height=40) 

        #give attendance
        img2=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\at.png")
        img2=img2.resize((150,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2= Button(image=self.photoimg2,command=self.face_data,cursor="hand2") 
        b2.place(x=400,y=200,width=150,height=150)

        b2_2= Button(command=self.face_data,text = "GIVE ATTENDANCE",font=("arial",10),fg="black", cursor="hand2") 
        b2_2.place(x=400,y=350,width=150,height=40) 
        
        #help button
        img3=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\help.png")
        img3=img3.resize((150,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3= Button(command=self.help_box,image=self.photoimg3,cursor="hand2") 
        b3.place(x=700,y=200,width=150,height=150)

        b3_2= Button(text = "HELP",command=self.help_box,font=("arial",10),fg="black", cursor="hand2") 
        b3_2.place(x=700,y=350,width=150,height=40) 

        #exit button
        img4=Image.open(r"C:\Users\golis\OneDrive\Desktop\face recognition\exit.png")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4= Button(image=self.photoimg4,command=self.iExit,cursor="hand2") 
        b4.place(x=1000,y=200,width=150,height=150)

        b4_2= Button(text = "EXIT",font=("arial",10),command=self.iExit,fg="black", cursor="hand2") 
        b4_2.place(x=1000,y=350,width=150,height=40) 

     #functions to buttons

    def student_details(self):  
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def face_data(self):  
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def help_box(self):  
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
    def iExit(self):  
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit?",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else :
            return
            




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

