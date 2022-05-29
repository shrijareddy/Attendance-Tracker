import tkinter as tk
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from time import strftime
from datetime import datetime
import cv2 
import os
import sys 
import csv
import mysql.connector
from pyparsing import dblQuotedString

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("530x330+300+200")
        self.root.title("Attendance")
        
        btn=Button(self.root, text= "Open Camera", command=self.face_recog,font=("Calibri",15,"bold"),bg="white",fg="black",cursor="hand2" )
        btn.place(x=200, y=100, width=150, height=40 )
    
    #mark attendance
    def mark_attendance(self,r,n,d):
        with open("attendance.csv","r+",newline="\n") as fi:
            myDataList= fi.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((r not in name_list) and (n not in name_list) and (d not in name_list)) : 
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                fi.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")
             
            
               
        
    #face recognition
    def face_recog(self):
        
           
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret, img=video_cap.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.3,5)
           
            for(x,y,w,h) in faces :
                id, conf = clf.predict(gray[y:y+h, x:x+w])
                confidence=int((100*(1-conf/300)))
                id=str(id)
                id=id[0]
                
                #fetch data
                conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where roll="+str(id))
                n=my_cursor.fetchone()
                n= " ".join(n)
                
                my_cursor.execute("select roll from student where roll="+str(id))
                r=my_cursor.fetchone()
                r=" ".join(r)
                
                my_cursor.execute("select dep from student where roll="+str(id))
                d=my_cursor.fetchone()
                d=" ".join(d)
           
                
            
                
                if confidence>77:
                    cv2.rectangle(img, (x,y), (x+y, y+h), (0,255,0), 3)
                    cv2.putText(img, f"Name:{n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX,0.8, (255,0,0),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,0,0,),2)
                    cv2.putText(img,f"Department:{d} ",(x,y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,0,0),2)
                    cv2.putText(img," Click Enter to Mark Attendance",(x,y+20),cv2.FONT_HERSHEY_COMPLEX, 0.6,(255,0,0,),2)
                    self.mark_attendance(r,n,d)
                    
           
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown, Click Enter to Exit",(x,y-30),cv2.FONT_HERSHEY_COMPLEX, 0.8,(0,0,255),3)
               

               
                
                
                
            cv2.imshow("Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
    

if __name__ == "__main__":
    ro=Tk()
    obj=Face_Recognition(ro)
    ro.mainloop()