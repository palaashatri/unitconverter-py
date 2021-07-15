import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk
from . import convert_temp


def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()
        kelTemp = kelTempVar.get()

        if celTempVar.get() != 0.0:
            fahTempVar.set(convert_temp.convert_celToFah(celTemp))
            kelTempVar.set(convert_temp.covert_celToKel(celTemp))

        elif fahTempVar.get() != 0.0:
            celTempVar.set(convert_temp.convert_fahToCel(fahTemp))
            kelTempVar.set(convert_temp.convert_fahToKel(fahTemp))
        
        elif kelTempVar.get() !=0.0:
            celTempVar.set(convert_temp.convert_kelToCel(kelTemp))
            fahTempVar.set(convert_temp.convert_kelTofah(kelTemp))
            

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text = "Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row = 0, padx = 5, pady = 5)
        button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0))
        kelTempVar.set(int(0))
        
    top = Toplevel()
    top.title("Temperature Converter")
  
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    kelTempVar = IntVar()
    kelTempVar.set(int(0))
    titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
   

    celLabel = Label (top, text = "Celcius: ", font = ("Arial", 16), fg = "red")
    celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
    fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)
    
    kelLabel = Label (top, text = "Kelvin: ", font = ("Arial", 16), fg = "black")
    kelLabel.grid(row = 4, column = 1, pady = 10, sticky = NW)

    celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


    fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
    fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )
    
    kelEntry = Entry (top, width = 10, bd = 5, textvariable = kelTempVar)
    kelEntry.grid(row = 4, column = 1, pady = 10, sticky = NW, padx = 125 )

    convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = convert)
    convertButton.grid(row = 5, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

    resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
    resetButton.grid(row = 5, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)