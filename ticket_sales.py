opcao_1 = 'Vingadores 4 da Marvel'
opcao_2 = 'Como Treinar o Seu Dragão 3'
opcao_3 = 'Dumbo'
opcao_4 = 'Shazam!'
ingresso = '12,50'

while True:
    escolha_de_filme = input('Digite uma opção de 1 á 4: ')

    if escolha_de_filme == '1':
        print(f'Você escolheu o filme: {opcao_1}, o valor do seu ingresso é: ${ingresso}')
    elif escolha_de_filme == '2':
        print(f'Você escolheu o filme: {opcao_2}, o valor do seu ingresso é: ${ingresso}')
    elif escolha_de_filme == '3':
        print(f'Você escolheu o filme: {opcao_3}, o valor do seu ingresso é: ${ingresso}')
    elif escolha_de_filme == '4':
        print(f'Você escolheu o filme: {opcao_4}, o valor do seu ingresso é: ${ingresso}')
    else:
        print('Você não escolheu nenhuma das opções.')

    sair = input('Você deseja comprar novamente? [s]im - [n]ão: ').lower().startswith('s')

    if sair == 'n':
        print('Obrigado, até a próxima!')

    if sair is False:
        break
