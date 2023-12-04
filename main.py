from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import filedialog
import platform 
import psutil
from weather_gui import WeatherAppGUI
from welcome import init_assistance, speak, get_time, welcome
from pygame import mixer
import os
import webbrowser
from PIL import Image, ImageTk

#start virtual assistance
assistance = init_assistance()

#brightness
import screen_brightness_control as pct


#clock
from time import strftime

#calendar 
from tkcalendar import*

#open google
import pyautogui
import subprocess
import webbrowser as wb
import random


root=Tk()
root.title("mac-soft")
root.geometry("850x500+300+170")
root.resizable(False, False)
root.configure(bg="#292e2e")


#icon
image_icon=PhotoImage(file='Image/icon.png')
root.iconphoto(False, image_icon)

Body=Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(pady=20, padx=20)



#-------------------------------------------------------
LHS=Frame(Body, width=310, height=435, bg="#f4f5f5", highlightbackground = "#adacb1", highlightthickness=1)
LHS.place(x=10, y=10)

#logo
photo=PhotoImage(file="Image/laptop.png").subsample(1, 1)
myimage=Label(LHS, image=photo, background="#f4f5f5")
myimage.place(x=10, y=20)

my_system=platform.uname()

l1=Label(LHS, text=my_system.node, bg="#f4f5f5", font=("Acumin Variable Concept", 13,"bold"), justify="center")
l1.place(x=30, y=250)

l2=Label(LHS, text=f"Version:{my_system.version}", bg="#f4f5f5", font=("Acumin Variable Concept", 8), justify="center")
l2.place(x=30, y=280)

l3=Label(LHS, text=f"System:{my_system.system}", bg="#f4f5f5", font=("Acumin Variable Concept", 9), justify="center")
l3.place(x=30, y=310)

l4=Label(LHS, text=f"Machine:{my_system.machine}", bg="#f4f5f5", font=("Acumin Variable Concept", 9), justify="center")
l4.place(x=30, y=340)

l5=Label(LHS, text=f"Total RAM installed:{round(psutil.virtual_memory().total/1000000000,2)} GB", bg="#f4f5f5", font=("Acumin Variable Concept", 9), justify="center")
l5.place(x=30, y=370)



#-------------------------------------------------------
RHS=Frame(Body, width=470, height=200, bg="#f4f5f5", highlightbackground = "#adacb1", highlightthickness=1)
RHS.place(x=330, y=10)

system=Label(RHS, text="System", font=("Acumin Variable Concept", 13), bg="#f4f5f5")
system.place(x=10, y=10)


##############Battery###############



def none():
    global battery_png
    global battery_label
    
    battery=psutil.sensors_battery()
    percent=battery.percent

    
    lbl.config(text=f'{percent}%')
    lbl_plug.config(text=f'Plug in: {str(battery.power_plugged)}')
    
    if battery_label is None:
        battery_label = Label(RHS, background="#f4f5f5")
        battery_label.place(x=15, y=50)

    battery_label.after(1000, none)
    
    battery_png=PhotoImage(file="Image/percent.png").subsample(3, 3)
    battery_label.config(image=battery_png)
    
def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_usage = []

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_usage.append({
                'Device': partition.device,
                'Total': round(usage.total / (1024 ** 3)),  # Convert to GB
                'Used': round(usage.used / (1024 ** 3)),  # Convert to GB
                'Free': round(usage.free / (1024 ** 3)),  # Convert to GB
                'Percentage': usage.percent
            })
        except PermissionError:
            continue

    return disk_usage



def display_disk_info():
    disk_info = get_disk_usage()

  
    device_label = tk.Label(root, text=f"Device:")
    device_label.place(x=510, y=50)

    total_label = tk.Label(root, text=f"Total:")
    total_label.place(x=510, y=80)

    used_label = tk.Label(root, text=f"Used:")
    used_label.place(x=510 , y=110)

    free_label = tk.Label(root, text=f"Free:")
    free_label.place(x=510, y=140)

    percentage_label = tk.Label(root, text=f"% Used:")
    percentage_label.place(x=510 , y=170)
        
    for idx, info in enumerate(disk_info):
        
        device_label = tk.Label(root, text=f"{info['Device']}", bg="#f4f5f5")
        device_label.place(x=92 * (idx+6.5), y=50)

        total_label = tk.Label(root, text=f"{info['Total']}GB", bg="#f4f5f5")
        total_label.place(x=89.5 * (idx+6.5), y=80)

        used_label = tk.Label(root, text=f"{info['Used']}GB", bg="#f4f5f5")
        used_label.place(x=89.5* (idx+6.5), y=110)

        free_label = tk.Label(root, text=f"{info['Free']}GB", bg="#f4f5f5")
        free_label.place(x=89.5 * (idx+6.5), y=140)

        percentage_label = tk.Label(root, text=f"{info['Percentage']}%", bg="#f4f5f5")
        percentage_label.place(x=89.5* (idx+6.5), y=170)


lbl=Label(RHS, font=("Acumin Variable Concept", 15, 'bold'), bg="#f4f5f5")
lbl.place(x=30, y=120)

lbl_plug=Label(RHS, font=("Acumin Variable Concept", 8), bg="#f4f5f5")
lbl_plug.place(x=20, y=160)


battery_label = None  # Initialize battery_label as None

none()
display_disk_info()

####################################

def weather():
    app1=Toplevel()
    app1.geometry('1000x500+300+200')
    app1.title('Weather app')
    app1.resizable(False, False)
    
    img = Image.open("Image/weather_bg.png") 
    img = img.resize((1000, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    # Đặt hình ảnh làm nền cho cửa sổ
    background_label = Label(app1, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    bottom = tk.PhotoImage(file="Image/bottom.png")
    frame = tk.Label(app1, image=bottom)
    frame.place(x=1, y=370) 

    app1_interface = WeatherAppGUI(app1)
    
    def exit():
        app1.destroy()
    exit_button = Button(app1, text='Exit', command=exit).place(x=860, y=34)
    exit_button.pack()
    
    welcome(assistance)
    
    app1.mainloop()
    

def clock():
    app2=Toplevel()
    app2.geometry("850x110+300+10")
    app2.title("Clock")
    app2.configure(bg="#292e2e")
    app2.resizable(False, False)
    
    #icon
    image_icon=PhotoImage(file="Image/app2.png")
    app2.iconphoto(False, image_icon)
    
    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)
    
    lbl=Label(app2, font=('digital-7',50,'bold'),width=20, bg='#f4f5f5',fg='#292e2e')
    lbl.pack(anchor='center', pady=20)
    
    clock()

    app2.mainloop()



def calendar():
    app3=Toplevel()
    app3.geometry('300x300+-10+10')
    app3.title('Calendar')
    app3.resizable(False, False)
    
    #icon
    image_icon=PhotoImage(file='Image/App3.png')
    app3.iconphoto(False, image_icon)
    
    mycal=Calendar(app3, setmode='day', date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)
    
    app3.mainloop()
    



def game():
    app4=Toplevel()
    app4.geometry('300x500+1170+170')
    app4.title('Ludo')
    app4.configure(bg='#dee2e5')
    app4.resizable(False, False)

    #icon
    image_icon=PhotoImage(file='Image/App4.png')
    app4.iconphoto(False, image_icon)
    
    ludo_image=PhotoImage(file='Image/ludo back.png')
    Label(app4,image=ludo_image).pack()
    
    label=Label(app4,text='',font=('times', 150))
    
    
    def roll():
        dice=['\u2680','\u2681','\u2682','\u2683','\u2684', '\u2685',]
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}', fg='#29292e', font=("Arial", 80))
        label.pack()
        
    btn_image=PhotoImage(file='Image/ludo button.png')
    btn= Button(app4, image=btn_image, bg='#dee2e5',command=roll)
    btn.pack(padx=10,pady=10)
    
    app4.mainloop()
    

def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
    
def crome():
    wb.register('chrome',None)
    wb.open('https://www.google.com/')
    
def youtube():
    wb.register('chrome', None)
    wb.open('https://www.youtube.com/')
    

def music():
    app8=Toplevel()
    app8.title("Music Player")
    app8.geometry("920x670+290+85")
    app8.configure(bg="#0f1a2b")
    app8.resizable(False,False)
    
    mixer.init()
    
    def open_folder():
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END,song)

    def play_song():
        music_name = playlist.get(ACTIVE)
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()
        music.config(text=music_name[0:4])
        
    #icon
    image_icon = PhotoImage(file="Image/logo1.png")
    app8.iconphoto(False,image_icon)

    Top = PhotoImage(file="Image/top.png")
    Label(app8, image= Top, bg="#0f1a2b").pack()

    #logo
    Logo=PhotoImage (file="Image/logo.png")
    Label(app8, image=Logo, bg="#0f1a2b"). place (x=65,y=115)

    #button
    play_button=PhotoImage(file="Image/play.png")
    Button(app8,image=play_button, bg="#0f1a2b",bd=0,command=play_song).place (x=100, y=400)

    stop_button=PhotoImage(file="Image/stop.png")
    Button(app8, image=stop_button, bg="#0f1a2b",bd=0, command=mixer.music.stop).place (x=30, y=500)

    resume_button=PhotoImage(file="Image/resume.png")
    Button (app8, image=resume_button, bg="#0f1a2b",bd=0, command=mixer.music.unpause).place (x=115, y=500)

    pause_button=PhotoImage(file="Image/pause.png")
    Button(app8, image=pause_button, bg="#0f1a2b",bd=0, command=mixer.music.pause).place (x=200, y=500)

    #label
    music=Label(app8,text="",font=("arial", 15),fg="white",bg="#0f1a2b")
    music.place(x=150, y=340, anchor="center")

    #music
    Menu = PhotoImage(file="Image\menu.png")
    Label(app8, image=Menu, bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

    music_frame = Frame(app8,bd= 2,relief=RIDGE)
    music_frame.place(x=330,y=350,width=560,height=250)

    Button(app8,text="Open Folder", width=15, height=2, font=("arial",10,"bold"),fg="white",bg="#21b3de",command=open_folder).place(x=330, y=330)

    scroll = Scrollbar(music_frame)
    playlist = Listbox(music_frame,width=100, font=("arial", 10),bg="#333333",fg="grey",selectbackground="lightblue",
                    cursor="hand2", bd=0, yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT, fill=Y)
    playlist.pack(side=LEFT, fill=BOTH)
    
    
    def exit():
        app8.destroy()
    exit_button = Button(app8, text='Exit', width=13, height=1, command=exit)
    exit_button.place(x=520, y=350)
    
    app8.mainloop()
        
    
def interest():
    app9=Toplevel()
    app9.title("Simple interest calculator")
    app9.geometry("700x300")
    app9.resizable(False,False)

    def Calculate():
        prin = int(principalentry.get())
        rat = float(rateentry.get())
        tim = int(timeentry.get())
        amount = (prin*tim*rat)/100
        Label(app9,text=f"{amount}", font="arial 30 bold").place(x = 280, y =220)


    principal = Label(app9,text = "Principal:", font="arial 15")
    rate = Label(app9,text = "Rate of interest:", font="arial 15")
    time = Label(app9,text = "Time:", font="arial 15")

    principal.place(x = 50, y = 20)
    rate.place(x = 50, y = 90)
    time.place(x = 50, y = 160)

    interest = Label(app9, text = "Interest:", font="arail 15")
    interest.place(x = 50, y =230)

    principalvalue = StringVar()
    ratevalue = StringVar()
    timevalue = StringVar()

    principalentry = Entry(app9, textvariable=principalvalue, font="arial 20", width=8)
    rateentry = Entry(app9, textvariable=ratevalue, font="arial 20", width=8)
    timeentry = Entry(app9, textvariable=timevalue, font="arial 20", width=8)

    principalentry.place(x = 280, y = 20)
    rateentry.place(x = 280, y = 90)
    timeentry.place(x = 280, y = 160)

    Button(app9, text="Calculate", font="arial 15",command=Calculate).place(x = 500, y = 20)
    
    def exit():
        app9.destroy()
    Button(app9, text="Exit", command=exit,font="arial 15",width=8).place(x = 500, y = 90)

    app9.mainloop()
    
    
def currency_converter():
    def open_streamlit_app():
        subprocess.Popen(['streamlit', 'run','currency-converter.py'])
    app10 = Toplevel()
    app10.title("Currency Converter")
    start_button = tk.Button(app10, text="Start Currency Converter App", command=open_streamlit_app)
    start_button.pack()

    app10.mainloop()
    
#-------------------------------------------------------
RHB=Frame(Body, width=470, height=225, bg="#f4f5f5", highlightbackground = "#adacb1", highlightthickness=1)
RHB.place(x=330, y=220)

apps=Label(RHB, text="Apps", font=("Acumin Variable Concept", 13), bg="#f4f5f5")
apps.place(x=10, y=10)

app1_image=PhotoImage(file="Image/App1.png")
app1=Button(RHB,image=app1_image,bd=0,command=weather)
app1.place(x=17, y=62)

app2_image=PhotoImage(file="Image/App2.png")
app2=Button(RHB,image=app2_image,bd=0, command=clock)
app2.place(x=109, y=62)

app3_image=PhotoImage(file="Image/App3.png")
app3=Button(RHB,image=app3_image,bd=0, command=calendar)
app3.place(x=205, y=63)

app4_image=PhotoImage(file="Image/App4.png").subsample(6, 6)
app4=Button(RHB,image=app4_image,bd=0,command=game)
app4.place(x=290, y=50)

app5_image=PhotoImage(file="Image/App5.png")
app5=Button(RHB,image=app5_image,bd=0, command=file)
app5.place(x=15, y=140)

app6_image=PhotoImage(file="Image/App6.png")
app6=Button(RHB,image=app6_image,bd=0, command=crome)
app6.place(x=110, y=145)

app7_image=PhotoImage(file="Image/App7.png").subsample(3, 3)
app7=Button(RHB,image=app7_image,bd=0, command=youtube)
app7.place(x=195, y=135)

app8_image=PhotoImage(file="Image/App8.png").subsample(3, 3)
app8=Button(RHB,image=app8_image,bd=0, command=music)
app8.place(x=280, y=142)

app9_image=PhotoImage(file="Image/App9.png").subsample(4, 4)
app9=Button(RHB,image=app9_image,bd=0, command=interest)
app9.place(x=390, y=145)

app10_image=PhotoImage(file="Image/App10.png").subsample(4, 4)
app10=Button(RHB,image=app10_image,bd=0,command=currency_converter)
app10.place(x=390, y=63)

root.mainloop()