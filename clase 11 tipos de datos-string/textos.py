# Ejemplo con len para calcular la longitud de una cadena
mensaje = "Hola, mundo"
longitud = len(mensaje)
print(f"La longitud del mensaje '{mensaje}' es {longitud} caracteres.")

# Ejemplo usando triple comilla con un texto de correo
correo = """Estimado cliente,

Gracias por elegir nuestros servicios. Nos complace informarle que su cuenta ha sido creada exitosamente. 
Si tiene alguna pregunta o necesita ayuda, no dude en contactarnos.

Atentamente,
El equipo de soporte
"""

print("Texto del correo:")
print(correo)



#con los tipos de datos strings tambien se pueden hacer prefijos y sufijos estos son para eliminar ciertos caracteres dentro de un texto 
#esto es por si solo queremos tomar una parte de la variable

producto1 = "0001 - manzana"
producto2 = "durazno - 0001"

print(producto1)
print(producto2)

print(producto1.removeprefix('0001 - '))
print(producto2.removesuffix(' - 0001'))
