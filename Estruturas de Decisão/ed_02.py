#. Peça ao usuário dois números e exiba o maior deles. Caso sejam iguais, exiba uma mensagem indicando que os números são iguais.

num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))

if num1==num2:
    print("Os dois números são iguais")
elif num1> num2:
    print(f"O {num1} é maior que o {num2}")
else:
    print(f"O {num2} é maior que o {num1}")
