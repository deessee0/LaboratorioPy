#======================
# Classe per file CSV
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
        print("Casa automobilistica: {}\nModello Automobile: {}\nNumero posti: {}\nNumero portiere: {}\nKw: {}\nTarga: {}".format())

    
 
#======================
# Corpo del programma
#======================

alfa_giulia = ("Alfa Romeo", "Giulia", 5, 5, 200, "ax9009")