from random import randint as rd
import os
import csv

os.chdir(r"C:\Users\ippol\OneDrive\Desktop\Haiku") 

f = open("cinq1.txt")
line = csv.reader(f)
v1 = list(line)

g = open("sette.txt")
line = csv.reader(g)
v2 = list(line)

h = open("cinq2.txt")
line = csv.reader(h)
v3 = list(line)

verso1 = v1[rd(0,5)]
verso2 = v2[rd(0,5)]
verso3 = v3[rd(0,7)]


print(*verso1)
print(*verso2)
print(*verso3)