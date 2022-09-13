
def maiorNumero(list):
    list.sort(reverse=True)
    return list[0]
print(f"O maior numero é  {maiorNumero([1,232,543,32342,356,4,13,65,1,41,5,1,4])}")