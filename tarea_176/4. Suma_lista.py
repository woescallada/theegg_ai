'''Programa que sume los valores de una lista'''
l1 = []
n= int(input("Introduce el número de elementos de la lista: "))
for i in range (0,n):
    element = int (input())
    l1.append(element)

suma_l1=sum(l1)
print ("La suma de los valores de: ", l1, " es: ", suma_l1)