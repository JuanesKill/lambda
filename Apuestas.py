jug=[0,0,0]

lista = [[2,20,15],[4,5,12],[6,0,4],["G","P","G"],["P","G","P"],["P","G","G"]]

apuestas= filter(lambda x:x, lista[0: int((len(lista)/2))])
resultados= filter(lambda x:x, lista[int((len(lista)/2)):(len(lista))])

def filtrar(resul,n,k):
    if n<len(jug):
        if(resul[n]=="G"):
            jug[n]=jug[n]+apuestas[k][n]
        else:
            jug[n]=jug[n]-apuestas[k][n]
        filtrar(resul,n+1,k)
        
def operar(x):
    if x<len(jug):
        filtrar(resultados[x],0,x)
        operar(x+1)
operar(0)

puntaje = [jug[0], jug[1], jug[2]]
print puntaje

gano = lambda a,b: a if (a > b) else b
print "Quien gano mas dinero: ",(reduce(gano, puntaje))

perdio = lambda c,d: c if (c < d) else d
print "Quien perdio mas dinero: ",(reduce(perdio, puntaje))
