#checando se o programa vai continuar rodando
loop = True
while(loop==True):
    #Interface simples
    print("Escolha uma das opcoes abaixo: ")
    print("1 - Soma\n2 - Subtracao\n3 - Divisao\n4 - Multiplicacao\n5 - Sair")


    #input das opções
    escolha = int(input("Escolha um opcao: "))
    
    #checar se a escolha é válida
    while escolha<1 or escolha>5:
        print("Escolha uma opcao valida")
        print("Escolha uma das opcoes abaixo: ")
        print("1 - Soma\n2 - Subtracao\n3 - Divisao\n4 - Multiplicacao\n5 - Sair")
        escolha = int(input("escolha uma opcao: "))

    #se a escolha não for "Sair" continuar rodando  
    if escolha >=1 and escolha<5:
        try:
            n1 = float(input("Primeiro numero: "))
            n2 = float(input("Segundo numero: "))
        except ValueError:
            print("Numero invalido. Insira apenas numeros.")
            continue


    #Definindo Opções
    #soma
    def soma():
        print(f'A soma {n1} + {n2} = {n1+n2:.3f}')

    #subtração
    def subtracao():
        print(f"A subtracao {n1} - {n2} = {n1-n2:.3f} ")

    #Divisão
    def divisao():
        print(f"A divisao {n1}/{n2} = {n1/n2:.3f} ")

    #Multiplicação
    def multiplicacao():
        print(f"A multiplicacao {n1} * {n2} = {n1*n2:.3f} ")
      

    #Switch Case
    if escolha == 1:
        soma()
    elif escolha == 2:
        subtracao()
    elif escolha == 3:
        divisao()
    elif escolha == 4:
        multiplicacao()
    else:
        loop = False
