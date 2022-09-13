number = input("Digite um numero\n")

if int(number) > 1000:
    print("numero muito alto")
else:
    try:
        print("Unidades: "+number[2])
        print("Dezenas: "+number[1])
        print("Centenas: "+number[0])
    except:
        pass