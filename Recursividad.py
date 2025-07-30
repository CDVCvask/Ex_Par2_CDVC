def Menu():
    print("Menu de recursividad")
    print("1.Calcular el MCD")
    print("2.Crear una cadena repetida N veces ")
    print("3.Contar cuantas veces aparece una letra en una cadena")
    print("4.Convertir un número decimal a binario")
    print("5.Calcular cuantos digitos tiene un número")
    print("6.Salir")
allow = False
def Repeat(word,num,cont):
    if cont == num:
        return cont
    else:
        cont = cont+1
        return Repeat(word,num,cont)
def Find(Parts,Look,cont):
    if Parts == []:
        return cont
    else:
        if Parts[0].lower() == Look.lower():
            cont = cont + 1
            return Find(Parts[1:],Look,cont)
        else:
            return Find(Parts[1:],Look,cont)
def Digits(Num,cont,check,repeat):
    if check <= 0:
        return repeat
    else:
        check = Num/cont
        cont = cont * 10
        repeat = repeat + 1
        return Digits(Num,cont,check,repeat)
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            num_a = int(input("Ingrese el primer número:"))
        case 2:
            word = input("Ingrese la cadena que desea repetir: ")
            num = int(input("Cuantas veces se va a repetir?"))
            if num <= 0 or num >1000:
                print("Cantidad invalida")
            else:
                print(Repeat(word,num,0))
        case 3:
            word = input("Ingrese la cadena: ")
            look = input("Ingrese la letra a encontrar: ")
            parts = list(word)
            total = Find(parts,look,0)
            print(f"En la cadena {word} la letra {look} se repite {total} veces")
        case 4:
            num = int(input("Ingrese un número: "))
            list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
            print(list)
        case 5:
            num = int(input("Ingrese un número: "))
            total = Digits(num,1,1,1)
            print(f"La cantidad {num} tiene {total} digitos")
        case 6:
            print("Gracias por utilizar el programa")
            break