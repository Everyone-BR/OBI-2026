#Fase 2 OBI 2012 - Frequencia na Aula
N = int(input())
lista = []


for i in range(N):
    i = int(input())
    lista.append(i)

presentes = len(lista)

for i in lista:
    if lista.count(i) != 1:
        lista.remove(i)
        presentes -= 1
        
print(presentes)