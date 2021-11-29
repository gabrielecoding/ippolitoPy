


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

    def getM(self):
        return self.__m

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

    def trovaY(self, i):

        if self.__a == 0:
            return - self.__c/ self.__b
        
        elif self.__b == 0:
            return - self.__c/ self.__a

        else:
            return (- self.__a * i - self.__c) / self.__b
        

    def punti(self):
        n = int((input("\n\n quante coppie di ordinate vuoi ricavare?...")))

        if self.__b == 0:
            #i = y
            for i in range(0, n):
                self.__punti.append((retta.trovaY(retta1, i), i))

        else:    
            for i in range(0, n):
                #i= x
                self.__punti.append ((i, retta.trovaY(retta1, i)))
        
        print("\n\n", self.__punti)


    def m(self):
        if self.__b == 0:
            return f"\ncoefficiente angolare: \n\n la retta è parallela all'asse delle y, il coefficiente angolare non è definito in alcun modo... \n\n ---------------------------"
        else:
            return f"\ncoefficiente angolare: \n\n m= {self.__m} \n\n ---------------------------"


    def intersezione(cls, retta1, retta2):

        if (retta.getA(retta1), retta.getB(retta1), retta.getC(retta1)) == (retta.getA(retta2), retta.getB(retta2), retta.getC(retta2)):
            return "Le due rette sono coincidenti"
        elif float(retta.getM(retta1)) == float(retta.getM(retta2)):
            return "\n\nle due rette sono parallele non coincidenti"
        else:
            d = (retta.getA(retta1) * retta.getB(retta2)) - (retta.getA(retta2) * retta.getB(retta1))
            d_x = (retta.getC(retta1) * retta.getB(retta2)) - (retta.getC(retta2) * retta.getB(retta1))
            d_y = (retta.getA(retta1) * retta.getC(retta2)) - (retta.getA(retta2) * retta.getC(retta1))
            return f" x= {d_x / d} y= {d_y / d}"


tipo_valori = int(input("\n\nche tipi di valore stai dando? \n\n1) a, b, c\n2) due punti appartenenti alla retta\n3) coefficiente angolare ed un punto appartenente alla retta \n\ndigitare 1, 2 o 3 a seconda della risposta..."))


intersezione = (input("vuoi ricavare il punto di intersezione con un'altra retta?..."))

if tipo_valori == 1:
    retta1 = retta("input_abc", int(input("\ninserire valore a...")), int(input("inserire valore b...")), int(input("inserire valore c...")))
    if intersezione == "si":
        retta2 = retta("input_abc", int(input("\n(seconda retta)inserire valore a...")), int(input("(seconda retta)inserire valore b...")), int(input("(seconda retta)inserire valore c...")))
    else:
        pass

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    if intersezione == "si":
        print("\n il punto di intersezione tra le due rette ha coordinate:\n")
        print(retta.intersezione(retta, retta1, retta2))
        print("\n-------------------------------------------------------------------")
    else:
        pass
   
    print(retta.punti(retta1))

elif tipo_valori == 2:
    retta1 = retta("input_2punti", int(input("inserie x del primo punto...")), int(input("inserie y del primo punto...")), int(input("inserie x del secondo punto...")), int(input("inserie y del secondo punto...")))  
    if intersezione == "si":
        retta2 = retta("input_2punti", int(input("\n(seconda retta)inserie x del primo punto...")), int(input("(seconda retta)inserie y del primo punto...")), int(input("(seconda retta)inserie x del secondo punto...")), int(input("(seconda retta)inserie y del secondo punto...")))
    else:
        pass

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    if intersezione == "si":
        print("\n il punto di intersezione tra le due rette ha coordinate:\n")
        print(retta.intersezione(retta, retta1, retta2))
        print("\n-------------------------------------------------------------------")
    else:
        pass
   
    print(retta.punti(retta1))


elif tipo_valori == 3:
    retta1 = retta("input_coefficiente", int(input("inserie il valore del coefficiente angolare...")), int(input("inserie x del un punto...")), int(input("inserie y del un punto...")))
    if intersezione == "si":
        retta2 = retta("input_coefficiente", int(input("\n(seconda retta)inserie il valore del coefficiente angolare...")), int(input("(seconda retta)inserie x del un punto...")), int(input("(seconda retta)inserie y del un punto...")))
    else:
        pass

    print(retta.eqImplicita(retta1))

    print(retta.eqEsplicita(retta1))

    print(retta.m(retta1))

    if intersezione == "si":
        print("\n il punto di intersezione tra le due rette ha coordinate:\n")
        print(retta.intersezione(retta, retta1, retta2))
        print("\n-------------------------------------------------------------------")
    else:
        pass
   
    print(retta.punti(retta1))
