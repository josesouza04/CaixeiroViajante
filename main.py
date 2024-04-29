from mip import Model, xsum, minimize, CBC, OptimizationStatus, INTEGER
from itertools import product
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

c = 3
m = 4

C = range(c)
M = range(m)
A = [(i,j) for (i,j) in product(C,M)]
Custo = [[10,2,20,11],
     [12,7,9,20],
     [4,14,16,18]]

oferta = [15, 25, 10]
demanda = [5,15,15,15]

# declaracao do modelo
model = Model('Centros de Distribuicao', solver_name=CBC)

x = {(i,j): model.add_var(lb=0) for (i,j) in A}

# funcao objetivo: minimizacao do custo
model.objective = minimize(xsum(Custo[i][j] * x[i,j] for (i,j) in A))

for i in C:
    model += xsum(x[i,j] for j in M) == oferta[i]
   
for j in M:
    model += xsum(x[i,j] for i in C) == demanda[j]

status = model.optimize()

print("Custo Total: {:12.2f}.".format(model.objective_value))
