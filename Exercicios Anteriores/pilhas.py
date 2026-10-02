#Fase 3 OBI 2022 - Pilhas de Moedas
N, K = map(int, input().split())
alturas = sorted(list(map(int, input().split())))
adicao = 0

while len(set(alturas)) != K:
    for i in range(N - 1):
        if alturas[i] == min(alturas):
            alturas[i] += 1
            adicao += 1
            if len(set(alturas)) == K:
                break

print(adicao)