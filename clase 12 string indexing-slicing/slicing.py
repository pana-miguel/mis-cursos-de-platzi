# Variable con el texto
mensaje = "Hola, mundo"


subcadena_revez = mensaje[::-1]  # Cadena completa al revés
print(f"Subcadena al reves (::-1): {subcadena_revez}")

# Slicing parcial al revés
parcial_revez = mensaje[-1:-6:-1]  # Desde el último carácter hasta el sexto desde el final
print(f"Subcadena parcial al reves (-1:-6:-1): {parcial_revez}")
