# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Importing the required modules
import tkinter
from PIL import Image, ImageTk
import random

# from PIL.ImageTk import PhotoImage

# Creating a top-level widget to make the main window of out application
mainwindow = tkinter.Tk()
mainwindow.geometry('800x600')
mainwindow.title('Dice Rolling Simulator')

# Adding labels to our mainwindow of different fonts and fontsize
# Label1 is heading label
label1 = tkinter.Label(mainwindow, text='DICE ROLLING SIMULATOR', fg='black', font="Times 20 bold", bg='red')
label1.pack(side='top')

# labelnew is bottom label
labelnew = tkinter.Label(mainwindow, text="ROLL! ROLL! ROLL!", fg='blue', font="Times 20 bold italic", bg='red')
labelnew.pack(side='bottom')
# label2 is blankline label
label2 = tkinter.Label(mainwindow, text="")
label2.pack()
# Images of dice
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']

# simulating the device with random numbers between 0 and 6 and generating images
images = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# creating a label widget of our image
label3 = tkinter.Label(mainwindow, image=images)
label3.image = images
# packing image label to our main window
label3.pack(expand=True)


# Dice roller function
def dice_roller():
    ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label3.configure(image=images)
    label3.image = images


# Creating button
button = tkinter.Button(mainwindow, text='ROLL', fg='red', command=dice_roller)
button.pack(expand=True)

mainwindow.mainloop()
