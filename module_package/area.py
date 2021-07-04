import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk
from . import convert_area

def AreaConverter():
    factors = {'sqm':1,'sqkm':1000000,'sqr':1011.7141056,'sqcm':0.0001,'sqf':0.09290304 ,
                    'sqin':0.00064516, 'sqmile':2589988.110336, 'mm':0.000001,'sqrod':25.29285264,
                    'sqyard':0.83612736, 'sqtownship':93239571.9721, 'sqacre':4046.8564224 ,'sqare': 100,
                    'sqbarn':1e-28, 'sqhectare':10000, 'sqhomestead':647497.027584}
    ids = {"square meter" : 'sqm', "square km" : 'sqkm', "square rood" : 'sqr', "square cm" : 'sqcm', "square foot" : 'sqf', "square inch" : 'sqin', "square mile" : 'sqmile', "square milimeter" : 'mm', "square rod" : 'sqrod', "square yard": 'sqyard', "square township": 'sqtownship',"square acre": 'sqacre',"square are": 'sqare',"square barn": 'sqbarn',"square hectare": 'sqhectare',"square homestead": 'sqhomestead'}

   
    

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
            out_amt.set(convert_area.convert(amt, frm, to))

   
    root = Toplevel()
    root.title("Area Converter")

    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Area Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

   
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    
    in_select = OptionMenu(mainframe, in_unit, "square meter", "square km", "square rood", "square cm", "square foot", "square inch", "square mile", "square milimeter", "square rod","square yard", "square township","square acre","square are","square barn", "square hectare","square homestead").grid(column=3, row=1, sticky=W)

    

    
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "square meter", "square km", "square rood", "square cm", "square foot", "square inch", "square mile", "square milimeter", "square rod","square yard", "square township","square acre","square are","square barn", "square hectare","square homestead").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()