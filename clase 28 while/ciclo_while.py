#ciclo while es un ciclo que se repite mientras la condicion sea verdadera o se cumpla la condicion que se le de al cliclo 

nombre = ""
correo = ""
mensaje = ""

condicion_salida = "CONTINUE" #este condicional es para que el cilco while se ejecute al menos una vez 
 
while condicion_salida == "CONTINUE": #mientras la condicion sea verdadera o igual a "CONTINUE" se ejecutara el cliclo
    nombre = input("ingrese su nombre: ")
    correo = input("ingrese su correo: ")
    mensaje = input("ingrese su mensaje: ")

    print(f"""
    mensaje enviado a {correo}  
    destinatariuo: {nombre}
      
    mensaje a enviar: {mensaje}
      """)

    condicion_salida = input("en caso de querer continuar con el programa escriba CONTINUE: ") #si el usuario escribe CONTINUE el ciclo se ejecutara nuevamente


