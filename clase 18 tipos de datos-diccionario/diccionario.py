#declarar un diccionario
diccionario = {
    'eduar' : [5.0, 4.3, 3.7],
    'carla' : [4.4, 5.0, 5.0],
    'miguel' : [3.5, 5.0, 5.0]
}

#dict es una funcion que sirve para crear diiconarios de manera mas sencilla 
dicciionario2 = dict(eduar = [5.0, 4.3, 3.7],
                    carla = [4.4, 5.0, 5.0],
                    miguel = [3.5, 5.0, 5.0])


#diciconarios vacios 
diccionario3 = dict()
diccionario3 ['jose'] = [5.0, 4.3, 3.7]
diccionario3 ['andres'] = [5.0, 4.3, 3.7]
diccionario3 ['miguel'] = [5.0, 4.3, 3.7]

print("diccionario1")
print(diccionario)
print("diccionario2")
print(dicciionario2)
print("diccionario3")
print(diccionario3)



#estos diccionarios tambien son mutables 
diccionario ['jose'] = [5.0, 4.3, 3.7]

print("añadir otro elemento al diccionario")
print(diccionario)

#forma de consulta 
print("consulta de un elemento")
print(diccionario['carla'])

#forma de cambio de valores a una clave queya estaen mi diccionario
print("cambio de valores de un elemento")
diccionario['carla'] = [1.0, 1.0, 1.0]
print(diccionario)

#eliminar elenemtos de mi diccionario 
print("eliminar unelemento ")
del diccionario['carla']
print(diccionario)

#visualizacion de diccionarios 
#llaves 
print("llaves de los elementos ")
print(diccionario.keys())

#values o valores
print("valores de los elementos ")
print(diccionario.values())
print(diccionario)

#items
print("items de los elementos")
print(diccionario.items())
print(diccionario)