def Menu():
    print("Menu de recursividad")
    print("1.Calcular el MCD")
    print("2.Crear una cadena repetida N veces ")
    print("3.Contar cuantas veces aparece una letra en una cadena")
    print("4.Convertir un número decimal a binario")
    print("5.Calcular cuantos digitos tiene un número")
    print("6.Salir")
allow = False
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            num_a = int(input("Ingrese el primer número:"))
        case 2:
            word = input("Ingrese la cadena que desea repetir: ")
        case 3:
            word = input("Ingrese la cadena: ")
        case 4:
            num = int(input("Ingrese un número: "))
        case 5:
            num = int(input("Ingrese un número: "))
        case 6:
            print("Gracias por utilizar el programa")
            break