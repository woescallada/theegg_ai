'''Programa que diga si una palabra dada es palíndromo'''
pal = input (str("Escribe una palabra: "))
if str(pal) == str(pal)[::-1]:
    print ("La palabra ", pal, " es un palíndromo.")
else:
    print ("La palabra ", pal, " no es un palíndromo.")