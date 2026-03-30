#las listas son inmutables y se pueden modificar

lista_numeros = [1, 2, 3, 4, 5]
lista_nombres = ["jose", "andres", "camilo"]

print(lista_nombres)

lista_nombres[2] = "gloria"

print(lista_nombres)

#aqui creamos esta tupla en una lista con la funcion list
lista_numeros = list((1, 2, 3))
print(type(lista_numeros))

