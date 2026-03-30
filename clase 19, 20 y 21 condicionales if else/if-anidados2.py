#tambien se puede realizar este ejecicio de la sguiente forma todo depende de la logica de programacion que se tnega

edad = int(input("ingrese su edad: "))
altura = int(input("ingrese su altura: "))

if edad >= 18:
    if altura >=170 or (edad >= 25 and altura >= 165 and altura <=169):
        print("puede participar")
    else:
        print("no puede participar")