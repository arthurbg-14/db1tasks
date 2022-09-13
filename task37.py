
dict = {}

def add(value):
    dict[len(dict)] = value
    print(dict)

while(True):
    char = input("Digite um valor\n")
    add(char)
