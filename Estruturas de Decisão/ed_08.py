#. Peça ao usuário três números e exiba o maior deles. Se os três forem iguais, exiba uma mensagem indicando que são iguais.

num1= int(input("Insira um número: "))
num2= int(input("Insira um número: "))
num3= int(input("Insira um número: "))

if num1==num2==num3:
    print("Todos os números são iguais.")
else:
    maior= max(num1, num2, num3)
    print(f"O maior número é o {maior}")