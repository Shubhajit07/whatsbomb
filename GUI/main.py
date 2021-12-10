from tkinter import *
from tkinter import messagebox
import keyboard as a
import time
import webbrowser as browser

err=False
def get_num():
    try:
        raw_n=number.get()
        raw_n=raw_n.replace(" ","")
        if raw_n[0]=="+":
            raw_n=raw_n.replace("+","")
        else:
            messagebox.showerror("Error", "Enter a your mobile number along with country code.\n E.g. +91 for India, +92 for Pakistan, +880 for Bangladesh")
            global err
            err=True
            raise ValueError
        global phone
        phone = int(raw_n)

    except:
        err=True
        messagebox.showerror("Error", "Enter a valid mobile number")

def get_mes():
    global mes
    mes=message.get()
    if len(mes)==0:
        messagebox.showerror("Error", "Message can't be empty")
        global err
        err=True
        raise ValueError

def get_cou():
    try:
        global cou
        cou = count.get()
        if len(cou)==0:
            messagebox.showerror("Error", "Message count cant be empty")
            raise ValueError
        if cou<= 0:
            messagebox.showerror("Error", "Message count cant be zero")
            global err
            err=True
            raise ValueError
            
    except:
        err=True
        messagebox.showerror("Error", "Message count must be a number")

def btn_clicked():
    try:
        get_num()
        get_mes()
        get_cou()
        if err==False:
            
            messagebox.showwarning("Notice","Whatsapp web will open in 5 seconds")
            n=0
            time.sleep(5)
            link = "https://web.whatsapp.com/send?phone="+str(phone)
            browser.open(link)
            messagebox.showwarning("Notice","Message(s) will start sending in 25 seconds with 0.5 second delay between each message")

            time.sleep(25)
            while n<cou:
                a.write(mes)
                a.press("enter")
                time.sleep(0.5)
                n+=1
                print(n, " sent")
            messagebox.showinfo("Success", "Process completed")
    except:
        messagebox.showerror("Error", "Something Went Wrong")

window = Tk()
window.wm_title("Whatsapp Bomber")
icon=PhotoImage(file="icon.png")
window.iconphoto(False,icon)
window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "images/background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

number_img = PhotoImage(file = "images/textBox.png")
number_bg = canvas.create_image(
    500.0, 213.0,
    image = number_img)

number = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

number.place(
    x = 341.0, y = 189,
    width = 318.0,
    height = 46)

message_img = PhotoImage(file = "images/textBox.png")
message_bg = canvas.create_image(
    500.0, 313.0,
    image = message_img)

message = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

message.place(
    x = 341.0, y = 289,
    width = 318.0,
    height = 46)

count_img = PhotoImage(file = "images/textBox.png")
count_bg = canvas.create_image(
    500.0, 413.0,
    image = count_img)

count = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

count.place(
    x = 341.0, y = 389,
    width = 318.0,
    height = 46)

Button_Img = PhotoImage(file = "images/Button_Img.png")

b0 = Button(
    image = Button_Img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 466, y = 470,
    width = 68,
    height = 48)

window.resizable(False, False)
window.mainloop()