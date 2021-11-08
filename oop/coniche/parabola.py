'''
PARABOLA
La classe parabola deve gestire un oggetto relativo alla rappresentazione e costruzione
di una parabola.
- Il costruttore dovrà tenere conto di tutte le possibilità di generazione di una parabola.
-- tramite parametri (a,b,c)
-- tramite fuoco e direttrice
-- rapporti con altri ogggetti (tangenza con rette, passaggio per punti ecc..)
'''

#devi ancora implementare l'eventualità di una parabola verticale e l'equazione a partire dal fuoco e della direttrice

class parabola:
    def __init__(self, tipo = None, p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):
            
            self.__dati = str(tipo)
            self.__a = int(p1)
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []

            self.delta = int(self.__b * self.__b - 4 * self.__a * self.__c)

        elif(tipo == "fuocoDiret"):
            self.__xfuoco = p1  
            self.__yfuoco = p2
            #da usare quando si implementa la parabola verticale self.__xdirettrice = p3
            self.__ydirettrice = p4
            pass
    


    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def equazione(self):
        if tipo_valori == 1:
            if self.__a == 0:
                pass
                
            elif self.__a > 0:
                return f"\nla parabola è rivolta verso l'alto \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x + {self.__c} "
                
            elif self.__a < 0:
                return f"\nla parabola è rivolta verso il basso \n\n equazione parabola:\n y = {self.__a}x^2 + {self.__b}x + {self.__c} "
        elif tipo_valori == 2:
            return f"\nnon so come ricavare l'equazione dal fuoco e dalla direttrice"

    def fuoco(self):
        if tipo_valori == 1:
            return f" \n\n Fuoco:\n x= {- self.__b / 2 * self.__a}   y= {(1 - self.delta)/ 4 * self.__a}"
        elif tipo_valori == 2:
            return f" \n\n Fuoco:\n x= {self.__xfuoco}   y= {self.__yfuoco}"

    def direttrice(self):
        if tipo_valori == 1:
            return f"\n Direttrice: \n y= {- (1 + self.delta)/ 4 * self.__a}\n"
        elif tipo_valori == 2:
            return f"\n Direttrice: \n y= {self.__ydirettrice}\n"


        




        

tipo_valori = int(input("\n\nche tipi di valore stai dando? \n\n1) a, b, c\n2) coordinate del fuoco e della direttrice \n\ndigitare 1 o 2 a seconda della risposta..."))

if tipo_valori == 1:
    parabola1 = parabola("param", input("\ninserire valore a..."), input("inserire valore b..."), input("inserire valore c..."))

    print(parabola.equazione(parabola1))
    print(parabola.fuoco(parabola1))
    print(parabola.direttrice(parabola1))

elif tipo_valori == 2:
    parabola1 = parabola("fuocoDiret", input("inserie x del fuoco..."), input("inserie y del fuoco..."), input("inserie x della direttrice..."), input("inserie y della direttrice..."))  

    print(parabola.equazione(parabola1))
    print(parabola.fuoco(parabola1))
    print(parabola.direttrice(parabola1))
