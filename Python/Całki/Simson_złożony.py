from sympy import *

x = symbols('x')

f=x**2

def complex_simpson(a, b, n):
    if(n%2!=0):
        print("Liczba przedziałów musi być parzysta")
        return


    h=(b-a)/n

    wyn = f.subs(x,a)+f.subs(x,b)

    xk=a+h
    for i in range(1,n):
        if(i%2==0):
            wyn+=2*f.subs(x,xk)
        else:
            wyn+=4*f.subs(x,xk)
        xk+=h
    wyn= ((1.0/3.0)*h)*wyn #wynik ze wzoru

    print("Wynik to: "+str(wyn))

    e=(a+b)/2 # wybieramy e do liczenia błędu

    r = ((((b-a)*pow(h,4))/180.0)*diff(f,x,4).subs(x,e))*(-1.0)

    print("Błąd to: "+str(r))

    print("Wartość całki to: "+str(wyn+r))

complex_simpson(-1,1,4)