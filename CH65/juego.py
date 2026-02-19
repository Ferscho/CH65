
for i in range(1, 1001):  # el for va a tener el rango del 1 al 1000
    if i % 3 == 0 and i % 5 == 0 : # 
        print(i, "izzbuzz")
    elif i % 5 == 0:   # 
        print(i, "buzz")  #Si es divicible entre 5 se imprime BUZZ 
    elif i % 3 == 0:     # 
        print(i, "izz")  # si es divicuble entre 3 se imprime izz
   
    else:               #
        print(i)


# Ejemplo de FizzBuzz con while

i = 1   # Inicialización

while i <= 20:   # Condición
    if i % 3 == 0 and i % 5 == 0:
        print(i, "izzbuzz")
    elif i % 3 == 0:
        print(i, "izz")
    elif i % 5 == 0:
        print(i, "buzz")
    else:
        print(i)
    
    i += 1   # Actualización para evitar ciclo infinito

print("Fin del ciclo")
