number = input("Digite um numero correspondente a um dia da semana\n")
dias = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta"]
number = int(number)
print(f"O dia correspondente é {dias[(number-1)]}")