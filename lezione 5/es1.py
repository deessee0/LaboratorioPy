def isintlist( mylist ):
    cane = True
    for k in range(len(mylist)):
        if type(mylist[k]) != type(1):
            cane = False
    return cane

def listlen( list1, list2 ):
    if len(list1) == len(list2):
        return True
    else: return False

def stampa( mylist ):
    print(mylist,"\n")
    return mylist
    
def statistiche( mylist ):
    if isintlist(mylist) == True:

        minimo = min(mylist) 
        massimo = max(mylist)
        nElementi = len(mylist)
        somma = 0

        for i in range(nElementi):
            somma += mylist[i]
        
        media = somma / nElementi

        print("Valore minimo della lista: {}".format(minimo))
        print("Valore massimo della lista: {}". format(massimo))
        print("Valore medio della lista: {}".format(media))  

    else: print("Dammi una lista di soli interi") 

def somma_vettoriale( list1, list2 ):
    if isintlist(list1) and isintlist(list2) == True:
        if listlen(list1,list2) == True:
            stampa([list1[i]+list2[i] for i in range(len(list1))])
        else: print("Le list date in input non hanno la stessa lunghezza")
    else: print("Le liste non sono composte esclusivamente da numeri interi")

    return None

def prodotto_vettoriale( list1, list2 ):
    if isintlist(list1) and isintlist(list2) == True:
        if listlen(list1,list2) == True:
            stampa([list1[i]*list2[i] for i in range(len(list1))])
        else: print("Le list date in input non hanno la stessa lunghezza")
    else: print("Le liste non sono composte esclusivamente da numeri interi")

    return None

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = [9,8,7,6,5,4,3,2,1]

somma_vettoriale(lista1,lista2)
prodotto_vettoriale(lista1,lista2)
print("\n")