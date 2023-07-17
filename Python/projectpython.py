from tkinter import *
from tkinter import ttk
import datetime #for reading present date
import time
import pywhatkit as pwt
import requests #for retreiving user entered  data from excel sheet
from plyer import notification
a=Tk()
a.title("Notification Application") #Creation of gui window
a.geometry("1000x1000")
a.configure(bg="cyan")

#Labes and Entry widgets to enter the task and time

v1=StringVar()
b=Button(a,text="Enter the task and time",background='yellow',foreground='black',font=("Arial",20),borderwidth=2,bd=5).grid(row=0,column=0)
e=Entry(a,textvariable=v1,font=10,bd=5).grid(row=1,column=0)

l1=Label(a,text="hh",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=2,column=0)
t1=IntVar()
hour=ttk.Combobox(a,width=10,textvariable=t1,font=10)
hour['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
hour.grid(row=3,column=0)
hour.current()

l2=Label(a,text="mm",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=2,column=1)
m1=IntVar()
minutes=ttk.Combobox(a,width=10,textvariable=m1,font=10)
minutes['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
minutes.grid(row=3,column=1)
minutes.current()

l3=Label(a,text="SS",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=2,column=2)
s1=IntVar()
seconds=ttk.Combobox(a,width=10,textvariable=s1,font=10)
seconds['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,81,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
seconds.grid(row=3,column=2)
seconds.current()

v2=StringVar()
e2=Entry(a,textvariable=v2,font=10,bd=5).grid(row=4,column=0)

l4=Label(a,text="hh",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=5,column=0)
t2=IntVar()
hour=ttk.Combobox(a,width=10,textvariable=t2,font=10)
hour['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
hour.grid(row=6,column=0)
hour.current()



l5=Label(a,text="mm",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=5,column=1)
m2=IntVar()
minutes=ttk.Combobox(a,width=10,textvariable=m2,font=10)
minutes['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
minutes.grid(row=6,column=1)
minutes.current()

l6=Label(a,text="SS",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=5,column=2)
s2=IntVar()
seconds=ttk.Combobox(a,width=10,textvariable=s2,font=10)
seconds['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,81,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
seconds.grid(row=6,column=2)
seconds.current()

v3=StringVar()

e3=Entry(a,textvariable=v3,font=10,bd=5).grid(row=8,column=0)

l7=Label(a,text="hh",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=9,column=0)
t3=IntVar()
hour=ttk.Combobox(a,width=10,textvariable=t3,font=10)
hour['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
hour.grid(row=10,column=0)
hour.current()



l8=Label(a,text="mm",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=9,column=1)
m3=IntVar()
minutes=ttk.Combobox(a,width=10,textvariable=m3,font=10)
minutes['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
minutes.grid(row=10,column=1)
minutes.current()

l9=Label(a,text="SS",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=9,column=2)
s3=IntVar()
seconds=ttk.Combobox(a,width=10,textvariable=s3,font=10)
seconds['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,81,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
seconds.grid(row=10,column=2)
seconds.current()

v4=StringVar()

e4=Entry(a,textvariable=v4,font=10,bd=5).grid(row=12,column=0)

l10=Label(a,text="hh",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=13,column=0)
t4=IntVar()
hour=ttk.Combobox(a,width=10,textvariable=t4,font=10)
hour['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
hour.grid(row=14,column=0)
hour.current()



l11=Label(a,text="mm",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=13,column=1)
m4=IntVar()
minutes=ttk.Combobox(a,width=10,textvariable=m4,font=10)
minutes['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
minutes.grid(row=14,column=1)
minutes.current()

l12=Label(a,text="SS",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=13,column=2)
s4=IntVar()
seconds=ttk.Combobox(a,width=10,textvariable=s4,font=10)
seconds['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,81,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
seconds.grid(row=14,column=2)
seconds.current()

v5=StringVar()

e5=Entry(a,textvariable=v5,font=10,bd=5).grid(row=16,column=0)




l14=Label(a,text="hh",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=18,column=0)
t5=IntVar()
hour=ttk.Combobox(a,width=10,textvariable=t5,font=10)
hour['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
hour.grid(row=19,column=0)
hour.current()



l15=Label(a,text="mm",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=18,column=1)
m5=IntVar()
minutes=ttk.Combobox(a,width=10,textvariable=m5,font=10)
minutes['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
minutes.grid(row=19,column=1)
minutes.current()

l9=Label(a,text="SS",background='cyan',foreground='black',font=("Arial",20),borderwidth=2).grid(row=18,column=2)
s5=IntVar()
seconds=ttk.Combobox(a,width=10,textvariable=s5,font=10)
seconds['values']=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,81,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60)
seconds.grid(row=19,column=2)
seconds.current()

#Function to print the notification

def fun():
    y1=t1.get()*60*60+m1.get()*60+s1.get()
    if y1!=0:
        if __name__=="__main__":
            time.sleep(y1)
            notification.notify(
            #title of the notification,
            title = "Desktop Notifier",
            #the body of the notification
            message ="Your task: "+v1.get(),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = None,
            # the notification stays for 50sec
            timeout=3)
        from datetime import datetime
        obj=datetime.now()
        pwt.sendwhatmsg("+919380672711","You have task now :"+v1.get(),obj.hour,obj.minute+1)
    y2=t2.get()*60*60+m2.get()*60+s2.get()
    if y2!=0:
        if __name__=="__main__":
            time.sleep(y2)
            notification.notify(
            #title of the notification,
            title = "Desktop Notifier",
            #the body of the notification
            message ="Your task: "+v2.get(),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = None,
            # the notification stays for 50sec
            timeout=3)
        from datetime import datetime
        obj=datetime.now()
        pwt.sendwhatmsg("+919380672711","You have task now :"+v2.get(),obj.hour,obj.minute+1)
    y3=t3.get()*60*60+m3.get()*60+s3.get()
    if y3!=0:
        if __name__=="__main__":
            time.sleep(y3)
            notification.notify(
            #title of the notification,
            title = "Desktop Notifier",
            #the body of the notification
            message ="Your task: "+v3.get(),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = None,
            # the notification stays for 50sec
            timeout=3)
        from datetime import datetime
        obj=datetime.now()
        pwt.sendwhatmsg("+91PhoneNumber","You have task now :"+v3.get(),obj.hour,obj.minute+1)
    y4=t4.get()*60*60+m4.get()*60+s4.get()
    if y4!=0:
        if __name__=="__main__":
            time.sleep(y4)
            notification.notify(
            #title of the notification,
            title = "Desktop Notifier",
            #the body of the notification
            message ="Your task: "+v4.get(),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = None,
            # the notification stays for 50sec
            timeout=3)
        from datetime import datetime
        obj=datetime.now()
        pwt.sendwhatmsg("+919380672711","You have task now :"+v4.get(),obj.hour,obj.minute+1)
    y5=t5.get()*60*60+m5.get()*60+s5.get()
    if y5!=0:
        if __name__=="__main__":
            time.sleep(y5)
            notification.notify(
            #title of the notification,
            title = "Desktop Notifier",
            #the body of the notification
            message ="Your task: "+v5.get(),  
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = None,
            # the notification stays for 50sec
            timeout=3)
        from datetime import datetime
        obj=datetime.now()
        pwt.sendwhatmsg("+919380672711","You have task now :"+v5.get(),obj.hour,obj.minute+1)

#Button to submit or get notification

b=Button(a,text="submit",background='yellow',foreground='black',font=("Arial",20),borderwidth=2,command=fun,bd=5).grid(row=25,column=1)
a.mainloop()






























                   
