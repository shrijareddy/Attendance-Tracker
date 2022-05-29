import tkinter as tk
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2 
import os
import sys 
import csv
import mysql.connector



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("340x150+300+300")
        self.root.title("Train")
        
        train_btn=Button(self.root,text="Click here to Save",command=self.train_classifier,font=("arial",10),bg="lavender",fg="black")
        train_btn.place(x=60,y=40,height=30,width=200)

    def train_classifier(self):
        data_dir= ("data")
        path= [os.path.join(data_dir, f) for f in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #grayscale
            imageNp=np.array(img,'uint8')
            
            s= (os.path.split(image)[-1].split(".")[0])
            d= (s.replace('user_',''))
            id= int(d)

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13 
        ids=np.array(ids)

        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result","Training Data Sets completed", parent=self.root)





if __name__ == "__main__":
    ro=Tk()
    obj=Train(ro)
    ro.mainloop()