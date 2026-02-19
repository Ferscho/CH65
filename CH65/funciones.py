#Bodmas
#b - soportes o parentecis 
#O - Orden de potencias o raices 
#D M - Divicion y multiplicacion 
#A  S - Suma y resta 

#Funciones: Es un bloque de codigo, que se puede reutilizar, permite modulizar
# tiene parametros y argumentos, le puedo dar datos y me devuelve datos,  
# se manda a llamar. Palabra reservada "def"

def calculadora (num1, num2, opcion):
    if opcion== 1 :
        print(f"El resultado de {num1} mas {num2}: {num1 + num2}")
    elif opcion == 2:
        print(f"El resultado de {num1} menos {num2}: {num1 - num2}")
    elif opcion == 3:
        print(f"El resultado de {num1} por {num2}: {num1 * num2}")
    elif opcion == 4:
        print(f"El resultado de {num1} entre {num2}: {num1 / num2}")
    else:
        print(f"Esta opcion no existe")

calculadora(7,7,4)
calculadora(21,63,3)
calculadora(26,12,4)
calculadora(41,6,2)



"""
# Función 1: Suma varios números que vienen en una lista
def addmultiplenumbers(numbers):
    # 'sum()' es una función ya lista en Python que suma todo lo que hay en la lista
    # Ejemplos:
    # sum([1, 2, 3]) → 6
    # sum([]) → 0 (lista vacía = 0)
    return sum(numbers)
# Función 2: Multiplica varios números que vienen en una lista
def multiplymultiplenumbers(numbers):
    r = 1          # Empezamos con 1 (porque 1 × cualquier cosa = esa cosa)
    for n in numbers:    # Para cada número en la lista...
        r *= n           # ...multiplicamos el resultado acumulado por ese número
    return r
    # Ejemplos:
    # [2, 3, 4] → 1×2×3×4 = 24
    # [1, 2, 3, 0] → ... termina en 0
    # [] (lista vacía) → queda en 1 (esto es convención matemática común)
# Función 3: ¿Es este número un número entero PAR?
def isiteven(num):
    # Tres condiciones deben cumplirse TODAS al mismo tiempo (por eso el 'and'):
    # 1. Es int o float                  → isinstance(num, (int, float))
    # 2. Es un número entero (sin decimales) → num.is_integer()
    # 3. Al convertirlo a entero, el resto de dividir entre 2 es 0 → % 2 == 0
    return isinstance(num, (int, float)) and num.is_integer() and int(num) % 2 == 0
    # Ejemplos:
    # 10     → True   (entero par)
    # 10.0   → True   (float pero es entero y par)
    # 10.5   → False  (tiene decimales)
    # 7      → False  (entero pero impar)
    # "10"   → False  (no es número)
# Función 4: ¿Es este número un entero? (con o sin .0)
def isitaninteger(num):
    # Dos posibilidades aceptables:
    # - Es un int directamente                  → isinstance(num, int)
    # - O es float pero sin parte decimal       → isinstance(num, float) and num.is_integer()
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())
    # Ejemplos:
    # 42     → True
    # 42.0   → True
    # 3.14   → False   (tiene decimales)
    # "42"   → False   (es texto, no número)
    # 5.000  → True
# Esta parte SOLO se ejecuta si corres el archivo directamente
# (no cuando la plataforma importa tu código para evaluarlo)
if __name__ == "__main__":
    print("Tests manuales:")                    # Solo para que veas resultados tú
    print(addmultiplenumbers([5, -2, 7]))       # 5 + (-2) + 7 = 10
    print(multiplymultiplenumbers([1, 2, 3, 0])) # 1×2×3×0 = 0
    print(isiteven(10))                         # True
    print(isiteven(10.0))                       # True
    print(isiteven(10.5))                       # False
    print(isitaninteger(42.0))                  # True
    print(isitaninteger(3.14))                  # False
"""