class retta:

    x= 0
    y= 0

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def implicita(self):
        return f"---------------------------\n\n equazione forma implicita: \n {self.a}x + {self.b}y + {self.c} = 0 "

    def esplicita(self):
        return f"\n\n equazione forma esplicita: \n {self.b}y = {- self.a}x + {- self.c} \n\n ---------------------------"

    def lista_punti(self):
        for i in range(10):
            retta.x += i
            retta.y += i
            print(f"\n x= {(- self.b * retta.y - self.c) / self.a} \n y= {(- self.a * retta.x - self.c) / self.b}")




retta1 = retta(input("inserire valore a..."), input("inserire valore b..."), input("inserire valore c..."))



print(retta.implicita(retta1))

print(retta.esplicita(retta1))

print(retta.lista_punti(retta1))