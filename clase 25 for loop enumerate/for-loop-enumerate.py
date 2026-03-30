#for loop enumerate esta funcion sirve para 
#recorrer una lista y obtener el indice y el valor 

#en este caso se muesta solo el nombre de las personas que estan en la lista 
lista_nombres = ['juan', 'jose','andres']

print("ejemplo 1")
for nombre in lista_nombres:
    print(nombre)


#aqui se muestra el indice y el nombre de la persona

print("ejemplo 2")
for indice in range(3):
    print(indice) #imprime el indice
    print(lista_nombres[indice]) #imprime el nombre
    print(indice, lista_nombres[indice]) #imprime el indice y el nombre 

#funcion enumerate esta es la mejor forma de recorrer una lista y que nos mueste el indice y valor de cada una de las pociciones de la lista 
print("ejemplo 3")
for indice, valor in enumerate(lista_nombres):
    print(indice, valor ) #imprime el indice y valor de la lista