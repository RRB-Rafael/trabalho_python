#Peça ao usuário o preço de um produto e a porcentagem de desconto. Calcule e exiba o valor do desconto e o preço final do produto.
P = int(input("Qual o valor do produto? "))
D= int(input("Qual a porcentagem do desconto? "))

V = (P*D)/100
VT= P-V

print(f"Inluindo o desconto, o valor do produto será: {VT}")

print("FIM-------------------------------------")