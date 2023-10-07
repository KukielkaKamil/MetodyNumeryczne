from sympy import *

x = symbols('x') #declaring symbols of your function

#declaring your function. '**' stands for '^'
f = x**2

def simple_trapez(a,b):
    wyn = ((b-a)/2)*(f.subs(x,a)+f.subs(x,b))
    print("Wynik to :"+str(wyn))
    psi = max(f.subs(x,a),f.subs(x,b))
    err = (1.0/12.0) * pow(b-a,3) * diff(f,x,2).subs(x,psi)
    print("Błąd to :"+str(err))

simple_trapez(-1,1)