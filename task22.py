a = int(input("Digite o valor  de A\n"))
b = int(input("Digite o valor  de B\n"))
c = int(input("Digite o valor  de C\n"))

D = (b**2 - 4*a*c)
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)

print(f"As raizes são {x1} e {x2}")