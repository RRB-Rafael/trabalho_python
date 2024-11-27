#Solicite ao usuário um número inteiro e verifique se ele é par ou ímpar. Exiba a mensagem correspondente

num= int(input("Insira um número: "))

if num % 2 == 0:
    print("É par :D")
else:
    print("É ímpar :(")