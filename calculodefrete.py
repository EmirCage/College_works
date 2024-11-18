def calcular_frete():

    print('Regiões para frete:')
    print('1 - Sul')
    print('2 - Suldeste')
    print('3 - Centro-Oeste')

    regiao = int(input('Digite a região 1, 2 ou 3: '))

    num_pecas = int(input('Digite a quantidade de peças: '))

    distancia = int(input('Digite a distãncia em quilõmetros: '))

    rastreamento = input('Deseja rastreamento S-sim ou N-não: ').upper()

    taxa_rastreamento = 200.00 if rastreamento == 'S' else 0.00

    if regiao == 1:
        valor_frete = 1.00
        desconto = 0.10
    elif regiao == 2:
        valor_frete = 1.20
        desconto = 0.12
    elif regiao == 3:
        valor_frete = 1.30
        desconto = 0.13
    else:
        print('Região inválida')
        return

    if num_pecas <= 1000:
        valor_frete_total_pecas = num_pecas * valor_frete
    else:
        valor_frete_ate_mil_pecas = 1000 * valor_frete
        pecas_extras = num_pecas - 1000
        valor_frete_extra = pecas_extras * (valor_frete * (1 - desconto))
        valor_frete_total_pecas = valor_frete_ate_mil_pecas + valor_frete_extra

    valor_por_km = distancia * 1.00

    total_frete = valor_frete_total_pecas + valor_por_km + taxa_rastreamento

    print(f'Taxa de rastreamento: R${taxa_rastreamento:.2f}')
    print(f'Valor do frete pelas peças: R${valor_frete_total_pecas:.2f}')
    print(f'valor do frete baseado nos quilômetros: R${valor_por_km:.2f}')
    print(f'Valor total do frete: R${total_frete:.2f}')


calcular_frete()
