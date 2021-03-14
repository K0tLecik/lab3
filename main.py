import sys as system
import math
import random

# Zad 1

print("\nZadanie 1: \n")

A = [1 - i for i in range(11) if i>0]
print(A)

B = [pow(4,i) for i in range(8)]
print(B)

C = [B[i] for i in range(len(B)) if B[i]%2==0]
print(C)

#Zad 2

print("\nZadanie 2: \n")
lista1 = []
for i in range(10):
    lista1.append(random.randrange(1,100))
lista2 = [lista1[i] for i in range(len(lista1)) if lista1[i]%2==0]
print(lista2)

#Zad 3

print("\nZadanie 3: \n")

produkty = {'jajka' : 'sztuki', 'mleko' : 'litry', 'ziemniaki' : 'kilogramy', 'mango' : 'sztuki', 'batony' : 'sztuki'}
sztuki1 = [key for key, value in produkty.items() if value == 'sztuki']
print(sztuki1)

#Zad 4

print("\nZadanie 4: \n")

def czy_prostokatny(a, b, c):
    if(pow(a,2) + pow(b,2) == pow(c,2)):
        print("Jest prostokątny\n")
    else:
        print("Nie jest prostokątny\n")

czy_prostokatny(5,7,20)

#Zad 5

print("\nZadanie 5: \n")

def pole_trapezu(a=5, b=10, h=15):
    return((a+b)*h/2)

print(pole_trapezu())

#Zad 6

print("\nZadanie 6: \n")

ciag = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def iloczyn_ciagu(a=1, b=4, ile=10):
    wynik = []
    for a in range(a - 1, ile + a - 1):
        wynik.append(ciag[a]*b)
    return wynik

print(iloczyn_ciagu())

#Zad 7

print("\nZadanie 7: \n")

def iloczyn_ciagu2(b, *x):
    wynik = []
    for a in x:
        wynik.append(a*b)
    return wynik

print("Pierwszy argument to b, potem elementy ciągu\n", iloczyn_ciagu2(4,5,7,12))

#Zad 8

print("\nZadanie 8: \n")

def lista_zakupow(**zakupy):
    suma = 0
    for key, value in zakupy.items():
        suma = suma + value
    print("Ilość produktów:", len(zakupy), "\nWartość produktów:", suma)

lista_zakupow(jajka = 7.20, mleko = 2.99, ziemniaki = 5.50, mango = 13.49, batony = 6.37)

from Ciagi import *

print(Ca.roznica(ciag))
