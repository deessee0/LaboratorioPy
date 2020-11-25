def isintlist( mylist):
    cane = True
    for k in range(len(mylist)):
        if type(mylist[k]) != type(1):
            cane = False
    return cane

def listlen(list1,list2):
    if len(list1) == len(list2):
        return True
    else: return False

def stampa( mylist ):
    print(mylist,"\n")
    return None
    
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

def somma_vettoriale( first, second):
    if isintlist(first) and isintlist(second) == True:
        

def prodotto_vettoriale():
    pass

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [10,9,8,7,6,5,4,3,2,1]

stampa(lista1)
statistiche(lista1)