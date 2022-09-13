letra = input("Digite uma letra\n")
def vogal (v):
    if v in ["a","e","i","o","u","A","E","I","O","U"]:
        return True
    else:
        return False 
if(vogal(letra)):
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} é uma consoante")