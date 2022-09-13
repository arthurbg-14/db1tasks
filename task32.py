lista = ['abc','xyz','aba','1221']
soma = 0

for i in lista:
    if(len(i)>2):
        if(i[0]==i[-1]):
            soma+=1

print(soma)