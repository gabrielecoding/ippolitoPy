#lavoro di Ippolito Gabriele, Avallone Enrico e Lastrucci Davide

#Il codice serve ad aprire o a generare dei grafici.
#Nel caso si voglia generare un grafico casuale, basterà seguire le istruzioni dell'interfaccia.
#Mentre nel caso si voglia aprire un grafico proprio, bisognerà inserire la directory del file + il nome del file + formato del file

import tkinter as tk
import csv
from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg


def getGraphRoot():

    rispostagrafico = richiesta_grafico.get()
    
    width = 530
    height = 350

    load = Image.open(rispostagrafico)
    load = load.resize((width,height), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    
    img = Label(image=render)
    img.image = render
    
    riquadro.create_window(450, 400, window=img)    
    root.mainloop()
        
def genera_grafico():
    f = open("dati.txt", 'w')
    dati = ""
    for riga in range(100):
        for elemento in range(1):
            dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
        dati = dati + "\n"
    f.write(dati)
    f.close()
    f = open("dati.txt", 'r')
    coordX = []
    coordY = []
    for riga in f:
        valori = str(f.readline())
        Nval = len(valori)
        valori = valori.strip('\n')
        valori = valori.split(',')
        valori = list(valori)
        print(valori)
        coordX.append(int(valori[0]))
        coordY.append(int(valori[1]))
    f.close()
    print(dati)
    print ("X: ",coordX)
    print ("Y: ",coordY)
    coordX.sort()
    coordY.sort()
    print("liste ordinate:")
    print ("X: ",coordX)
    print ("Y: ",coordY)
    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX, coordY)
    plt.show()

root = Tk()
riquadro = tk.Canvas(root, width = 900, height = 600, bg="dark sea green")
riquadro.pack()



scritta=Label(root, text="inserisci la directory del file da aprire", bg= "dark sea green")
riquadro.create_window(450,110, window=scritta)

#button 1 permette all'utente, nel caso non avesse un grafico, di generarlo.
button1 = tk.Button(root, text="genera un grafico", command=genera_grafico, bg= "NavajoWhite2")
riquadro.create_window(55, 15, window=button1)

#button 2 permette all'utente di chiudere tutte le finestre aperte.
button2 = tk.Button(root, text="chiudi scheda", command=root.destroy, bg="NavajoWhite2")
riquadro.create_window(860, 15, window=button2)

#button 3 permette all'utente di caricare un file dal proprio computer.
button3 = tk.Button(root, text="clicca per aprire il file", command=getGraphRoot, bg= "NavajoWhite2")
riquadro.create_window(450, 180, window=button3)

richiesta_grafico = Entry(root)
riquadro.create_window(450, 140, window=richiesta_grafico)


root.mainloop()

