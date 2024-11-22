#Crie um programa que peça o nome de um produto, sua quantidade e o preço unitário. Calcule e exiba o valor total da compra
NP = input("Qual o nome do produto? ")
Q= int(input("Quantos produtos são? "))
PU= int(input("Qual o preço deste produto? R$"))
PF= float(Q*PU)
print(f"O valor total da compra de {Q} {NP} é R${PF}")
