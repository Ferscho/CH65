""" Pograma de calculadora Avanzada"""

# Definimos la funcion addmultiplenumbers
def addmultiplenumbers(nums):
    """Devuelve la suma de una lista de números."""
    return sum(nums)

# definimos la funcion multiplymultiplenumbers
def multiplymultiplenumbers(nums):
    """Devuelve el producto de una lista de números.."""
    result = 1
    for num in nums: 
        result *= num
    return result

# definimos la funcion isiteven
def isiteven(num): # isinstance: sirve para comprobar si un objeto pertenece a un tipo de dato específico. devuel un booleano 
    """Devuelve True si num es un número entero par, False en caso contrario."""
    # Verifica tanto el tipo entero como la paridad
    return isinstance(num, int) and num % 2 == 0  # si al dividir entre 2 y su resuido es 0 es par 

# definimos la funcion isitaninteger
def isitaninteger(num):
    """Devuelve True si num es un número entero, False en caso contrario."""
    return isinstance(num, int)

# comenzamos con main 
def main():
    print("Hello learners!")
    # Ejemplo de uso interactivo
    nums_1 = [6, 8, 13]
    print("Suma:", addmultiplenumbers(nums_1))
    print("Produto:", multiplymultiplenumbers(nums_1))
    print("Is 4 even?", isiteven(4))
    print("Is 4.5 an integer?", isitaninteger(4.5))


if __name__ == "__main__":
    main()



  