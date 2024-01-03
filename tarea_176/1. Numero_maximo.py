'''Programa que diga el máximo de 3 números dados'''
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

if n1 > n2 and n1 > n3 :
    print ("El máximo es: ",n1)
elif n2 > n1 and n2 > n3:
    print ("El máximo es: ",n2)
elif n3 > n1 and n3 > n2:
    print ("El máximo es: ",n3)
else:
    print("No se ha podido establecer el máximo")