""" Este es un pograma que detecta que nuemero que va desde el 1 al 1000 si es divisible entre 3 y 5 o ambos casos """

for i in range(1, 1001):  # el for tiene el rango del 1 al 1000 
    if i % 3 == 0 and i % 5 == 0 : # si es divicible entre 3 y 5 se imprime izzbuzz
        print(i, "izzbuzz")
    elif i % 3 == 0:     # 
        print(i, "izz")  # si es divisible entre 3 se imprime izz 
    elif i % 5 == 0: 
        print(i, "buzz") # si es divisible entre 5 se imprime buzz
   
    else:               #
        print(i)      # sigue con el siguinete numero hasta llegar al 1000

