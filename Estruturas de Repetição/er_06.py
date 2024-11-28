#. Crie um programa que solicite números ao usuário até que ele digite 0. Ao final, exiba a soma de todos os números digitados.

soma= 0 

while True: 
    num=int(input("Digite um número: "))
    if num==0:
            break
    soma+=num

print(f"A soma dos números digitados é: {soma}")