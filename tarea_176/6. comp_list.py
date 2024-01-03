'''Programa que compare dos listas y encuentre si hay algún valor coincidente'''
l1 = []
n1= int(input("Introduce el número de elementos de la primera lista: "))
for i1 in range (0,n1):
    element = int (input())
    l1.append(element)

l2 = []
n2= int(input("Introduce el número de elementos de la segunda lista: "))
for i2 in range (0,n2):
    element = int (input())
    l2.append(element)

coincidentes = []

for i in l1:
    if i in l2:
        coincidentes.append(i)
if coincidentes == []:
    print ("No hay elementos coincidentes")    
else:
    print ("Los elementos coincidentes son los siguientes: ", coincidentes)        