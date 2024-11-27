#Crie um programa que peça ao usuário uma nota de 0 a 10. Verifique se a nota está no intervalo válido. Caso
#contrário, exiba uma mensagem de erro.

nota= int(input("Digite uma nota de 0 a 10: "))

if nota<0 or nota>10:
    print("Irmão, eu pedi uma nota entre 0 e 10.")
else: 
    print("boa")