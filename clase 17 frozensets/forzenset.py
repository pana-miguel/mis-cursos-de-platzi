#frozenset sirve para optimizar memoria o para hacer diciionarios 
frutas = ("pera", "manzana", "uva")

miFrozenSet = frozenset(frutas)
print(miFrozenSet)


#no se pueden agregar en un frozenset otro dato
miFrozenSet.add("naranja") #esto genera un error 

