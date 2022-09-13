lista1 = [1,2,3]
lista2 = []
listas = [lista1,lista2]

for i in listas:
    try:
        i[0]
    except:
        print("a lista está vazia")