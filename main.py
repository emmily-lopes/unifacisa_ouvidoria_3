from bc_ouvidoria import *

conn = abrirBancoDados('localhost','root','123456789','reclamacoes')

opcao = 4

print('Bem-vindo a Ouvidoria Da Unifacisa!')

print()

while opcao != 6:
    print('1) Listagem das Reclamações: ')
    print('2) Adicionar uma nova Reclamação: ')
    print('3) Quantidades de Reclamações: ')
    print('4) Pesquisa rápida (digite o código): ')
    print('5) Excluir ')
    print('6) Sair ')
    print()

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print()
        sql = "SELECT * FROM reclamacao"
        resultado = listarBancoDados(conn, sql)

        if len(resultado) == 0:
            print('Não existe reclamações criadas no momento')
            print()
        else:
            for elemento in resultado:
                print('Código:', elemento[0], '\nReclamação:',elemento[1], '\nNome:',elemento[2] )
                print()

    elif opcao == 2:
        print()
        print('Inserir nova reclamação')
        print()
        nome = input('digite seu nome ')
        reclamacao = input('digite a reclamaçao ')
        print()
        sql = "INSERT INTO reclamacao (nome, reclamacao) VALUES (%s, %s)"
        dados = (nome, reclamacao)

        insertNoBancoDados(conn, sql, dados)
        sql = 'select max(codigo) from reclamacao'
        codigo = listarBancoDados(conn, sql)

        print('Reclamação cadastrada com sucesso, seu código é: ', codigo[0][0])
        print()



    elif opcao == 3:
        print()
        sql = 'select count(*) from reclamacao'
        quantidade = quantidadeDeLinhas(conn, sql)
        quantidade = quantidade[0]
        print('A quantidade de reclamações é:', quantidade)
        print()

    elif opcao == 4:
        print()
        codigo = int(input('Digite o código da reclamação que deseja pesquisar: '))

        codigo = str(codigo)
        sql = 'select reclamacao, nome from reclamacao where codigo =' + codigo
        resultado = listarBancoDados(conn, sql)
        print()
        print('O resultado da sua pesquisa é: ', resultado[0][0], resultado[0][1])
        print()
        for elemento in resultado:
            print(elemento)
            print()

    elif opcao == 5:
        print()
        codigo = int(input('Digite o código que queres excluir: '))
        print()
        codigo = str(codigo)
        sql = 'delete from reclamacao where codigo = %s'
        dados = (codigo,)
        resultado = excluirBancoDados(conn, sql, dados)
        if resultado == 0:
                print('Código não existente')
                print()
        else:
                print('Reclamação Excluída')
                print()

    elif opcao == 6:
        print()
        print('Obrigado por usar a ouvidoria da Unifacisa!')


    else:
        print()
        print('Opção inválida! Digite Novamente: ')
        print()