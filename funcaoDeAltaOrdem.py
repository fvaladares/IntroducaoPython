import math


def funcao_aplicar(x, funcao):
    return funcao(x)


def multiplicar_por_dez(x):
    return x * 10


def calcular_imposto_simples(valor):
    return math.ceil(valor * 0.3)


def calcular_taxa_imposto(valor_produto, funcao_calculo):
    return funcao_calculo(valor_produto)


if __name__ == '__main__':
    print()
    print(funcao_aplicar(20, multiplicar_por_dez))
    print()
    print('Executando o exemplo de uma função de alta ordem')
    valor_produto = 45000
    imposto_devido = calcular_taxa_imposto(valor_produto=valor_produto,
                                           funcao_calculo=calcular_imposto_simples)
    print(f'Imposto devido sobre o valor de R${valor_produto:.2f}'
          f' é de R${imposto_devido:.2f}')
