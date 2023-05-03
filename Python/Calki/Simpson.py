from sympy import *

x = symbols('x') #declaring symbols of your function

#declaring your function. '**' stands for '^'
f = x**2

def simpson(a,b):
    wyn = ((b-a)/6) * (f.subs(x,a) + f.subs(x,b) + 4 * f.subs(x,(a+b)/2))
    print("Wynik to :"+str(wyn))
    psi = max(f.subs(x,a),f.subs(x,b))
    err = (1.0/90.0)* pow((b-a)/2,5) * diff(f,x,4).subs(x,psi)
    print("Błąd to :"+str(err))

simpson(-1,1)