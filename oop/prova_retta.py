class retta:

    def __init__(self, __a, __b, __c):
        self._a = float(__a)
        self._b = float(__b)
        self._c = float(__c)
        self._xy = (0, 0)
        self.lista_punti = []

    
    
    def implicita(self):
        if self._b == 0:
            return f"---------------------------\n\n equazione forma implicita: \n {self._a}x + {self._c} = 0 \n (y= 0) "
        elif self._a == 0:
            return f"---------------------------\n\n equazione forma implicita: \n {self._b}y + {self._c} = 0 \n (x= 0) "
        else:
            return f"---------------------------\n\n equazione forma implicita: \n {self._a}x + {self._b}y + {self._c} = 0 "

    def esplicita(self):
        if self._b == 0:
            return f"\n\n equazione forma esplicita: \n x = {- self._c/ self._a} \n (y= 0) \n\n ---------------------------"
        elif self._a == 0:
            return f"\n\n equazione forma esplicita: \n y = {- self._c/ self._b} \n (x= 0) \n\n ---------------------------"
        else:
            return f"\n\n equazione forma esplicita: \n y = {- self._a / self._b}x + {- self._c/ self._b} \n\n ---------------------------"

    def coefficiente_angolare(self):
        if self._b == 0:
            return f"\ncoefficiente angolare: \n\n la retta è parallela all'asse delle y, il coefficiente angolare non è definito in alcun modo... \n\n ---------------------------"
        else:
            return f"\ncoefficiente angolare: \n\n m= {- self._a / self._b} \n\n ---------------------------"

    def ricavo_punti(self):

        inizio = - (1/2) * int(n)
        fine = (1/2) * int(n)

        if self._a == 0:
            for i in range(int(inizio), int(fine)):
                x = i
            self.lista_punti.append((x, - self._c/ self._b))
        
        elif self._b == 0:
            for i in range(int(inizio), int(fine)):
                y = i
            self.lista_punti.append((- self._c/ self._a, y))

        else:    
            for i in range(int(inizio), int(fine)):
                x = i
                self.lista_punti.append ((x, (- self._a * x - self._c) / self._b))
        
        print(self.lista_punti)



while True:

    menù = int(input("\n-Premi 1 per creare una nuova retta\n-Premi 2 per utilizzare una retta già esistente\n-->"))

    while True:

        if menù == 1:
            nome_retta = str(input("come vuoi chiamare la tua nuova retta\n -->"))
            nome_retta = retta(input("inserire valore a..."), input("inserire valore b..."), input("inserire valore c..."))
            
            while True:
                scelta1=input("la tua retta è stata creata correttamente \n digita 'm' per tornare al menù principale\n-->")
                if scelta1 == "m":
                    break
                else: 
                    print("errore")
            break
    
        elif menù == 2:
            
            nome_retta1= str(input("di quale retta vuoi ricavare le informazioni? \n inserisci il nome-->"))
            n = (input("quante coppie di ordinate vuoi ricavare?..."))
            
            print(retta.implicita(str(nome_retta1)))

            print(retta.esplicita(str(nome_retta1)))

            print(retta.coefficiente_angolare(str(nome_retta1)))

            print(retta.ricavo_punti(str(nome_retta1)))

        else:
            print("errore, non hai inserito uno dei due valori")
            break
        



