from random import randint
nome = input("come vuoi chiamare il nuovo file?...") 
print("creazione del file:",nome)
f = open("nome.txt", 'w')

dati = ""

for riga in range(100):

    for elemento in range(1):

        dati = dati + str(randint(1,1000)) + "," + str(randint(1,1000))
    
    dati = dati + "\n"

print(dati)

f.write(dati)

f.close()

from tkinter import *
import string
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


f = open("nome.txt", 'r')

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

print ("X: ",coordX)
print ("Y: ",coordY)

coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)

print(type(coordX))
print(type(coordY))








root = Tk()
riquadro = tk.Canvas(root, width = 400, height = 400)
riquadro.pack()

richiesta_grafico = Entry(root)
riquadro.create_window(200, 140, window=richiesta_grafico)

scritta=Label(root, text="enter the name of the file")
riquadro.create_window(200,110, window=scritta)




def getGraphRoot():
    rispostagrafico = richiesta_grafico.get()
    
    if rispostagrafico == nome:
        plt.scatter(coordX,coordY)
        plt.ylabel(nome)
        plt.show()
    else:
        scritta_errore = tk.Label(root, text= "nome file errato" )
        riquadro.create_window(200, 230, window=scritta_errore)


#immagine = PhotoImage(root, plt.scatter)

my_button = tk.Button(root, text="clicca per confermare", command=getGraphRoot)

riquadro.create_window(200, 180, window=my_button)

root.mainloop()