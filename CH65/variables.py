#Tipo de datos y variables 
#Variables : son espacios que se almacenan informacion en la memoria de mi pograma 
#Tipos de datos : string, number int o float, boolean y lista 

#string es una cadena de texto  "Fernando"
#enteros : Nuemros enteros 33 
#Flotantes : numeros decimales 12.25
#bolean : True o False 
#Lista : Lleva corchetes, es una lista ordenada, indice y se empieza a partir del 0. 

print(type("Hola"))
print(type(45))
print(type(25.36))
print(type(True))
print(type([9,9,10]))

nombre = "fernando"
edad = 28 
participante = True
instrucion = False

#Lista con diferentes tipos de datos 
lista_1= ["Fernando", 28, True]

print("Lista inicial: ", lista_1)

print("Hola "+ " tu edad es " + str(edad) )

#agregar un nuevo elemento a la lista 
lista_1.append("instruccion ")

print(" Lista con un nuevo elemento: ", lista_1)

#Agregar elemento al principio
lista_1.insert(0, "intrucción")

print("Lista con elemento al inicio", lista_1)

#Elimina el ultimo elemento 
eliminar_elemento = lista_1.pop()

print("elemento eliminado", eliminar_elemento)
print("Lista despues de pop:")

#Verificar el tipo de elemento 
print("\n Tipos de datos de la lista:")

for elemento in lista_1: 
    print(elemento, type(elemento))

#Concatenar fstring agregar una f antes de las comillas 

print(f"\nHola {nombre}")







