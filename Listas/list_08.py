#Solicite ao usuário uma lista de palavras e, em seguida, peça uma palavra específica para buscar. Informe se a
#palavra está ou não presente na lista.

pals= input("Digite uma lista de palavras: ").split()

palsproc= input("Qual palavra deseja buscar? ")

if palsproc in pals: 
    print(palsproc)
else:
    print("Está palavra não existe no conjunto digitado")