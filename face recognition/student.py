from platform import release
from socket import if_nameindex
from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
from turtle import color
from tkinter import messagebox
from cv2 import COLOR_BAYER_BG2GRAY, COLOR_BAYER_BG2RGB, COLOR_BGR2GRAY, FONT_HERSHEY_COMPLEX, CascadeClassifier, VideoCapture, cvtColor, destroyAllWindows, imshow, imwrite, putText, resize, waitKey
import mysql.connector
import cv2
import numpy as np


import sys 
import csv
import os 
from train import Train


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x660+0+0")
        self.root.title("Register")

        #variables
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()


        #background image
        left_frame=LabelFrame(self.root,bg="white")
        left_frame.place(x=15,y=15,width=560,height=620)

        title=Label(self.root,text="REGISTER ",font=("Calibri Light",20,"bold"),fg="black",bg="white")
        title.place(x=20,y=30,width=200,height=50)

        #name
        name=Label(self.root,text=" Name:",font=("arial",11),bg="white",fg="black")
        name.place(x=60,y=90,height=30,width=50)
        name_entry=ttk.Entry(self.root,textvariable=self.var_name,font=("arial",10),width=17)
        name_entry.place(x=60,y=120,height=30,width=300)

        #rollno
        roll=Label(self.root,bg="white",text="Enrollment No.:  ",font=("arial",11),fg="black")
        roll.place(x=60,y=160,height=35,width=110)
        roll_entry=ttk.Entry(self.root,textvariable=self.var_roll,font=("arial",10),width=17)
        roll_entry.place(x=60,y=190,height=30,width=240)
 
        #course
        course=Label(self.root,bg="white",text="Course: ",font=("arial",11),fg="black")
        course.place(x=60,y=240,height=30,width=60)
 
        cor_combo=ttk.Combobox(self.root,textvariable=self.var_course,font=("arial",10),width=17, state="readonly")
        cor_combo["values"]=("Select","B.E/B.Tech","M.Tech")
        cor_combo.current(0)
        cor_combo.place(x=60,y=270,height=30,width=200)
 
        #department
        dep=Label(self.root,bg="white",text="Department:    ",font=("arial",11),fg="black")
        dep.place(x=300,y=240,height=30,width=100)
 
        dep_combo=ttk.Combobox(self.root,textvariable=self.var_dep, font=("arial",10),width=17, state="readonly")
        dep_combo["values"]=("Select","Computer Science","Information Technology","Electrical Engineering","Mechanical Engineering","Civil Engineering")
        dep_combo.current(0)
        dep_combo.place(x=300,y=270,height=30,width=200)
 
        #year
        year=Label(self.root,bg="white",text="Year:  ",font=("arial",11),fg="black")
        year.place(x=60,y=320,height=30,width=50)
 
        year_combo=ttk.Combobox(self.root,textvariable=self.var_year,font=("arial",10),width=17, state="readonly")
        year_combo["values"]=("Select","2019-23","2020-24","2021-25","2022-26")
        year_combo.current(0)
        year_combo.place(x=60,y=350,height=30,width=150)
 
        #sem
        sem=Label(self.root,text="Semester: ",font=("arial",11),fg="black", bg="white")
        sem.place(x=300,y=320,height=30,width=80)
 
        sem_combo=ttk.Combobox(self.root,textvariable=self.var_sem,font=("arial",10),width=17, state="readonly")
        sem_combo["values"]=("Select","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.place(x=300,y=350,height=30,width=150)

        #email
        email=Label(self.root,bg="white",text="Email ID:",font=("arial",10),fg="black")
        email.place(x=60,y=400,height=30,width=50)
        email_entry=ttk.Entry(self.root,textvariable=self.var_email,font=("arial",10),width=17)
        email_entry.place(x=60,y=430,height=30,width=300)
 
        #photosample radio
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(self.root, text="Take Photo Sample",variable=self.var_radio1,value="yes")
        radio_btn1.place(x=60,y=480,width=200,height=30)
 
        #no photosample
        radio_btn2=ttk.Radiobutton(self.root, text="No Photo Sample",variable=self.var_radio1,value="no") 
        radio_btn2.place(x=320,y=480,width=200,height=30)

        #update
        update=Button(self.root,text="Update",command=self.update_data,font=("arial",10),bg="lavender",fg="black")
        update.place(x=60,y=540,height=30,width=100)

        #delete
        delete=Button(self.root,text="Delete",command=self.delete_data,font=("arial",10),bg="lavender",fg="black")
        delete.place(x=180,y=540,height=30,width=100)

        #reset
        update=Button(self.root,command=self.reset_data,text="Reset",font=("arial",10),bg="lavender",fg="black")
        update.place(x=320,y=540,height=30,width=100)

        #take photo sample
        photo=Button(self.root,command=self.generate_dataset,text="Take Photo Samples",font=("arial",10),bg="SeaGreen4",fg="white")
        photo.place(x=100,y=585,height=30,width=150)

        #Train photo sample
        photo=Button(self.root,command=self.train_datasets,text="Save Photo Samples",font=("arial",10),bg="lavender",fg="black")
        photo.place(x=350,y=585,height=30,width=150)

        #save
        save=Button(self.root,command=self.add_data,text="Save",font=("arial",11),bg="SeaGreen4",fg="white")
        save.place(x=450,y=540,height=30,width=80)

        #right frame
        Right_frame=LabelFrame(self.root,bg="white")
        Right_frame.place(x=590,y=15,width=660,height=620)

        Title=Label(self.root,text="Student Details",font=("Calibri Light",20,"bold"),fg="black",bg="white")
        Title.place(x=600,y=25,width=200,height=50)

        #table
        table_frame=LabelFrame(self.root,bg="white",fg="black")
        table_frame.place(x=595,y=80,width=650,height=550)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","name","roll","year","sem","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Enrollment")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"

        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor) 
        self.fetch_data()
       





    def add_data(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_course.get()=="Select" or self.var_roll.get()=="" or self.var_sem.get()=="Select" or self.var_email.get=="" :
            messagebox.showerror("Error","All Fields are Required", parent= self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","saved successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to: {str(es)} ", parent = self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_name.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_year.set(data[4]),
        self.var_sem.set(data[5]),
        self.var_email.set(data[6]),
        self.var_radio1.set(data[7]),


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_course.get()=="Select" or self.var_roll.get()=="" or self.var_sem.get()=="Select" or self.var_email.get=="" :
            messagebox.showerror("Error","All Fields are Required", parent= self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s, name=%s, year=%s, sem=%s, email=%s, photo=%s where roll=%s",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_roll.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("success","Successfully Updated", parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

            
            
    #delete function
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Enrollment Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete?",parent= self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where roll=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

    #reset function
    def reset_data(self):
                self.var_dep.set("Select")
                self.var_course.set("Select")
                self.var_name.set("")
                self.var_roll.set("")
                self.var_year.set("Select")
                self.var_sem.set("Select")
                self.var_email.set("")
                self.var_radio1.get( )

   #generating data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select" or self.var_name.get()=="" or self.var_course.get()=="Select" or self.var_roll.get()=="" or self.var_sem.get()=="Select" or self.var_email.get=="" :
            messagebox.showerror("Error","All Fields are Required", parent= self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="sr",password="1234",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s, course=%s, name=%s, year=%s, sem=%s, email=%s, photo=%s where roll=%s ",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_radio1.get(),
                                                                                        self.var_roll.get(),
                ))
                                                                                     
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            

                #load predefined data on face frontals from opencv
                (width, height) =(450,450)
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  

                cap =cv2.VideoCapture(0)
                 
                
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    gray=cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(my_frame, (x,y), (x+w, y+h), (255,0,0),2)
                        face = gray[y:y+h, x:x+w]
                        face_resize= cv2.resize(face, (width, height))
                        file_name_path="data/user_{}_{}.png".format(id,img_id)                                                           
                        cv2.imwrite(file_name_path, face_resize)

                    
                    img_id+=1

                
                    cv2.imshow("Cropped Face",my_frame)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo ("result","generating data sets completed", parent=self.root)

            except Exception as es:
                messagebox.showerror("error",f"due to: {str(es)} ", parent = self.root)

    def train_datasets(self):  
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

if __name__ == "__main__":
    ro=Tk()
    obj=Student(ro)
    ro.mainloop()
