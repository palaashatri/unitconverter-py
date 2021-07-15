import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk
from src import area, digital, length, temperature, weight
       
root = Tk()
root.title('Unit Converter')
root.geometry("600x400+100+200")
labelfont = ('ariel', 56, 'bold')
l=Label(root,text='Unit Converter SDLC Team 23',font = ("Arial", 20, "bold"), justify = CENTER)
l.place(x=80,y=20)

widget = Button(None, text="EXIT", bg="white", fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "red", activeforeground="green", command=root.destroy).place(x=250,y=350)
   

def color_config(widget, color, event):
    widget.configure(foreground=color)

widget = Button(root, text="Temperature converter", bg="white" , fg="green",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=temperature.TemperatureConverter).place(x=300,y=60)
widget = Button(root, text="Length Converter", bg="white" , fg="orange",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=length.LengthConverter).place(x=50,y=120)
widget = Button(root, text="Area Converter", bg="white" , fg="yellow",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=area.AreaConverter).place(x=300,y=120)
widget = Button(root, text="Digital converter", bg="white" , fg="blue",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=digital.DigitalConverter).place(x=50,y=60)
widget = Button(root, text="Weight Converter", bg="white" , fg="black",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=weight.WeightConverter).place(x=180,y=180)

root.mainloop()
