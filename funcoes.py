def hello():
    """
    Esta função imprime uma mensagem Olá mundo em inglês.
    :return:
    """
    print("Hello World")


def funcao_troca(num_a, num_b):
    """
    Função para inverter dois valores
    :param num_a:
    :param num_b:
    :return: Os parâmetros em ordem inversa
    """
    return num_b, num_a


def potenciacao(base, expoente=2):
    return base ** expoente


if __name__ == '__main__':
    print('Olá')
    print()
    hello()
    print()
    num_a = 10
    num_b = 20
    print(f'num_a: {num_a} | num_b: {num_b}')
    num_a, num_b = funcao_troca(num_a, num_b)
    print('Após execução da função de troca')
    print(f'num_a: {num_a} | num_b: {num_b}')

    base = 2
    expoente = 5

    resultado = potenciacao(base, expoente)

    print()
    print('Usando base e expoente')
    print(f'{base}^{expoente} = {resultado}')

    print()
    resultado = potenciacao(base)
    print('Usando apenas a base')
    print(f'{base}^{2} = {resultado}')

    resultado = potenciacao(expoente=expoente, base=base)
    print(f'{base}^{expoente} = {resultado}')
