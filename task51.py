
class Conversor:
    def __init__(self):
        self.text = ""
    def romano(self, texto):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        while texto:
            div = texto // num[i]
            texto %= num[i]
            while div:
                self.text += sym[i]
                div -= 1
            i -= 1
    def inteiro(self, texto):
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        i = 0
        resultado = 0   
        while texto:
            try:
                if sym[i]==texto[-1]:
                    resultado += num[i]
                    texto = texto[:-1]
                if sym[i]==(texto[-2]+texto[-1]):
                    resultado += num[i]
                    texto = texto[:-2]
            except:
                pass
            i += 1
            if i > 12:
                i = 0
        self.text  = resultado
    def printar(self):
        print(self.text)

script = Conversor()
script.romano(1806)
script.inteiro("MDCCCVI")
script.printar()