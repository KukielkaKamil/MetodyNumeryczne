from sympy import *

x=symbols('x') 

#Deklarowanie wzoru twojej funkcji. '**' oznacza potęgowanie
f=lambda x:(x+1) * (x-1)**4

epsilon = 0.0001 #Margines błędu

def falsi(a,b):
    #Sprawdzanie czy funkcja ma przeciwne znaki w punktach a i b
    if f(a)*f(b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    #metoda właściwa
    xn = (a*f(b) - b*f(a))/(f(b)-f(a))
    iterations = 0
    while abs(f(xn))>epsilon:
        x1 = (xn*f(a) - a*f(xn))/(f(a) - f(xn))
        x2 = (xn*f(b) - b*f(xn))/(f(b)-f(xn))
        if f(a)*f(xn)<0:
            xn=x1
        else:
            xn=x2
        iterations += 1
    print("Wynik: "+str(xn))
    print("Liczba iteracji: "+str(iterations)+"\n")

falsi(-1.5,-0.75)
falsi(0.75,1.0)
    
