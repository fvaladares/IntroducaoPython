class Pessoa:
    def __init__(self, nome, data_nascimento, nacionalidade):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._nacionalidade = nacionalidade
        self._idade = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Entrando no setter do nome')
        if isinstance(nome, str) and len(nome) > 2:
            self._nome = nome

    @property
    def idade(self):
        if self._idade == 0:
            dados_dada_nascimento = str(self._data_nascimento).split('/')
            ano_nascimento = int(dados_dada_nascimento[2])
            mes_nascimento = int(dados_dada_nascimento[1])
            ano_corrente = 2026
            self._idade = ano_corrente - ano_nascimento
            mes_corrente = 10
            if mes_nascimento > mes_corrente:
                self._idade -= 1

        return self._idade

    def falar_nome(self):
        return f'Meu nome é {self._nome}'

    def __str__(self):
        return  (f'Nome: {self._nome}, ' +
                 f'Data Nascimento: {self._data_nascimento}, ' +
                 f'Nacionalidade: {self._nacionalidade}' +
                 f'Idade: {self.idade}')


