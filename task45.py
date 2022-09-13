def contarLetras(str):
    maiusculas = 0
    minusculas = 0
    for i in str:
        if(i==i.lower()):
            minusculas+=1
        elif(i==i.upper()):
            maiusculas+=1
    printarLetras(maiusculas,minusculas)
def printarLetras(mai,min):
    print(f"Letras maisculas: {mai}\n")
    print(f"Letras minusculas: {min}\n")
contarLetras("LaSaNhA") 