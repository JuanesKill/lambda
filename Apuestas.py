jug1 = 0
jug2 = 0
jug3 = 0
lista = [[100,10,50],[1,30,1500],[200,5,30],["G","P","G"],["P","G","P"],["P","G","G"]]
lista2 =[0,0,0]
lista3=[0,1,2]
f4= filter(lambda x:x, lista[0: int((len(lista)/2))])
f5= filter(lambda x:x, lista[int((len(lista)/2)):(len(lista)-1)])
#print f5[0][0]
for x in lista3:
    for y in lista3:
        print f5[x][y]
        print x,y
        print lista2
        if (f5[x][y] == "G"):
            lista2[y] = lista2[y] + f4[x][y]
        else:
            lista2[y] = lista2[y] - f4[x][y]

print lista2


f = lambda a,b: a if (a > b) else b
print "Quien gano mas dinero: ",(reduce(f, lista2))

g = lambda c,d: c if (c < d) else d
print "Quien perdio mas dinero: ",(reduce(g, lista2))
print list(f4)
print list(f5)

