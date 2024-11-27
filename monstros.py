

def obter_escolha_usuario_1():
    print('Esolha a primeria parte de seu monstro:')
    print('1 - FRANKEN')
    print('2 - ZOMBOS')
    print('3 - HAPPY')
    escolha = input('Digite um número de sua escolha: ')

    if escolha == '1':
        return 'FRANKEN'
    elif escolha == '2':
        return 'ZOMBOS'
    elif escolha == '3':
        return 'HAPPY'
    else:
        print('Escolha inválida. Tente novamente')
        return obter_escolha_usuario_1()


def obter_escolha_usuario_2():
    print('Escolha a segunda parte de seu monstro:')
    print('1 - SPRITEM')
    print('2 - WACKUS')
    print('3 - VEGITAS')
    escolha_dois = input('Digite um número de sua escolha: ')

    if escolha_dois == '1':
        return 'SPRITEM'
    elif escolha_dois == '2':
        return 'WACKUS'
    elif escolha_dois == '3':
        return 'VEGITAS'
    else:
        print('Escolha inválida. Tente novamente')
        return obter_escolha_usuario_2()


def escolha_final(escolha_usuario_1, escolha_usuario_2):
    if escolha_usuario_1 == 'FRANKEN' and escolha_usuario_2 == 'WACKUS':
        print('Você montou Franken Wackus, um monstro já existente, ele tem a \
cabeça no formato "Franken" e predominância da característica "Wackus".')
    elif escolha_usuario_1 == 'ZOMBOS' and escolha_usuario_2 == 'VEGITAS':
        print('Você montou Zombos Vegitas, assim chamado porque ele tem \
classificação de cabeça "Zombos" e predominância de \
características "Vegitas".')
    elif escolha_usuario_1 == 'HAPPY' and escolha_usuario_2 == 'SPRITEM':
        print('Você montou o monstro da família Happy. Sua cabeça tem um \
formato "Happy" distinto, enquanto suas características faciais \
são predominantemente "Spritem".')

    else:
        print('Monstro não compatível com sua característica!')
        print()
        print('TENTE NOVAMENTE.')


def jogar():
    print('Boa sorte ao montar seu monstro!👹👹')
    escolha_usuario_1 = obter_escolha_usuario_1()
    escolha_usuario_2 = obter_escolha_usuario_2()

    print(f'Primeira parte do monstro: {escolha_usuario_1}')
    print(f'Segunda parte do monstro: {escolha_usuario_2}')

    escolha_final(escolha_usuario_1, escolha_usuario_2)


jogar()
