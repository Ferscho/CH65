""" Este es un pograma de una calculadora sencilla """

#Definimos la clase calculadora 
def calculadora():
    print("Selecciona una operacion")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicación")
    print("4.-Divicion")

    escoger = input("escoge ente el 1-4")

    if escoger in ['1','2','3', '4']:
        num1 = float(input("Coloca el primer numero: "))
        num2 = float(input("Coloca el segundo numero"))
        if escoger == 1:
            print (num1 + num2)
        elif escoger == 2:
            print(num1 - num2)
        elif escoger ==3:
            print(num1*num2)
        elif escoger == 4:
            if num2 !=0:
                print(num1/num2)
            else:
                print("Error: Divicion es cero")


calculadora()

    
    


    
    