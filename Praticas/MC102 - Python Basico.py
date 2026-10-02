'''
Valores das variaveis!!!
Temos varias variaveis!!!
Letras MAIUSCULAS e minusculas
armazenam variaveis diferentes
'''

pi = 3.141592
x, y, z = 3, 2, 1
X, Y, Z = True, 2.0, "Z"
a, b = 20, 15

print("Murilo", "RA113354213", "MC102", "2026", sep = " - ")
print(type(x), type(Z)) #esse 'type' significa o tipo
print(type(X), type(pi)) #temos int, str, bool e float

print(x, y, z, "...")
print("_" * 15)

'''
Trabalhando com operadores matematicos
'''
print(a + b) #Adição
print(a * b) #Multiplicação
print(a - b) #Subtração
print(a / b) #Divisão
print(a // b) #Divisão inteira
print(a ** b) #Potenciação
print(a % b) #Resto de uma divisão

'''
Trabalhando com operadores de comparação
'''

num1 = 5
num2 = 12

print(num1 == num2) #comparação de igualdade
print(num1 != num2) #comparação de desigualdade
print(num1 > num2) #maior que
print(num1 >= num2) #maior ou igual a
print(num1 <= num2) #menor ou igual a
print(num1 < num2) #menor que

'''
Trabalhando com operadores de lógica
'''

print(3 < 4 and 2 == 2) #True pois 3 é menor que 4 e 2 é igual a 2
print(5 != 5 and 6 > 3) #False pois 5 não é diferente de 5

print(10 == 10 or 20 < 12) #True pois 10 é igual a 10
print(3.0 != 3 or 4 > 5) #False pois todos são falsos

'''
Entrada de dados
'''

valor = (input("insira um valor qualquer:"))
print(valor, type(valor))