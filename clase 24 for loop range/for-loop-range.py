#for loop range esta es una funcion que se utiliza para generar una secuencia de numeros en un rango especifico 

#esta es la sintaxis de la funcion range pero se esta utilizando es un for loop que no es lo mas optimo
lista = [0, 1, 2, 3]

print("ejemplo 1")
for iter in lista:
    print("desde origen avanzar 10 pasos ")
    print("girar 10 pasos")


#en etse caso si usaremos la funcion range para generar una secuencia de numeros en un rango especifico 

#codigo corregido de el de arriba para que el codigo sea mas limpio y optimo
print("ejemplo 2")

for _  in range(4):   #el signo _ se indica que no se va a utoilizar la variable en el for loop
    print("desde origen avanzar 10 pasos ")
    print("girar 10 pasos")





