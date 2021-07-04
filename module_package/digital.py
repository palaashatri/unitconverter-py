#import index
import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk
from . import convert_digital


def DigitalConverter():
    factors = {'PB': 8000000000000000, 'TB': 8000000000000, 'GB': 8000000000, 'MB' : 8000000, 'kB' : 8000, 'bit' : 1, 'byte' : 0.125}
    ids = {"petabyte": 'PB', "terabyte": 'TB', "gigabyte" : 'GB', "Megabyte" : 'MB', "Kilobyte" : 'kB', "bit" : 'bit', "byte" : 'byte'}
   
    

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert_digital.convert(amt, frm, to))

    
    root = Toplevel()
    root.title("Digital Converter")

    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Digital Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    
    in_select = OptionMenu(mainframe, in_unit, "bit", "byte", "Kilobyte", "Megabyte", "gigabyte", "terabyte", "petabyte") .grid(column=3, row=1, sticky=W)

    

    
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "bit", "byte", "Kilobyte", "Megabyte", "gigabyte", "terabyte", "petabyte").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()