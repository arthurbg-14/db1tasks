number = input("Digite um numero positivo ou negativo\n")
number = int(number)
if(number<0):
    print(f"O número {number} é negativo\n")
elif(number>0):
    print(f"O número {number} é positivo\n")
else:
    print("ERROR ALGUÉM ME DESCONFIGUROU\n")