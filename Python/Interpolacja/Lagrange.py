from sympy import *

wenz = [[-1,3],[0,1],[1,2],[2,-6]]

x = symbols('x')
n = len(wenz) - 1

lambd_up =[]
lambd_down = []

for i in range(len(wenz)):
    fup = 1
    fdown = 1
    for k in range(len(wenz)):
        if i != k:
            fup *= x - wenz[k][0]
            fdown = (wenz[i][0] - wenz[k][0]) *fdown
    
    lambd_up.append(fup)
    lambd_down.append(fdown)

funk = 0
for iter in range(len(wenz)):
    funk += wenz[iter][1]* (lambd_up[iter]/lambd_down[iter])

wyn = simplify(funk)
pretty_print(wyn)


        