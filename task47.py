def isPrimo(int):
    divisores = 0
    for i in range(int):
        if(int%(i+1)==0):
            divisores+=1
    if(divisores==2):
        return True
    else:
        return False

print(isPrimo(4))