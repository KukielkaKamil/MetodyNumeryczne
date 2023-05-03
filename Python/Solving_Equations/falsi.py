from sympy import *

x=symbols('x') #declaring symbols of your function

#declaring your function. '**' stands for '^'
f=lambda x:(x+1) * (x-1)**4

epsilon = 0.0001 #setting our error

def falsi(a,b):
    #checking if function has oposite signs in points a and b
    if f(a)*f(b) >= 0:
        print("funkcja nie przyjmuje różnych znaków na końcach przedziału")
        return
    #function
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
    
