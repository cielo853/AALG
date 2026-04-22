'''
pida el nombre del cliente,
cuantas manzanas comprara y un precio.
Muestra el nombre y el total a pagar.
'''
nom = input ("ingrese nombre:\n")
can = int (input("ingrese cantidad de manzanas:\n"))
pre = float(input("Ingrese precio:\n"))
tot = can * pre
print(f"{nom}compro s/{tot}")