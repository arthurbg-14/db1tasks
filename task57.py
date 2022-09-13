class Ponto3D:
    def __init__(self, num1, num2, num3) -> None:
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def __str__(self):
         return f"({self.num1}, {self.num2}, {self.num3})"


ponto = Ponto3D(1, 2, 3)
print(ponto)