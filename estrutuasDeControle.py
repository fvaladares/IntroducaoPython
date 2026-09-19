if __name__ == '__main__':
    numero_inteiro = int(input('Por favor, informe um número inteiro: '))

    if numero_inteiro > 0:
        print(f'O numero {numero_inteiro} é positivo.')
    elif numero_inteiro < 0:
        print(f'O numero {numero_inteiro} é negativo.')
    else:
        print(f'O numero {numero_inteiro} não é positivo nem negativo.')

    print('\n----------------------------\n')

    idade = int(input('Informe a sua idade: '))
    status = ''
    if 12 < idade < 18:
        status = 'Adolescente'
    else:
        status = 'Não adolescente'

    print(status)

    novo_status = 'Adolescente' if 12 < idade < 18 else 'Não adolescente'
    print(novo_status)
