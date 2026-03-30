#aunque la siguiente variable si cambien internamente lo que pasa es que el id de la variable e crea con el hola mundo
#y cuando la cambiamos se borra ese id y se crea uno nuevo

# Las cadenas de texto son inmutables
texto = "Hola, mundo"
print(texto)

texto = "como estan"
print(texto)


#los que pasa con las listas es que si copiamos exactamente otra listalas dos tendran el mismo id
#y si queremos cambiar una de las dos afectara a la otra tambien generando muchas veces errores

lista1 = ['jose','carlos','andres']
print(lista1)

lista2 = lista1
print(lista2)

lista2[1] = 'camilo'
print(lista2)
print(lista1)