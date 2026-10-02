#Fase 3 OBI 2022 - Caravanas
N = int(input())
pesos = []

for i in range(N):
    i = int(input())
    pesos.append(i)

media = sum(pesos) / len(pesos)

for i in pesos:
    peso = media - i
    print(int(peso))