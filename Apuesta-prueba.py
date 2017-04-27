from functools import reduce
jug1 = 0
jug2 = 0
jug3 = 0
lista = [[100,10,50],[1,30,1500],[200,5,30],["G","P","G"],["P","G","P"],["P","G","G"]]

n = (len(lista))
listaApuestas = lista[0:n/2]
listaGanadores = lista[n/2:]

for i in range(n/2):
    for j in range(n/2):
        if (listaGanadores[i][j] == "G"):
            "jug"+(i+1) = jug1 + listaApuestas[i][j]
        else:
            jug1 = jug1 - listaApuestas[i][j]
        print jug1
