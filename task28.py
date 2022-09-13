
from tkinter import N


numeros=[]

numeros.append(int(input("Digite  um numero\n")))
numeros.append(int(input("Digite  um numero\n")))
numeros.append(int(input("Digite  um numero\n")))
numeros.append(int(input("Digite  um numero\n")))

media=0

for i in numeros:
    media+=i

media = media/len(numeros)

print("Média: "+str(media))