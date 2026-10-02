#Lista 1 - MC102

#Exercício 1 - Trocar valores
x = int(input("insira um valor x: "))
y = int(input("insira um valor y: "))

x, y = y, x

print(x, y)

#Exercício 2 - área do triangulo
a, b, c = map(int, input("Insira 3 valores para um triangulo a b c: ").split())
s = (a + b + c) / 2
triangulo = ""

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

if a == b and b == c:
    triangulo = "Equilatero"
elif a != b and b != c:
    triangulo = "Escaleno"
else:
    triangulo = "Isosceles"
print("Esse triangulo é", triangulo, "e tem area de:", area)

#Exercício 3 - Celcius para Farenheint
tipo = str(input("insira C ou F: "))
temperatura = float(input("insira uma temperatura: "))

if tipo == "C":
    temperatura = (temperatura * 9/5) + 32
    print(temperatura, "°F")
elif tipo == "F":
    temperatura = (temperatura - 32) * 5/9
    print(temperatura, "°C")
else:
    print("Você não inseriu C ou F para o tipo")