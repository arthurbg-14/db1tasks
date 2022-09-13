print("Organizações Tabajara calculadora de salario\n")
def calc():
    try:
        salario = input("Qual o salario atual\n")
        percent = input("Digite a porcentagem de aumento\n")
        salario = int(salario)
        percent = int(percent)
        print(f"O novo salario deve ser: {(salario+salario*percent/100)}\n")
        calc()
    except:
        print("ERROR ALGUEM ME DESCONFIGUROU")
        calc()
calc()