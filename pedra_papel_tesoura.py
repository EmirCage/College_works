import random


def obter_escolha_usuario():
    print('Esolha uma opção:')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    escolha = input('Digite um número de sua escolha: ')

    if escolha == '1':
        return 'Pedra'
    elif escolha == '2':
        return 'Papel'
    elif escolha == '3':
        return 'Tesoura'
    else:
        print('Escolha inválida. Tente novamente')
        return obter_escolha_usuario()


def obter_escolha_computador():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(opcoes)


def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        print('Empate!')
    elif (escolha_usuario == 'Pedra' and escolha_computador == 'Tesorua') or \
         (escolha_usuario == 'Tesoura' and escolha_computador == 'Papel') or \
         (escolha_usuario == 'Papel' and escolha_computador == 'Pedra'):
        print('Você venceu!')

    else:
        print('O computador venceu!')


def jogar():
    print('Bem-vindo ao jogo Pedra-Papel-Tesoura!')
    escolha_usuario = obter_escolha_usuario()
    escolha_computador = obter_escolha_computador()

    print(f'\nVocê escolheu: {escolha_usuario}')
    print(f'O computador escolheu: {escolha_computador}')

    determinar_vencedor(escolha_usuario, escolha_computador)


jogar()
