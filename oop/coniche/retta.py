class retta:
    def __init__(self, tipo = None, p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo == "input_abc"):
    
            self.__a = int(p1)
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []
            self.__m = -int(p1) / int(p2)

        elif(tipo == "input_2punti"):
            # inserire la procedura per ricavare a, b, c a partire da due punti.
            #p1=x1 p2=y1 p3=x2 p4=y2
            self.__a = p4 - p2
            self.__b = - (p3 - p1)
            self.__c = - p1 * (p4-p2) + p2 * (p3 - p1)
            self.__punti = []
            self.__m = (p4 - p2)/(p3-p1)
               
        elif(tipo == "input_coefficiente"):
            # inserire la procedura per ricavare a, b, e c a partire dal coefficiente angolare ed un punto. 
            #p1=coefficiente p2=x p3=y
            self.__a = -p1
            self.__b = 1
            self.__c = p1 * p2 - p3
            self.__punti = []
            self.__m = p1
 
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def eqEsplicita(self):
        if self.__b == 0:
            return f"\n\n equazione forma esplicita: \n x = {- self.__c/ self.__a} \n (y= 0) \n\n ---------------------------"
        elif self.__a == 0:
            return f"\n\n equazione forma esplicita: \n y = {- self.__c/ self.__b} \n (x= 0) \n\n ---------------------------"
        else:
            return f"\n\n equazione forma esplicita: \n y = {- self.__a / self.__b}x + {- self.__c/ self.__b} \n\n ---------------------------"

    def eqImplicita(self):
        if self.__b == 0:
            return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x + {self.__c} = 0 \n (y= 0) "
        elif self.__a == 0:
            return f"---------------------------\n\n equazione forma implicita: \n {self.__b}y + {self.__c} = 0 \n (x= 0) "
        else:
            return f"---------------------------\n\n equazione forma implicita: \n {self.__a}x + {self.__b}y + {self.__c} = 0 "

    def trovaY(self, x):
        if self.__b == 0:
            return f"\n\n equazione forma esplicita: \n x = {- self.__c/ self.__a} \n (y= 0) \n\n ---------------------------"
        elif self.__a == 0:
            return f"\n\n equazione forma esplicita: \n y = {- self.__c/ self.__b} \n (x= 0) \n\n ---------------------------"
        else:
            return f"\n\n equazione forma esplicita: \n y = {- self.__a / self.__b}x + {- self.__c/ self.__b} \n\n ---------------------------"

    def punti(self):

        inizio = - (1/2) * int(n)
        fine = (1/2) * int(n)

        if self.__a == 0:
            for i in range(int(inizio), int(fine)):
                x = i
            self.__punti.append((x, - self.__c/ self.__b))
        
        elif self.__b == 0:
            for i in range(int(inizio), int(fine)):
                y = i
            self.__punti.append((- self.__c/ self.__a, y))

        else:    
            for i in range(int(inizio), int(fine)):
                x = i
                self.__punti.append ((x, (- self.__a * x - self.__c) / self.__b))
        
        print(self.__punti)

    def m(self):
        if self.__b == 0:
            return f"\ncoefficiente angolare: \n\n la retta è parallela all'asse delle y, il coefficiente angolare non è definito in alcun modo... \n\n ---------------------------"
        else:
            return f"\ncoefficiente angolare: \n\n m= {self.__m} \n\n ---------------------------"

    def intersezione(self, s):
        '''
        acquisita una retta s in input, questo metodo deve restituire il punto in comune 
        (sottoforma di tupla), verificandone l'esistenza. Restituire "null" se le rette sono 
        in parallelo oppure la lista __punti() se le rette dovessero coincidere. 
        '''
        return 0

tipo_valori = int(input("\n\nche tipi di valore stai dando? \n\n1) a, b, c\n2) due punti appartenenti alla retta\n3) coefficiente angolare ed un punto appartenente alla retta \n\ndigitare 1, 2 o 3 a seconda della risposta..."))

n = (input("quante coppie di ordinate vuoi ricavare?..."))

if tipo_valori == 1:
    retta1 = retta("input_abc", input("\ninserire valore a..."), input("inserire valore b..."), input("inserire valore c..."))

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    print(retta.punti(retta1))

elif tipo_valori == 2:
    retta1 = retta("input_2punti", int(input("inserie x del primo punto...")), int(input("inserie y del primo punto...")), int(input("inserie x del secondo punto...")), int(input("inserie y del secondo punto...")))  

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    print(retta.punti(retta1))


elif tipo_valori == 3:
    retta1 = retta("input_coefficiente", int(input("inserie il valore del coefficiente angolare...")), int(input("inserie x del un punto...")), int(input("inserie y del un punto...")))

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    print(retta.punti(retta1))



            
