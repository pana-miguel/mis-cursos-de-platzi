# Variable con el texto
mensaje = "Hola, mundo"


# Indexing: Accediendo a caracteres individuales
primera_letra = mensaje[0]  # Primer carácter
ultima_letra = mensaje[-1]  # Último carácter
print(f"Primera letra: {primera_letra}")
print(f"ultima letra: {ultima_letra}")

# Indexing al revés
indice_negativo = mensaje[-5]  # Accede a 'm' desde el final
print(f"Letra en indice negativo -5: {indice_negativo}")

# Slicing: Obteniendo porciones de la cadena
subcadena_derecho = mensaje[0:4]  # Primeras 4 letras ("Hola")
print(f"Subcadena al derecho (0:4): {subcadena_derecho}")