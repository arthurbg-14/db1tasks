class Estudante:
    def __init__(self, id, nome="", classe="") -> None:
        self.id = id
        self.nome = nome
        self.classe = classe
    def mostrar(self):
        print(f"Id:{self.id}")
        if(self.nome):
            print(f"Nome:{self.nome}")
        if(self.classe):
            print(f"Classe:{self.classe}")

estudante = Estudante(10, "COCONUTBOY", "3")
estudante.mostrar()

print(type(estudante))
print(estudante.__dict__)