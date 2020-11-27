#======================
# Classe per file Automobile
#======================

class Automobile:

    def __init__(self, casa_auto, modello, numero_posti, numero_portiere, kw, targa):
        
        self.casa_auto = casa_auto
        self.modello = modello
        self.numero_posti = numero_posti
        self.numero_portiere = numero_portiere
        self.kw = kw
        self.targa = targa

    def __str__(self):
        print("Casa automobilistica:", self.casa_auto, "\n", "Modello Automobile:", self.modello, "\n", "Numero posti:", self.numero_posti,"\n", "Numero portiere:", self.numero_portiere, "\n", "Kw:", self.kw, "\n", "Targa:", self.targa)
        
    def parla(self):
        print("Broom Broom")
    
    def confronta(self, istance):
        if self.casa_auto == istance.casa_auto and self.numero_posti == istance.numero_posti and self.numero_portiere == istance.numero_portiere and self.kw == istance.kw:
            print("Le due autovetture hanno le stesse informazioni, esclusa la targa")
        else: print("Le due autovetture non hanno le stesse informazioni") 

    def bollo(self, euro):
        euro = input('Inserisci la categoria della tua autovettura:')

        if euro == "Euro0":
            costokm_below100 = 3
            costokm_below100 = 4.50
            
    
    def separatore():
        print("-~-~-o-~-~-o-~-~-")

#======================
# Corpo del programma
#======================

alfa_giulia = Automobile("Alfa Romeo", "Giulia", 5, 5, 200, "ax9009")
alfa_giulia1 = Automobile("Alfa Romeo", "Giulia", 5, 5, 200, "ax9009")
alfa_giulia.__str__()
alfa_giulia.confronta(alfa_giulia1)