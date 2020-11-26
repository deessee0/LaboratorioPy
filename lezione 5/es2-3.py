from datetime import datetime
#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name

    def __str__(self):
        pass

    
    def get_date_vendite(self):
        values = []

        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                my_date  = datetime.strptime(elements[0], '%d-%m-%Y')
                value = elements[1]
                
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(my_date)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return values

    
        
#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_date_vendite()))
