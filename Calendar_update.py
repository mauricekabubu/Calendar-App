# import the necessary modules & libraries:Tkinter,calendar
import tkinter as tk
from tkinter.constants import CENTER
import calendar
import sqlite3

conn = sqlite3.Connection('database.db')

# creating a function to update the calendar to functionality
def update_calendar():
    root = tk.Tk()
    root.config(bg='light green')
    root.geometry('800x800')
    root.title(f'{entry0.get()} Calendar...')
    # creating the label to display the full calendar
    year_call = int(entry0.get())
    cal = calendar.calendar(year_call)
    lab0 = tk.Label(root,text=cal,bg='light green',fg='black',
                    font=('arial bold',10))
    lab0.pack(anchor=CENTER)

    root.mainloop()

if __name__ == '__main__':
    # creating the interface:geometry,configuration and title
    win = tk.Tk()
    win.title('Calendar App')
    win.config(bg='light grey')
    win.geometry('600x300')
    # creating the labels
    label0 = tk.Label(win,text='Calendar App',bg='light grey',fg='blue',
                   font=('britannic bold',35))
    label0.pack(pady=0,anchor=CENTER)
    label1 = tk.Label(win,text='Enter year:',bg='light grey',fg='green',
                      font=('britannic bold',20))
    label1.place(x=200,y=80)
    entry0 = tk.Entry(win,bg='cyan',width=50,bd=0)
    entry0.place(x=120,y=120)
    button0 = tk.Button(win,text='Check',bg='light green',fg='black',
                        font=('britannic bold',15),width=20,bd=0,command=lambda :update_calendar())
    button0.place(x=160,y=160)


    win.mainloop()