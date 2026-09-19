variavel_global = 662

def minha_funcao():
    global variavel_global
    variavel_global += 661
    return variavel_global

def funcao_externa():
    titulo = 'Aula Python'
    def funcao_interna():
        nonlocal titulo
        titulo = ('Aula Python - Em andamento, '
                  'apesar do computador não querer ajudar')
        print('resultado funcao_interna', titulo)
    funcao_interna()
    print('resultado funcao_externa', titulo)


if __name__ == '__main__':
    print('Variável global: ', variavel_global)

    print('Retorno da função: ', minha_funcao())

    print('Variável global: ', variavel_global)

    print()

    print('Chamando a função externa')
    funcao_externa()
