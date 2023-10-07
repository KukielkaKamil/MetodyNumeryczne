# Wypisywanie funkcji wielomianu
def getPolynomial(polyn):
    n=len(polyn)-1
    i = n
    polyn_string = ''
    for x in range(n+1):
        if x == n:
            polyn_string = polyn_string + str(abs(polyn[x]))
            break
        elif x == n-1:
            polyn_string = polyn_string+str(abs(polyn[x]))+'x'
        else:
            polyn_string = polyn_string+str(abs(polyn[x]))+'x^'+str(i)
        i = i-1
        polyn_string = polyn_string+' - ' if polyn[x] < 0 else polyn_string+' + '

    return polyn_string


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
x0 = float(input("\nPodaj dla jakiego x chcesz policzyć wartość wielomianu: "))

# MEtoda Hornera
temp = [0]*(n+1)
temp[0] = polynimial[0]

for x in range(n):
    temp[x+1] = x0*temp[x]+polynimial[x+1]

out=temp.pop(len(temp)-1) # Przechowywanie reszty z dzielenia osobno

#Wypisywanie wyniku
print("W punkcie x = "+str(x0)+" wielomian "+getPolynomial(polynimial)+" przyjmuje wartość: "+str(out))
