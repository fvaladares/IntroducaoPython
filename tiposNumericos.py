

if __name__ == '__main__':
    idade = None
    print(f'Tipo da variável idade {type(idade)}')

    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))

    print('\n----------------------------\n')
    print(f'Tipo da variável altura {type(altura)}')
    print('\n----------------------------\n')
    print(f'Tipo da variável idade {type(idade)}')
    print('\n----------------------------\n')
    numero_complexo = 33 + 8j
    print(f'Tipo {type(numero_complexo)}, '
          f'\nparte real: {numero_complexo.real}, '
          f'\nparte imaginária: {numero_complexo.imag}, '
          f'\nnúmero completo: {numero_complexo}')

    print('\n----------------------------\n')
    numero_ponto_flutante = 4*0.1
    print(f'Número com ponto flutuante 4*0.1 = {numero_ponto_flutante}')
    print('\n----------------------------\n')
    numero_ponto_flutante = 3*0.1
    print(f'Número com ponto flutuante 3*0.1 = {numero_ponto_flutante}')

    print('\n----------------------------\n')
    saida_formatada = '{:>10} = {}'
    print(saida_formatada.format('3//2', 3//2))  #1.5
    print(saida_formatada.format('-3//2', -3//2)) #-1.5
    print(saida_formatada.format('-3/2', int(-3/2))) #-1.5


    # print(f'Coteúdop da variável numero_complexo {numero_complexo}')
    # print(f'Tipo da variável numero_complexo {type(numero_complexo)}')
