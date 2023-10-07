from sympy import *

x=symbols('x')

#Sprawdzanie czy funkcja ma przeciwne znaki w punktach a i b
f=lambda x:(x+1) * (x-1)**4

epsilon = 0.0001 #Margines błędu

def sieczne(a,b):
    #Sprawdzanie czy funkcja ma przeciwne znaki w punktach a i b
    if f(a)*f(b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    #Metoda włąściwa
    c=(a+b)/2
    x0 = a
    x1 = b
    x2=0
    iterations = 0
    while abs(f(x1))>epsilon:
        x2 = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        x0=x1
        x1=x2
        iterations += 1
    print("Wynik: "+str(x2))
    print("Liczba iteracji: "+str(iterations)+"\n")

sieczne(-1.5,-0.75)
sieczne(0.75,1.0)