jug1 = 0
jug2 = 0
jug3 = 0
lista = [[100,10,50],[1,30,1500],[200,5,30],["G","P","G"],["P","G","P"],["P","G","G"]]

filtro = filter(lambda x: x, lista[3])
filtroo = filter(lambda x: x, lista[4])
filtrooo = filter(lambda x: x, lista[5])
f1 = list(map(lambda x: x, lista[0]))
f2 = list(map(lambda y: y, lista[1]))
f3 = list(map(lambda z: z, lista[2]))

if (filtro[0] == "G"):
    jug1 = jug1 + f1[0]
else:
    jug1 = jug1 - f1[0]

if (filtro[1] =="G"):
    jug2 = jug2 + f1[1]
else:
    jug2 = jug2 - f1[1]
    
if (filtro[2] == "G"):
    jug3 = jug3 + f1[2]
else:
    jug3 = jug3 - f1[2]



if (filtroo[0] == "G"):
    jug1 = jug1 + f2[0]
else:
    jug1 = jug1 - f2[0]

if (filtroo[1] =="G"):
    jug2 = jug2 + f2[1]
else:
    jug2 = jug2 - f2[1]

if (filtroo[2] == "G"):
    jug3 = jug3 + f2[2]
else:
    jug3 = jug3 - f2[2]



if (filtrooo[0] == "G"):
    jug1 = jug1 + f3[0]
else:
    jug1 = jug1 - f3[0]

if (filtrooo[1] == "G"):
    jug2 = jug2 + f3[1]
else:
    jug2 = jug2 - f3[1]

if (filtrooo[2] == "G"):
    jug3 = jug3 + f3[2]
else:
    jug3 = jug3 - f3[2]

puntaje = [jug1, jug2, jug3]
print puntaje

f = lambda a,b: a if (a > b) else b
print "Quien gano mas dinero: ",(reduce(f, puntaje))

g = lambda c,d: c if (c < d) else d
print "Quien perdio mas dinero: ",(reduce(g, puntaje))
