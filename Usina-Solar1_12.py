def cadastrar_cliente(bancoDeDados):
    
    cliente = input('Nome do cliente: ')

    endereco = input('Endereço: ')

    numero = input('Número: ')

    resp_tec = input('Responsál técnico: ')
    

    while True:  # Tratamento de erro

        try:

            cons_anual = float(input('Informe o consumo anual em (Kwh): '))

        except(ValueError, TypeError):

            print('ERRO !! Digite números com (.) ou inteiro apenas.')

        else:

            break

    cons_mensal_med = round(cons_anual / 12, 2)  # arredonda 2 casas decimais

    print('Média consumo mensal:', cons_mensal_med, 'Kwh.')

    cons_dia = round(cons_mensal_med / 24, 2)  # arredonda 2 casas decimais

    print('Média consumo diário:', cons_dia, 'Kwh.')

    while True:  # Tratamento de erro

        try:

            h_sol_pleno = float(input('Informe as horas de sol pleno: '))

        except(ValueError, TypeError):

            print('ERRO !! Digite números com (.) ou inteiro apenas.')

        else:

            break

    pot_instal = round(cons_dia / h_sol_pleno, 2)

    print('Potência a ser instalada:', pot_instal, 'Kwp.')

    bancoHandler = open(bancoDeDados, 'a')

    bancoHandler.write(cliente + '\t' + endereco + '\t' + numero + '\t' + resp_tec + '\t' + str(cons_anual) + '\t' +
                       str(cons_mensal_med) + '\t' + str(cons_dia) + '\t' + str(h_sol_pleno) + '\t' + str(pot_instal) + '\n')

    bancoHandler.close()


def consulta_cadastro(bancoDeDados):
    
    valido=0 
    
    while(valido==0):
        
        try:
            opcao = int(input('  Que tipo de consulta deseja fazer?\n 1) Completa.\n 2) Unica,\n >'))
            
            valido= 1

        except:

            print("\nDigite uma opção válida\n")


    if (opcao == 1):

        with open(bancoDeDados) as bancoHandler:

            for linha in bancoHandler:
                
                print('*' * 40)

                linha = linha.strip('\n').split('\t')

                print('Cliente: ' + linha[0])

                print('Endereço: ' + linha[1])

                print('Número: ' + linha[2])

                print('Responsável técnico: ' + linha[3])

                print('Consumo anual: ' + linha[4], 'KWh.')

                print('Consumo mensal médio: ' + linha[5], 'KWh')

                print('Consumo diário médio: ' + linha[6], 'KWh.')

                print('Horas de sol pleno: ' + linha[7])

                print('Potência instalada: ' + linha[8], 'KWp.')

                print('*' * 40)

    if (opcao == 2):

        cliente = str(input('Cliente: '))
        achou=0

        with open(bancoDeDados) as bancoHandler:

            for linha in bancoHandler:

                if linha.find(cliente) != -1:
                    
                    print('=' * 40)

                    linha = linha.strip('\n').split('\t')

                    print('Cliente: ' + linha[0])

                    print('Endereço: ' + linha[1])

                    print('Número: ' + linha[2])

                    print('Responsável técnico: ' + linha[3])

                    print('Consumo anual: ' + linha[4], 'KWh.')

                    print('Consumo mensal médio: ' + linha[5], 'KWh.')

                    print('Consumo diário médio: ' + linha[6], 'KWh.')

                    print('Horas de sol pleno: ' + linha[7])

                    print('Potência instalada: ' + linha[8], 'KWp.')

                    print('=' * 40)

                    achou= 1

            if (achou!=1):

                print("\n!!!Cliente não cadastrado!!!\n")


def main():
    
    bancoDeDados = 'banco_de_dados.txt'

    while True:

        print('*' * 40)

        print('     Dimensionamento sistema solar')

        print('*' * 40)

        print('-' * 40)

        print('        Escolha uma das opções:\n 1) Cadastrar cliente,\n 2) Consultar cadastro.\n 3) Sair')

        print('-' * 40)

        op = 1000

        while op != 1 or op != 2 or op != 3:  # Tratamento de erro

            try:

                op = int(input(' Opção: '))

                if op == 1 or op == 2 or op == 3:
                    
                    break

                print('ERRO !! Digite apenas 1, 2, ou 3.')

            except:

                print('ERRO !! Digite apenas 1, 2, ou 3.')

        print('-' * 40)

        if op == 1:
            
            cadastrar_cliente(bancoDeDados)

        if op == 2:
            
            consulta_cadastro(bancoDeDados)

        if op == 3:

            sair = int(input('Deseja realmente sair?\n1)Sim.\n2)Não.'))

            if sair == 1:
                
                print('Até o próximo cliente !!')

                break

            if sair == 2:
                
                False


main()
