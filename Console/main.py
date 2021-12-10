import keyboard as a
import time
import webbrowser as browser

num_loop=True

while num_loop:
    number = str(input("Enter the mobile number with country code: "))
    try:
        raw_n=number
        raw_n=raw_n.replace(" ","")
        if raw_n[0]=="+":
            raw_n=raw_n.replace("+","")
        else:
            print("Enter a your mobile number along with country code.\n E.g. +91 for India, +92 for Pakistan, +880 for Bangladesh")
            num_loop=True
            raise ValueError
        number = int(raw_n)
        num_loop=False

    except:
        num_loop=True
        print("Enter a valid mobile number")
mes_loop=True       
while mes_loop:
    message = str(input("\nEnter the message you want to send continuously: "))
    if len(message)>0:
        mes_loop=False
    else:
        print("Message can't be empty")

c_loop = True
n=0
while c_loop:
    count=input("\nHow many times you want to send? : ")
    if len(count)==0:
        print("Count can't be enpty")
    else:
        try:
            count = int(count)
            if count<=0:
                print("Count can't be negative or zero")
            else:
                c_loop=False
        except ValueError:
            print("\nOops!\nIt seems you have entered a text, please enter a number")
print("\nWhatsapp web will open in 5 seconds")
time.sleep(5)
link = "https://web.whatsapp.com/send?phone="+number
browser.open(link)
print("Message(s) will start sending in 25 seconds with 0.5 second delay between each message")

time.sleep(25)
while n<count:
    a.write(message)
    a.press("enter")
    time.sleep(0.5)
    n+=1
    print(n, " sent")
input("Process completed, press enter to exit")