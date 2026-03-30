#en solo se hace una comparacion en varias lineas a diferencia que un opeador ternario que se hace en una sola linea

edad = int(input("ingrese su edad: "))

#operador ternario este sirve para hacer una coparacion ed una sola linea 

mensaje = "usted es mayor de edad " if edad >= 18 else "usted es menor de edad "
print(mensaje)