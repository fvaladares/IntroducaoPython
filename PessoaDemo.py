from Pessoa import Pessoa

if __name__ == '__main__':
    print()
    pessoa_um = Pessoa(nome='João',
                       data_nascimento='16/11/1982',
                       nacionalidade='Brasileiro')
    pessoa_dois = Pessoa(nome='Maria',
                         data_nascimento='15/10/1989',
                         nacionalidade='Brasileiro')

    pessoa_formatada = ('Nome: {nome}, '
                        'Data Nascimento: {data_nascimento}, '
                        'Nacionalidade: {nacionalidade}')

    pessoa_um.nome = 'Fabricio'
    # print(pessoa_formatada.format(nome=pessoa_um.nome,
    #                               data_nascimento=pessoa_um.data_nascimento,
    #                               nacionalidade=pessoa_um.nacionalidade))
    print(pessoa_um)
    print(pessoa_dois)

    print()
    print(pessoa_um.nome)
    print(pessoa_um.falar_nome())
