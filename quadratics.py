#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 22:42:25 2020

@author: isa
"""
import tkinter as tk
from tkinter import IntVar


def mainwindow():    
    mainwindow = tk.Tk()
    mainwindow.title('Enter values')
    mainwindow.geometry('160x110')
    mainwindow.config(bg='#aaf0d1')
    
    tk.Label(mainwindow, text = 'Enter a', font = ('verdana'),  bg='#aaf0d1').grid(row=0)
    tk.Label(mainwindow, text = 'Enter b', font = ('verdana'),  bg='#aaf0d1').grid(row=1)
    tk.Label(mainwindow, text = 'Enter c', font = ('verdana'),  bg='#aaf0d1').grid(row=2)

    getA = IntVar()
    aBox = tk.Entry(mainwindow, textvariable = getA, width=3,  bg='#aaf0d1')
    aBox.grid(row=0, column=1)
    aBox.config(highlightbackground='#aaf0d1')                

    getB = IntVar()
    bBox = tk.Entry(mainwindow, textvariable = getB, width=3,  bg='#aaf0d1')
    bBox.grid(row=1, column=1)
    bBox.config(highlightbackground='#aaf0d1')
    
    getC = IntVar()
    cBox = tk.Entry(mainwindow, textvariable = getC, width=3,  bg='#aaf0d1')
    cBox.grid(row=2, column=1)
    cBox.config(highlightbackground='#aaf0d1')
                    
                    
                    
    button = tk.Button(mainwindow, text='Obtain roots', command = lambda: valueget(), font = ('verdana'), highlightbackground='#aaf0d1')
    button.grid(row=4)
    button.config(bg='#aaf0d1')
    
    def valueget():    
    
        readA = getA.get()
        readB = getB.get()
        readC = getC.get()
        
        
        intA = int(readA)
        intB = int(readB)
        intC = int(readC)
    
        negroot = (readB**2)-(4*readA*readC)
    
        quadformulaplus = (-readB + (pow(negroot,0.5)))/(2*readA) #quad forumla
        quadformulaminus = (-readB - (pow(negroot,0.5)))/(2*readA) #quad forumla
        
        
        
        messagewindow = tk.Toplevel()
        messagewindow.geometry('290x50')
        messagewindow.title('Roots of the equation')
        messagewindow.config(bg='#aaf0d1')

                  
        label = tk.Label(messagewindow, text = f'The roots are {quadformulaplus:.1f} and {quadformulaminus:.1f}', bg='#aaf0d1', font = ('verdana'))
        label.grid(row=1)
        closebutton = tk.Button(messagewindow, text='Close', command = lambda: messagewindow.destroy(), font = ('verdana'), highlightbackground='#aaf0d1')
        closebutton.grid(row=2)
        closebutton.config(bg='#aaf0d1')
        messagewindow.mainloop()
                           

       # print(f'the roots are {quadformulaplus:.1f} and {quadformulaminus:.1f}')
    mainwindow.mainloop()


def startup():
    startpage = tk.Tk()
    startpage.title('Solver')
    #startpage.iconphoto(False, tk.PhotoImage(file='/Users/isa/Desktop/DiffEqns/icon.png'))
    photo = tk.PhotoImage(file = r"/Users/isa/Desktop/DiffEqns/cover.png")  #image load
    coverbutton = tk.Button(startpage, image = photo, command = lambda: [startpage.destroy(), mainwindow()])
    coverbutton.pack()
    coverbutton.configure(highlightbackground='#aaf0d1')

    
    startpage.mainloop()
startup()







