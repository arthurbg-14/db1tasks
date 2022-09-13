numeros = []

numeros.append(int(input("Digite o preço de um produto\n")))
numeros.append(int(input("Digite o preço de um produto\n")))
numeros.append(int(input("Digite o preço de um produto\n")))

numeros.sort()

print(f"Você deve comprar o produto que custa {numeros[0]}")