from random import randint
numeroA = str(randint(100000000, 999999999))

novo_cpf = numeroA
contador = 10
soma = 0    
for i in range(19):
    if i > 8:
        i -=9

    soma += int(novo_cpf[i]) * contador


    contador -= 1
    if contador < 2:
        contador = 11
        digito = 11 - (soma % 11)

        if digito >= 9:
            digito = 0
        soma = 0
        novo_cpf += str(digito)

print(novo_cpf)


