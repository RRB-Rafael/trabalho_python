# Crie um programa que receba dois números inteiros e exiba: o quociente inteiro da divisão (usando //) e o resto da
#divisão (usando %).
num1 = int(input("Insira o primeiro num: "))
num2 = int(input("Insira o segundo num: "))
div = num1 // num2
rest = num1%num2
print(f"O resultado da divisão é: {div}")
print(f"O que sobra é: {rest}")

print("FIM-------------------------------------")