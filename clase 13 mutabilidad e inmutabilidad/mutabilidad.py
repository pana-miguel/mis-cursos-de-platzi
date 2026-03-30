#Mutabilidad (listas): Puedes modificar directamente los elementos de una lista, agregar nuevos elementos o eliminarlos 
# sin crear un nuevo objeto.

# Las listas son mutables
lista = [1, 2, 3]
print(f"Lista original: {lista}")

# Modificando un elemento de la lista
lista[1] = 99
print(f"Lista despues de modificar un elemento: {lista}")

# Agregando un nuevo elemento
lista.append(4)
print(f"Lista despues de agregar un elemento: {lista}")

# Eliminando un elemento
lista.remove(99)
print(f"Lista despues de eliminar un elemento: {lista}")
