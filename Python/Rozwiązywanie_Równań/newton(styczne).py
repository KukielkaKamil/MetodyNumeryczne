from sympy import *

x=symbols('x')

#Deklarowanie wzoru twojej funkcji. '**' oznacza potęgowanie
f=(x+1) * (x-1)**4

epsilon = 0.0001 #Margines błędu

x0=0
def newton(a,b):
    #Sprawdzanie czy funkcja ma przeciwne znaki w punktach a i b
    if f.subs(x,a)*f.subs(x,b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    #Metoda włąściwa
    #Szukanie punktu początkowego
    dx2=lambdify(x,diff(f,x,2))
    dx=lambdify(x,diff(f,x))
    if f.subs(x,a)*dx2(a)>0:
        x0=a
    else:
        x0=b
    iterations = 0
    while abs(f.subs(x,x0))>epsilon:
        xn= x0-(f.subs(x,x0)/dx(x0))
        x0=xn
        iterations+=1
    print("Wynik: "+str(x0))
    print("Liczba iteracji: "+str(iterations)+"\n")

newton(-1.5,-0.75)
newton(0.75,1.0)

