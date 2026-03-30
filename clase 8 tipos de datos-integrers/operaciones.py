#estas son todas las operaciones ue se pueden hacer en python en las cuales estan suma restas multiplicacion division 
#comparadores y seguimiento bit a bit


# Definimos dos variables numéricas
num1 = 10
num2 = 3

# Operaciones aritméticas
resultado = num1 + num2
print(f"Suma: {num1} + {num2} = {resultado}")

resultado = num1 - num2
print(f"Resta: {num1} - {num2} = {resultado}")

resultado = num1 * num2
print(f"Multiplicacion: {num1} * {num2} = {resultado}")

resultado = num1 / num2
print(f"Division: {num1} / {num2} = {resultado}")

resultado = num1 // num2
print(f"Division entera: {num1} // {num2} = {resultado}")

resultado = num1 % num2
print(f"Resto (modulo): {num1} % {num2} = {resultado}")

resultado = num1 ** num2
print(f"Potencia: {num1} ** {num2} = {resultado}")

# Operaciones relacionales
resultado = num1 > num2
print(f"{num1} > {num2}: {resultado}")

resultado = num1 < num2
print(f"{num1} < {num2}: {resultado}")

resultado = num1 >= num2
print(f"{num1} >= {num2}: {resultado}")

resultado = num1 <= num2
print(f"{num1} <= {num2}: {resultado}")

resultado = num1 == num2
print(f"{num1} == {num2}: {resultado}")

resultado = num1 != num2
print(f"{num1} != {num2}: {resultado}")

# Operaciones lógicas
resultado = num1 > 0 and num2 > 0
print(f"{num1} > 0 and {num2} > 0: {resultado}")

resultado = num1 > 0 or num2 < 0
print(f"{num1} > 0 or {num2} < 0: {resultado}")

resultado = not (num1 > num2)
print(f"not ({num1} > {num2}): {resultado}")

# Operaciones bit a bit
resultado = num1 & num2
print(f"{num1} & {num2} (AND bit a bit): {resultado}")

resultado = num1 | num2
print(f"{num1} | {num2} (OR bit a bit): {resultado}")

resultado = num1 ^ num2
print(f"{num1} ^ {num2} (XOR bit a bit): {resultado}")

resultado = num1 << num2
print(f"{num1} << {num2} (Desplazamiento a la izquierda): {resultado}")

resultado = num1 >> num2
print(f"{num1} >> {num2} (Desplazamiento a la derecha): {resultado}")

# División por cero 
try:
    resultado = num1 / 0
    print(f"División por cero: {num1} / 0 = {resultado}")
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
