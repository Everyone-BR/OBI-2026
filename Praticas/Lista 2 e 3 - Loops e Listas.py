#MC102 - Lista 2 e 3
#Exercício 1 - verificação de ordem de lista

n = int(input())
lista = []

for i in range(n):
    lista.append(int(input()))

if lista == sorted(lista):
    print(lista, sorted(lista))
    print("A lista está em ordem")
else:
    print(lista, sorted(lista))
    print("A lista não está em ordem")

#Exercício 2 - diagonal de números

n = int(input())

for i in range(n):
    print(" " * int(i), i+1, sep = "")

#Exercício 3 - Intercessão entre duas listas

a = [1, 2, 3, 4, 5]
b = [2, 5, 7, 1, 9, 18]
intersecao = list(set(a) & set(b))

print(intersecao)

#MC102 - Lista 2 e 3
#Exercício 1 - verificação de ordem de lista

n = int(input())
lista = []

for i in range(n):
    lista.append(int(input()))

if lista == sorted(lista):
    print(lista, sorted(lista))
    print("A lista está em ordem")
else:
    print(lista, sorted(lista))
    print("A lista não está em ordem")

#Exercício 2 - diagonal de números

n = int(input())

for i in range(n):
    print(" " * int(i), i+1, sep = "")

#Exercício 3 - intersecao entre duas listas

a = [1, 2, 3, 4, 5]
b = [2, 5, 7, 1, 9, 18]
intersecao = list(set(a) & set(b))

print(intersecao)

#Exercício 4 - Multiplicação de numeros de listas

lista = list(map(int, input().split()))
c = int(input())
encontro = False

for i in lista:
    for j in lista:
        if i * j != c:
            encontro = False
        else:
            encontro = True
            print(i, j)
            break
    if encontro:
        break

if encontro == False:
    print("Numeros não encontrados no produto C")

#Exercicio 5 - Desvio padrão
n = list(map(int, input().split()))
media = (sum(n) / len(n))
somatoria = 0

for i in n:
    somatoria = somatoria + ((i - media) ** 2)

s = (somatoria / len(n)) ** 0.5

print(s)