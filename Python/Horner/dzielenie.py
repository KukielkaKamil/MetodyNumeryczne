from sympy import *


# Pobieranie danych od użytkownika
n = input("Podaj stopień wielomianu: ")
n = int(n)
polynimial = [0] * (n+1)
i = n
for x in range(n+1):
    if x == n:
        polynimial[n] = float(input("Podaj wyraz wolny: "))
    else:
        polynimial[x] = float(input("Podaj wpółczynnik "+str(i)+" stopnia: "))
        i = i-1
binomal = float(input("\nPodaj współczynnik dwumianu: "))

#Tworzenie tablicy wynikowej
out = [0]*(n+1)
out[0] = polynimial[0]
binom = [1,binomal]
for x in range(n):
    out[x+1] = binomal*out[x]+polynimial[x+1]

rest=out.pop(len(out)-1) # Przechowywanie reszty z dzielenia osobno
x = symbols('x')
print(Poly(polynimial,x).as_expr())
print(Poly(binom,x))
print(Poly(polynimial,x)/Poly(binom,x))
#Wypisywanie wyniku
print("\n")
print (str(Poly(polynimial,x).as_expr())+' : '+str(Poly(binom,x).as_expr())+" = "+str(Poly(out,x).as_expr()))
print("Reszta z dzielenia: "+str(rest))