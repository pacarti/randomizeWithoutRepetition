def randCountDiffers(randCount, lista):
    for i in range(len(lista)):
        if randCount == lista[i]:
            return False
    return True        


def randomizeCount(lista):
    i = 0
    while i < 5:
        randCount = random.randint(1,10)
        if randCountDiffers(randCount, lista) == True:
            lista.append(randCount)
            i = i+1
        else:
            continue    
    return lista    


import random
lista = []

print(randomizeCount(lista))
