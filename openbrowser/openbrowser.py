from io import FileIO
import tkinter
import webbrowser
from tkinter import *
import os
import sys
from tkinter import filedialog

root = Tk( )
pyexec = sys.executable

root.title('Abrir o Browser')
root.geometry('300x200')

def mobsystem():
    #root.filename = filedialog.askopenfilename (initialdir = "/" , title = "Selecionar arquivo" , filetypes = (( "arquivos jpeg" , "* .jpg" ), ( "todos os arquivos" , "* . * " )))
    #root.filename = filedialog.askopenfilename (initialdir = "C:/Users/Agnaldo/Desktop/ImobSystem - Sistema Imobiliário.appref-ms")
    #open('C:/Users/Agnaldo/Desktop/ImobSystem - Sistema Imobiliário.appref-ms')
    PathPy = tkinter.filedialog.askdirectory(initialdir="Sistema Imobiliário",filetypes=[('C:/Users/Agnaldo/Desktop/ImobSystem','.appref-ms')])
    os.system('%s %s' % (pyexec, PathPy))

def google():
    webbrowser.open('www.google.com.br')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
mymobsystem = Button(root, text='Abrir o sistema imob', command=mobsystem).pack(pady=20)
root.mainloop()
