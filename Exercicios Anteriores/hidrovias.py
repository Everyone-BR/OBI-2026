#Fase 3 OBI 2025 - Rodovias e Hidrovias
N, M, K = map(int, input().split())
pai = list(range(N + 1))

def find(x):
    while pai[x] != x:
        x = pai[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        pai[b] = a
        return True
    return False

conexoes = []

for _ in range(M):
    a, b, t = map(int, input().split())
    conexoes.append((a, b, t))

for a, b, t in conexoes:
    if t == 1:
        if not union(a, b):
            print("N")
            exit()

removidas = 0

for a, b, t in conexoes:
    if t == 2:
        if not union(a, b):
            removidas += 1

if removidas <= K:
    print("S")
else:
    print("N")