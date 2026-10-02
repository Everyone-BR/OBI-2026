#Fase 3 OBI 2017 - Postes
N = int(input())
postes = list(map(int, input().split()))
reforco = 0
substituidos = 0

for poste in postes:
    if poste < 50:
        substituidos += 1
    elif poste >= 50 and poste < 85:
        reforco += 1

print(substituidos, reforco)