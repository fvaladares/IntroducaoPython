
if __name__ == '__main__':
    contador = 0
    print('Iniciando a contagem...')
    while contador < 10:
        print(contador, ' ', end='')
        contador += 1
    print()
    print('A contagem chegou ao fim.')

    print('Criando a iteração usando os valores em um range')
    for i in range(0, 10):
        print(i, ' ', end = '')
    print()
    print('A contagem chegou ao fim.')


    print('Criando a iteração usando os valores em um range de dois em dois')
    for i in range(0, 10, 2):
        print(i, ' ', end = '')
    print()
    print('A contagem chegou ao fim.')

    print('\n----------------------------\n')

    numero_informado = int(input('Informe um número entre 0 e 10: '))
    for i in range(0, 10):
        if i == numero_informado:
            break
        print(i, ' ', end='')
    else:
        print()
        print('A iteração total foi concluída com sucesso!')