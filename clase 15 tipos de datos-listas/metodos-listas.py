lista_numeros = [1, 2, 3]

#append este agrega un elemento al final de la lista
lista_numeros.append(4)
lista_numeros.append(5)
lista_numeros.append(100)
lista_numeros.append(100)

print(lista_numeros)

#count cuenta cuantas veces se repite un elmento en una lista
print(lista_numeros.count(100))

#extend agrega una listaa a otra lista
lista_extendida = [100, 101]

lista_numeros.extend(lista_extendida)
print(lista_numeros)

#index devuelve el indice de un elemento en una lista
print(lista_numeros.index(100))

#insert inserta un elemento en una posicicion especifica 
lista_numeros.insert(8, 5000)
print(lista_numeros)

#pop el ultimo elemento de la lista
print(lista_numeros)
print(lista_numeros.pop()) #ultimo elemento 
print(lista_numeros.pop(0)) #primer elemento que nosotros definimos

#remove elimina un elemento de la lista 
lista_numeros.remove(100)
print(lista_numeros)

#reverse invierte la lista
print(lista_numeros) 
lista_numeros.reverse()
print(lista_numeros)

#clear elimina todos los elementos de una lista 
lista_numeros.clear()
print(lista_numeros)

#sort ordena la lista
lista_nueva = [4, 6, 91, 1000, 3]
print(lista_nueva)
lista_nueva.sort()
print(lista_nueva)
