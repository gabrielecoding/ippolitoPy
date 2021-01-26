from tkinter import * 
import numpy as np
import matplotlib.pyplot as plt
from guizero import App, PushButton, Text
import csv
from random import randint
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from pygame.locals import *
import pygame, sys

def genera_grafico():
    root = Tk() 
    root.title('Generatore di grafici')
    root.geometry('400x400') 
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
    def graph():
        plt.scatter(coordX, coordY)
        plt.show()
    c = Button(root,text="premimi per avere il grafico", command=graph)
    c.pack()
    root.mainloop()

def carica_file_csv():
    ro = Tk()
    ro.title("carica file csv")
    riquadro = tk.Canvas(ro, width = 400, height = 400)
    riquadro.pack()

    richiesta_grafico = Entry(ro)
    riquadro.create_window(200, 140, window=richiesta_grafico)

    scritta=Label(ro, text="inserisci il nome del file")
    riquadro.create_window(200,110, window=scritta)

    def file_csv():
        rispostagrafico = richiesta_grafico.get()
    
        with open(rispostagrafico, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

        print("")
        print("")

        with open(rispostagrafico, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                print(dict(row))

    my_button = tk.Button(ro, text="clicca per confermare", command=file_csv)

    riquadro.create_window(200, 180, window=my_button)

    ro.mainloop()

#richiesta_grafico = Entry(root)
#riquadro.create_window(200, 140, window=richiesta_grafico)

#scritta=Label(root, text="inserisci il nome del file")
#riquadro.create_window(200,110, window=scritta)

def getGraphRoot():
    rispostagrafico = input("inserire directory del file...")
    
    pygame.init()
    display_width = (640)
    display_height = (480)
    graph=pygame.image.load(rispostagrafico)
    screen=pygame.display.set_mode((display_width, display_height))
    screen.blit(graph, (1,1))
    pygame.display.update()

app = App(title="Carica grafici", width=250, bg="light cyan", height=200, layout="grid")
button1 = PushButton(app, command=carica_file_csv,  text="clicca qui per caricare un file csv", grid=[400,50])
button2 = PushButton(app, command=getGraphRoot,  text="clicca qui per caricare un grafico", grid=[400,150])
button3 = PushButton(app, command=genera_grafico,  text="clicca qui per generare un grafico", grid=[400,250])
button4 = PushButton(app, command=app.destroy, text="Clicca qui per chiudere la scheda", grid=[400,350])
app.display()



#LAVORO DI: Gabriele Ippolito, Davide Lastrucci, Enrico avallone