def isPerfect(value):
    Divisores = divisores(value)
    if(value==somarLista(removeFromList(Divisores, value)) and value==int(somarLista(Divisores))):
        return True
    else:
        return False
def divisores(value):
    divisores = []
    for i in range(value):
        if(value%(i+1)==0):
            divisores.append(i+1)
    return divisores
def somarLista(list):
    soma = 0
    for i in list:
        soma+=i
    return soma
def removeFromList(list, char):
    for i  in list: 
        if(i==char):
            list.remove(char)   
    return list
print(isPerfect(6))