def trianguloDePascal(n):
    list = []
    for i in range(n):
        list.append([])
        list[i].append(1)
        for m in range(1, i):
            list[i].append(list[i - 1][m - 1] + list[i - 1][m])
        if(n != 0):
            list[i].append(1)
    list[0] = [1]
    for i in list:
        print(i)
trianguloDePascal(10)