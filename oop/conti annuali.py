class Conti:

    bilancio = 0

    def __init__(self, data, entrata, motivazioni_entrate, uscita, motivazioni_uscite):
        self.data = data
        self.entrata = int(entrata)
        self.motivazioni_entrate = motivazioni_entrate
        self.uscita = int(uscita)
        self.motivazioni_uscite = motivazioni_uscite
        Conti.bilancio += (self.entrata - self.uscita)
    
    def rapporto(self):
        return f"\n\n---------------\n {self.data}\n---------------\n Entrate:{self.entrata}\n motivo:{self.motivazioni_entrate}\n\n Uscite:{self.uscita}\n motivo:{self.motivazioni_uscite}"

    def bilancio_show():
        return f" \n\n...............\n bilancio complessivo:{Conti.bilancio}\n...............\n\n"




Conti_marzo = Conti("31/03/2021", "1500", "stipendio", "500", "telefono")
Conti_aprile = Conti("20/04/2021", "1500", "stipendio", "1300", "riparazione auto")

#print(Conti_marzo.rapporto())
#print(Conti_aprile.rapporto())

print(Conti.rapporto(Conti_marzo))
print(Conti.rapporto(Conti_aprile))

print(Conti.bilancio_show())