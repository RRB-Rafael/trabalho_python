#Crie um programa que peça o nome de um aluno, suas três notas em variáveis separadas, e calcule a média dessas
#notas. Exiba uma mensagem como: "[Nome], sua média é [média]."

nome= input("Qual o seu nome? ")
n1= int(input("E qual foi sua primeira nota? "))
n2= int(input("E a segunda? "))
n3= int(input("E a terceira? "))

nf= (n1+n2+n3)/3

print(f"{nome}, sua média final é {nf}")