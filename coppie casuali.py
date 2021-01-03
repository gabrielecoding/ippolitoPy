
from random import randint

f = open("dati4.txt", 'w')

dati = ""

for riga in range(100):

    for elemento in range(1):

        dati = dati + str(randint(1,1000)) + "," + str(randint(1,1000))
    
    dati = dati + "\n"

print(dati)

f.write(dati)

f.close()


import string
import numpy as np
import matplotlib.pyplot as plt

f = open("dati4.txt", 'r')

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

plt.scatter(coordX,coordY)
plt.ylabel('coppie casuali di numeri')
plt.show()