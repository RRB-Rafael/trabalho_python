#Solicite ao usuário um número inteiro positivo e verifique se ele é um número primo. Exiba uma mensagem indicando se é primo ou não.
while True: 
    n=int(input("Digite um número: "))
    if n%2==0:
          print("É par")
    else:
          print('É impar')