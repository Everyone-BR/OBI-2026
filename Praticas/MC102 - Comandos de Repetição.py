n = int(input())

for i in range(1, n+1):
  if n % i == 0:
    print(i)

n = int(input())
divisores = 0

for i in range(1, n+1):
  if n % i == 0:
    divisores = divisores + 1
print(divisores)

n = int(input())
divisores = 0

for i in range(1, n+1):
  if n % i == 0:
    divisores = divisores + 1

if divisores == 2:
  print("Primo")
else:
  print("Composto")