import datetime

data = input('Digite um data no formato  dd/mm/aaaa\n')
lista = data.split("/")

try:
    newDate = datetime.datetime(int(lista[2]),int(lista[1]),int(lista[0]))
    print("Data valida")
except:
    print("DATA INVALIDAAA")