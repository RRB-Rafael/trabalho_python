#Escreva um programa que solicite dois números ao usuário e exiba: a soma dos dois números, a subtração do primeiro número pelo segundo, a multiplicação dos dois números e a divisão do primeiro número pelo segundo.
num1 = int(input("Insira o primeiro num: "))
num2 = int(input("Insira o segundo num: "))
soma = num1 + num2
sub = num1-num2
mult = num1*num2
div= num1 / num2
print(f"O resultado da soma destes números é: {soma}")
print(f"O resultado da subtração destes números é: {sub}")
print(f"O resultado da multiplicação destes números é: {mult}")
print(f"O resultado da divisão destes números é: {div}")

print("FIM-------------------------------------")