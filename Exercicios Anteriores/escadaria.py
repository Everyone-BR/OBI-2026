#Fase 3 OBI 2025 - Escadaria
n = int(input())
escadaria = list(map(int, input().split()))
esquerda = []
direita = []

for i in range(n - 1):
    if escadaria[i] != -1 and escadaria[i + 1] == -1:
        escadaria[i + 1] = escadaria[i] + 1
            
esquerda = escadaria

for i in range(n - 1, -1, -1):
    if escadaria[i] != -1 and escadaria[i - 1] == -1:
        escadaria[i - 1] = escadaria[i] + 1
        
direita = escadaria

escadaria = min(esquerda, direita)
print(*escadaria)