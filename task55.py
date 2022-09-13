
import math
import turtle

class Triangulo:
    def  __init__(self, angulos):
        self.angulos = angulos
    def somarLista(self, lista):
        soma = 0
        for i in lista:
            soma += i
        return soma
    def check_angulo(self):
        if(self.somarLista(self.angulos)==180):
            return True
        else:
            return False
    def sin(angle):
        return math.sin(angle*math.pi/180)
    def showTriangulo(self, ratio):
        if(self.check_angulo()):
            window =  turtle.Screen()
            turtle.bgcolor("black")
            turtle.fillcolor("white")
            turtle.begin_fill()
            turtle.pencolor("white")
            turtle.pendown()
            for i in range(3):
                if i==0:
                    turtle.forward(ratio)
                elif i==1:
                    turtle.forward(ratio*Triangulo.sin(self.angulos[2])/Triangulo.sin(self.angulos[1]))
                elif i==2:
                    turtle.forward(ratio*Triangulo.sin(self.angulos[0])/Triangulo.sin(self.angulos[1]))
                turtle.right(self.angulos[i]+180)
            turtle.end_fill()
            window.exitonclick()            
        else:
            print("Angulos Invalidos")

angles = []
angles.append(int(input("Digite um angulo\n")))
angles.append(int(input("Digite um angulo\n")))
angles.append(int(input("Digite um angulo\n")))
triangulo = Triangulo(angles).showTriangulo(100)