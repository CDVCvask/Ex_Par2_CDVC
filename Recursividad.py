def Menu():
    print("Menu de recursividad")
    print("1.Calcular el MCD")
    print("2.Crear una cadena repetida N veces ")
    print("3.Contar cuantas veces aparece una letra en una cadena")
    print("4.Convertir un número decimal a binario")
    print("5.Calcular cuantos digitos tiene un número")
    print("6.Salir")
allow = False
def Repeat(word,num,cont,final):
    print(cont)
    print(final)
    if cont == num:
        return
    else:
        cont = cont+1
        return f"{word}{Repeat(word,num,cont)}"
def Find(Parts,Look,cont):
    if Parts == []:
        return cont
    else:
        if Parts[0].lower() == Look.lower():
            cont = cont + 1
            return Find(Parts[1:],Look,cont)
        else:
            return Find(Parts[1:],Look,cont)
def Bin(num,bin,cont):
    if cont == num:
        return bin
    else:
        if bin == 1:
            bin = 0
        else:
            bin = 1
        return f"{bin}{Bin(num,bin,cont+1)}"
def Digits(Num,cont,check,repeat):
    print(f"{num},{check},{cont},{repeat}")
    if check <= 1:
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
            num = int(input("Cuantas veces se va a repetir? "))
            if num <= 0 or num >1000:
                print("Cantidad invalida")
            else:
                print(Repeat(word,num,0,""))
        case 3:
            word = input("Ingrese la cadena: ")
            look = input("Ingrese la letra a encontrar: ")
            parts = list(word)
            total = Find(parts,look,0)
            print(f"En la cadena {word} la letra {look} se repite {total} veces")
        case 4:
            num = int(input("Ingrese un número: "))
            print(Bin(num,0,0))
        case 5:
            num = int(input("Ingrese un número: "))
            total = Digits(num,1,2,0)
            print(f"La cantidad {num} tiene {total} digitos")
        case 6:
            list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
            print(list)
            print("Gracias por utilizar el programa")
            break