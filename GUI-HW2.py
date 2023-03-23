import tkinter as tk
from tkinter import ttk #theme of tk
from tkinter import messagebox
import datetime
##################################################
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw= csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist=['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr=csv.reader(file) #fr=file reader
        data=list(fr)
    return data
#############################################

# Create the main window
window = tk.Tk()
window.title("My Diary")
window.geometry("500x400")

# Create Label
L1 = tk.Label(window,text='Today is:')
L1.place(x=170,y=100)
L2 = tk.Label(window,text='My Diary',font=('Angsana New',30),fg='pink')
L2.place(x=200,y=30)

# Get today's date
today = datetime.date.today()
date_label = tk.Label(window,text=str(today))
date_label.place(x=250,y=100)

# Create an input inbox
input_box = ttk.Entry(window)
input_box.place(x=180,y=250)

#Save data
def SaveData():
    data = input_box.get()
    input_box.delete(0,tk.END) #clear info in input box 
    writecsv([data]) #record into csv
    text= 'Congrats! your diary is recorded'
    messagebox.showinfo('Message',text)


def button2_click():
# Create msgbox2
    text= 'No messages recorded. Do you want to record again?'
    answer = messagebox.askyesno('Confirmation',text)
    if answer():
        messagebox.showinfo('Message','Recorded')
    else:
        messagebox.showinfo('Message','Canceled')

# Create a Record Button
button1 = ttk.Button(window, text="Record",command=SaveData)
button1.place(x=170,y=300)

    # Create another button
button2 = ttk.Button(window, text="Cancel",command=button2_click)
button2.place(x=250,y=300)

# Start the event loop
window.mainloop()
