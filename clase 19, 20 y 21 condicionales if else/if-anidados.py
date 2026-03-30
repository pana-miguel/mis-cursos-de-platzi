#desarrollar un script que pida la edad y la altura del usuario 
#si la persona es mayor de edad puede participar 
#si la persona no mide 170 podra participar si es mayor de 25 años 
#y si altura es mayor a 165 

edad = int(input("ingrese su edad: "))
altura = int(input("ingrese su altura: "))

if edad >= 18 and altura >=170:
    print("puede participar")
elif edad >= 25 and altura <=169 and altura >= 165:
    print("puede participar")
else: 
    print("no puede participar")










