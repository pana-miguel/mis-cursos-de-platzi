#declaraicon del set
#los sets funcionan para la declaracion de busquedas en bigquery o en las bases de datos en general 

mi_set = {1, 5, 8, 14 ,2 ,4 ,9, 17}
print(mi_set)

#en esta forma tambien se puede hacer los sets pero no se pueden añadir elementos repetidos porque eliminara uno de los dos 
miSet = set()
miSet.add(4)
miSet.add(3)
miSet.add(8)
miSet.add(200)
miSet.add(1)
miSet.add(0)

#estaforma de pasar una lista a un set sirve para eliminar los datos repetidos de una lista y solo dejar todos los datos diferentes que tenga
#osea que si tiene un dato repetido o mas loseliminara y solo dejara uno de ellos
mi_sets = [1, 5, 8, 14 ,2 ,4 ,9, 17, 5, 5, 5, 5, 5, 5, 5]
mi_sets = set(mi_sets)
print(mi_sets)

#para saber si hay un elemento dentro de un se de puede hacer de la siguiente doorma 
print(9 in mi_sets) #si esta en este caso dentro de mi set
print(100000 in mi_sets) #no esta en este caso dentro de mi set

