from sympy import *

x=symbols('x') #declaring symbols of your function

#declaring your function. '**' stands for '^'
f=lambda x:(x+1) * (x-1)**4

epsilon = 0.0001 #setting our error

def sieczne(a,b):
    #checking if function has oposite signs in points a and b
    if f(a)*f(b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    #function
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