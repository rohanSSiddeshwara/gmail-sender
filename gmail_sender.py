from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import math
import smtplib
import tkinter.scrolledtext as st

root=Tk()
root.title("Email Sender")
root.configure(bg="#048d91")
root.geometry("320x400")

label=Label(root,text='WELCOME',bg='#048d91',fg='black')
label.place(x=137,y=50)

username_l=Label(root,text='Email: ',bg='#048d91',fg='black')
username_l.place(x=77,y=117)
password_l=Label(root,text='Password: ',bg='#048d91',fg='black')
password_l.place(x=77,y=177)

username_i=Entry(root,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
username_i.place(x=77,y=140)
password_i=Entry(root,width=30,bg='black',fg='#0bab05',relief='groove',borderwidth=0,show="*")
password_i.place(x=77,y=200)

def logout_pressed(s):
    s.quit()
    root.destroy()

def send_pressed(s,sendto_e,email_add,subject_e,body):
    rep_e=sendto_e.get()
    subj=subject_e.get()
    message=body.get('1.0',END)
    if '@gmail.com' not in rep_e or rep_e =='':
        messagebox.showerror("sendind mail.error","Enter a valid email address")
    elif message=='':
        messagebox.showerror("sending mail error","message should't be empty")
    else:
        s.sendmail(email_add,rep_e,f"Subject : {subj}\n\n {message}")
        messagebox.showinfo('Success',"Your Message has been send successfully")
    sendto_e.delete(0,END)
    body.delete('1.0',END)
    subject_e.delete(0,END)




def submit_pressed():
    email_add=username_i.get()
    password=password_i.get()
    if '@gmail.com' not in email_add or email_add=='':
        messagebox.showerror("enter a valid username")
    elif password=='':
        messagebox.showerror("Password should't be empty")
    else:
        try:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login(email_add,password)
            messagebox.showinfo('sucess',"login sucessful..")
            root.geometry("400x400")
            C = Canvas(root, bg="#048d91", height=400, width=400,relief='groove',borderwidth=0)
            C.place(x=-1,y=-1)
            logout_b =Button(root,text='logout',command=lambda:logout_pressed(s),bg='#e60505',fg='black',relief='groove',borderwidth=0)
            logout_b.place(x=350,y=5)
            label1=Label(root,text='Send to :',bg='#048d91',fg='black').place(x=30,y=30)
            sendto_e=Entry(root,width=50,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
            sendto_e.place(x=30,y=60)
            label2=Label(root,text='Subject :',bg='#048d91',fg='black').place(x=30,y=90)
            subject_e=Entry(root,width=50,bg='black',fg='#0bab05',relief='groove',borderwidth=0)
            subject_e.place(x=30,y=120)
            label3=Label(root,text="Message :",bg='#048d91',fg='black').place(x=30,y=150)
            body=st.ScrolledText(root,width=35,height=7,borderwidth=3,bg='black',fg='#0bab05')
            body.place(x=30,y=180)
            send_b=Button(root,text='Send',command=lambda:send_pressed(s,sendto_e,email_add,subject_e,body),bg='#3605e6',fg='black',relief='groove',borderwidth=0)
            send_b.place(x=350,y=360)
        except Exception as e:
            messagebox.showerror('Login error',"either email address or password is wrong")

submit_b=Button(root,text='Submit',bg='#ff6f00',fg='black',command=submit_pressed,relief='groove',borderwidth=0)
submit_b.place(x=137,y=280)

root.mainloop()
