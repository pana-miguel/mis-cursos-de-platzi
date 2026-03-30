#en una tupla funciona igual que una lista con ladiferencia que la tupla puede almacenar diferentes tipos dedatosy las listas solo uno

my_tupla = (1, 3.14 ,"adrian, True")
print(my_tupla)
print(my_tupla[2])

print(type(my_tupla))

#en una funcion que tiene ciertos valores en este caso nombre edad y nota de un estudiante podemos hacer que depues sea almacenado en una tupla 

def retornar_estudiante():
    return "adrian", 35, 4.3

tupla_estudiante = retornar_estudiante()
print(tupla_estudiante)

#para guardar la informacion en varias variables y no solo en la tupla se puedehcaer de la siguiente manera

nombre_estudiante, edad_estudiante, nota_estudiante = retornar_estudiante()
print(nombre_estudiante)
print(edad_estudiante)
print(nota_estudiante)
