# printing polynomial function
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


# Getting input from the user
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

#creating output array
out = [0]*(n+1)
out[0] = polynimial[0]

for x in range(n):
    out[x+1] = binomal*out[x]+polynimial[x+1]

rest=out.pop(len(out)-1) # storing the rest of the division separately

#printing output
print("\n")
bdm = 'x  '+str(abs(binomal)) if binomal < 0 else 'x - '+str(binomal)
print (getPolynomial(polynimial)+' : '+bdm+" = "+getPolynomial(out))
print("Reszta z dzielenia: "+str(rest))