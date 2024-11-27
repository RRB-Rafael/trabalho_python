#Solicite ao usuário o valor do salário bruto e o valor de um desconto. Calcule e exiba o salário líquido

SB = int(input("Informe o valor do salário bruto:  "))
D = int(input("Informe o valor do desconto:  "))
XD= D * 100 / SB
SL= SB-XD
print(f"O valor final será de: R${SL}")