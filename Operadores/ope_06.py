#Solicite dois números ao usuário e troque os valores dessas variáveis usando apenas operadores matemáticos.
#Exemplo: Se o usuário informar os números 10 e 20, ao final do programa, o valor do primeiro número deve ser 20,
#e o do segundo, 10.

A= int(input("Informe o primeiro valor: "))
B= int(input("Informe o segundo valor: "))

A= A+B
B= A-B
A= A-B
print(f"Primeiro núm: {A}")
print(f"Segundo núm: {B}")

print("FIM-------------------------------------")