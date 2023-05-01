from sympy import *

x=symbols('x') #declaring symbols of your function

#declaring your function. '**' stands for '^'
f=lambda x:(x+1) * (x-1)**4

epsilon = 0.001 #setting our error

def bisection(a,b):
    iterations = 0
    if f(a)*f(b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    c=(a+b)/2
    while abs(f(c))>epsilon:
        if abs(f(c)) <= epsilon:
            break
        elif f(a)*f(c) < 0:
            b=c
        else:
            a=c
        c=(a+b)/2
        iterations+=1
    print("Wynik: "+str(c))
    print("Liczba iteracji: "+str(iterations)+"\n")

bisection(-1.5,-0.75)
bisection(0.75,1.0)