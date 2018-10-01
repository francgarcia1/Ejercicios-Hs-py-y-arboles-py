def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])

def invertirlista(listainver):
    if len(listainver) == 1:
        return listainver[0]
    else:
        listainver.reverse()
    return listainver


def listasiguales(monda,mondb):
    if len(monda) != len(mondb):
        return ("DiferentesTamaños")
    else:
        for i in range(0,len(monda)):
            if(monda[i] != mondb[i]):
                return("Nosoniguales")
 
    return ("yies")

def ordenalista(listainver):
    if len(listainver) == 1:
        return listainver[0]
    else:
        listainver.sort()
    return listainver

def buscarlista(buscali,x):
    if len(buscali) == 0:
        return "noks"
    else:
        buscali.index(x)
    return "si"

def mayor(lista):
    if lista ==[]:
        return("error")
    elif len(lista) == 1:
        return(lista)
    lista_nueva = 0
    while lista != []:
        primero = lista[0]
        if lista_nueva > primero:
            lista_nueva = lista_nueva
        else:
            lista_nueva =primero
        lista = lista[1:]
    return(lista_nueva)
   
def pares(listapa):
    if listapa ==[]:
        return("error")
    pares = 0
    while lista != []:
      primero = lista[0]
        if primero%2==0:
           pares=pares+1 
        listapa = listapa[1:]
      
   return(pares)


      




