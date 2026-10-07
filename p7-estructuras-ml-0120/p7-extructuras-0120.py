# Nicole Robles NC 0120
# ------------------------------------------------------------------------------
# 1. PYTHON CONDITIONS
# ------------------------------------------------------------------------------
print("=== 1. PYTHON CONDITIONS ===")
print(" ==========================================")
# Ejemplo 1.1: Uso de la estructura 'if' simple con operador de comparación (>)
temperatura = 28

if temperatura > 25:
    print(
        f"[Ejemplo 1.1 - Sentencia IF simple]: Hace calor (Temperatura: {temperatura}°C)."
    )

# ------------------------------------------------------------------------------
# 2. PYTHON IF...ELIF
# ------------------------------------------------------------------------------
print("\n=== 2. PYTHON IF...ELIF ===")
print(" ==========================================")

# Ejemplo 2.1: Estructura 'if...elif' para evaluar múltiples condiciones
nota = 85

if nota >= 90:
    print("[Ejemplo 2.1 - Sentencia IF...ELIF]: Excelente calificación.")
elif nota >= 80:
    print(
        f"[Ejemplo 2.1 - Sentencia IF...ELIF]: Buena calificación (Nota: {nota})."
    )

# ------------------------------------------------------------------------------
# 3. PYTHON IF...ELSE
# ------------------------------------------------------------------------------
print("\n=== 3. PYTHON IF...ELSE ===")
print(" ==========================================")

# Ejemplo 3.1: Estructura 'if...else' completa
edad = 16

if edad >= 18:
    print("[Ejemplo 3.1 - Sentencia IF...ELSE]: Eres mayor de edad.")
else:
    print(
        f"[Ejemplo 3.1 - Sentencia IF...ELSE]: Eres menor de edad (Edad: {edad})."
    )

# Ejemplo 3.2: Short Hand If...Else (Ternary Operator)
estado_acceso = "Permitido" if edad >= 18 else "Denegado"
print(f"[Ejemplo 3.2 - Short Hand If...Else]: Acceso {estado_acceso}.")

# Ejemplo 3.3: Operadores lógicos (and, or, not)
tiene_pago = True
tiene_identificacion = True

if tiene_pago and tiene_identificacion:
    print(
        "[Ejemplo 3.3 - Operadores Lógicos (AND)]: Registro completado con éxito."
    )

# Ejemplo 3.4: Condicionales anidados (Nested If)
es_miembro = True
puntos = 120

if es_miembro:
    if puntos > 100:
        print(
            "[Ejemplo 3.4 - Nested IF]: Calificas para un descuento VIP especial."
        )

# Ejemplo 3.5: Instrucción 'pass'
variable_vacia = True
if variable_vacia:
    pass
print("[Ejemplo 3.5 - Instrucción PASS]: Evaluado correctamente con 'pass'.")
print(" ==========================================")
# ------------------------------------------------------------------------------
# 4. PYTHON FOR LOOPS
# ------------------------------------------------------------------------------
print("\n=== 4. PYTHON FOR LOOPS ===")
print(" ==========================================")

# Ejemplo 4.1: Recorrer una lista (Iteración sobre colección)
lenguajes = ["Python", "JavaScript", "C++"]
print("[Ejemplo 4.1 - For en Lista]:")
for lenguaje in lenguajes:
    print(f"  - Lenguaje: {lenguaje}")

# Ejemplo 4.2: Iterar sobre una cadena de texto (String)
palabra = "Code"
print("[Ejemplo 4.2 - For en Cadena de Texto]:")
for letra in palabra:
    print(f"  Letra: {letra}")

# Ejemplo 4.3: Sentencia 'break' en bucle For
print("[Ejemplo 4.3 - For con BREAK]:")
frutas = ["Manzana", "Banana", "Uva", "Naranja"]
for fruta in frutas:
    if fruta == "Uva":
        print(f"  Se encontró '{fruta}', interrumpiendo el bucle.")
        break
    print(f"  Procesando: {fruta}")

# Ejemplo 4.4: Sentencia 'continue' en bucle For
print("[Ejemplo 4.4 - For con CONTINUE]:")
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    if n % 2 == 0:
        continue
    print(f"  Número impar: {n}")

# Ejemplo 4.5: Uso de la función range()
print("[Ejemplo 4.5 - For con RANGE]:")
for i in range(1, 4):
    print(f"  Iteración número: {i}")

# Ejemplo 4.6: Bloque 'else' en bucle For
print("[Ejemplo 4.6 - For con ELSE]:")
for x in range(3):
    print(f"  Pasada {x}")
else:
    print("  El bucle 'for' ha finalizado correctamente.")
    print(" ==========================================")
# ------------------------------------------------------------------------------
# 5. PYTHON WHILE LOOPS
# ------------------------------------------------------------------------------
print("\n=== 5. PYTHON WHILE LOOPS ===")
print(" ==========================================")

# Ejemplo 5.1: Bucle 'while' básico
contador = 1
print("[Ejemplo 5.1 - Bucle WHILE básico]:")
while contador <= 3:
    print(f"  Contador en: {contador}")
    contador += 1

# Ejemplo 5.2: Sentencia 'break' en bucle While
i = 1
print("[Ejemplo 5.2 - While con BREAK]:")
while i < 10:
    print(f"  Valor: {i}")
    if i == 3:
        print("  Se alcanzó el 3, rompiendo el bucle While.")
        break
    i += 1

# Ejemplo 5.3: Sentencia 'continue' en bucle While
j = 0
print("[Ejemplo 5.3 - While con CONTINUE]:")
while j < 4:
    j += 1
    if j == 2:
        continue
    print(f"  Valor impreso: {j}")

# Ejemplo 5.4: Bloque 'else' en bucle While
k = 1
print("[Ejemplo 5.4 - While con ELSE]:")
while k < 3:
    print(f"  Paso {k}")
    k += 1
else:
    print("  La condición del bucle While ya no es verdadera.")
    print(" ==========================================")
    print("--------------Nicole Robles NC 0120---------------")