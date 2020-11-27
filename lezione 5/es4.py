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
        euro = input('Inserisci la categoria della tua autovettura: ')

        if euro == "Euro0":
            if self.kw > 100:
                bollo = 4.5 * self.kw
            else: 
                bollo = 3 * self.kw
        elif euro == "Euro1":
            if self.kw > 100:
                bollo = 4.35 * self.kw
            else: 
                bollo = 2.50 * self.kw
        elif euro == "Euro2":
            bollo = 3 * self.kw
        else: 
            return print("Inserisci Euro0, Euro1 o Euro2 ")

        return print("Costo del bollo:",bollo)
    
    def separatore():
        print("-~-~-o-~-~-o-~-~-")

#======================
# Corpo del programma
#======================

alfa_giulia = Automobile("Alfa Romeo", "Giulia", 5, 5, 99, "ax9009")
alfa_giulia1 = Automobile("Alfa Romeo", "Giulia", 5, 5, 101, "ax9009")
alfa_giulia.__str__()
Automobile.separatore()
alfa_giulia.confronta(alfa_giulia1)
Automobile.separatore()
alfa_giulia.bollo("Euro1")
Automobile.separatore()