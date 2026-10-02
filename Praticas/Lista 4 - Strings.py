#MC102 - Lista 4
#exercício 1 - Inverter a string
msg = "Tangamandapio"
print(msg[::-1])

#exercício 2 - Remover espaços
msg =  "Out\tof the night that\tcovers me"
print(msg.replace(" ", "").replace("\t", ""))

#exercício 3 - Caracteres não comuns
str_1 = list("ANDERSON")
str_2 = list("CALCINHA")

for i in str_1:
    for j in str_2:
        if i in str_2:
            str_2.remove(i)
str_2 = "".join(str_2)
print(str_2)

#exercício 4 - Anagrama
str_1 = ("SILAS")
str_2 = ("SALIS")

if sorted(str_1) == sorted(str_2):
    print("Anagramanderson!")
else:
    print("Não Anagramanderson!")