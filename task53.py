from argparse import ArgumentError
from ast import Str
from pickletools import stringnl_noescape


class String:
    def __init__(self) -> None:
        self.array = []
    def adicionar_string(self, string):
        self.array.append(string)
    def inverter_string(self, string):
        self.array.append(string[::-1])
    def mostrarArray(self):
        print(self.array)

string = String()
string.adicionar_string("Ola")
string.inverter_string("Mundo")
string.mostrarArray()