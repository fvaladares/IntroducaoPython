# Arquivo python de exemplo


nome_completo = ''
nome_completo = 'Fabricio Valadares'

print('Boas vindas à aula de introdução ao Python!')

print('*O nome armazenado é: ', nome_completo)

print('**O nome armazenado é: {}'.format(nome_completo))

print(f'***O nome armazenado é: {nome_completo}')

print("Exemplo do uso de áspas duplas.")

print('João falou: "Olá"')

tamanho_variavel = len(nome_completo)

print(f'O tamanho do texto armazendo na variavel '
      f'nome_completo é {tamanho_variavel}')

print(f'Caractere na posição 10 {nome_completo[10]}')

# nome_completo[10] = '*' #Isso não é permitido.

nome_completo = 'Pedro Leopoldo'

print(f'Nome nome armazenado na variável {nome_completo}')

# range [início:fim] -> [início:fim)
print(f'Trecho entre os caracteres 5 e 10 {nome_completo[5:10]}')
print(f'Trecho entre os caracteres 0 e 10 {nome_completo[:10]}')
print(f'Trecho entre os caracteres 10 e o fim {nome_completo[10:]}')

texto_longo = """Classes are defined using the class keyword, 
followed by the class name and a colon. 


Attributes are variables defined inside class and 
represent properties of the class. 

Attributes can be accessed using dot (.)
 
       operator (e.g., MyClass.my_attribute)."""

print('\n----------------------------\n')

print(texto_longo)

print('\n----------------------------\n')
sequencia_numerica = '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'

variavel_temporaria = sequencia_numerica.split(',')

print(variavel_temporaria)

# type retorna o tipo de uma variável
print(type(variavel_temporaria[0]))

print('\n----------------------------\n')

print(f'Sequência numérica original: {sequencia_numerica}')
print(f'Quantos números uns existem na '
      f'variável sequencia_numerica {sequencia_numerica.count('1')}')

print(f'Quantas vezes a palavra *the* aparece no texto longo '
      f'{texto_longo.count("the")} vezes')


string_formatada = "{1} canta {2} no ano de {0}"

print(string_formatada.format(1982, 'Pink Floyd', 'Wish you were here'))


string_formatada_v2 = "{artista} canta {musica} no ano de {ano}"
print(string_formatada_v2.format(ano=1970,
                              musica='Iron Man',
                              artista='Black Sabbath'))

print("\n--------------------------\n")

# Formatação e alinhamento da impressão.
print('|{:<50}|'.format("Boas vindas!!"))
