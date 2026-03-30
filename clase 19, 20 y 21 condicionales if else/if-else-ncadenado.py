#if else encadenado si no se cumple la primera condicion el progrema pasa a la siguiente condicion hasta que se cumpla una de ellas 
#si no se cumple ninguna de las condiciones se ejecutara el else final 

edad = 80

if edad >=0 and edad <=12:
    print("usted es un niño")
elif edad >=13 and edad <=17:
    print("usted es un adolecente")
elif edad >=18 and edad <= 50:
    print("usted es un adulto")
else:
    print("usted es un adulto mayor")