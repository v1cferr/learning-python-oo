# Usando o Python 3.13

# Criando uma classe
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

# Instanciando a classe Restaurante em um objeto
restaurante_praca = Restaurante()

# Atribuindo valores ao objeto
restaurante_praca.nome = "Praca"
restaurante_praca.categoria = "Comida Brasileira"
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()

array_restaurantes = [restaurante_praca, restaurante_pizza]

# print(array_restaurantes) # Saída: apenas referencia o objeto na memória com endereços hexadecimais

# print(vars(restaurante_praca)) # Saída: {'nome': 'Praca', 'categoria': 'Comida Brasileira', 'ativo': True}

# ------------------------------------------------------------

# 1- Criando uma classe
# 2- Instanciando o objeto
# 3- Adicionando valores aos atributos

class Musica:
    nome = ""
    artista = ""
    duracao = 0

musica_1 = Musica()
musica_1.nome = "Breezeblocks"
musica_1.artista = "Alt-J"
musica_1.duracao = 227

# print(f'Musica: {musica_1.nome} - Artista: {musica_1.artista} - Duração: {musica_1.duracao} segundos')

# ------------------------------------------------------------

# Exercicio: https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos/task/147014

restaurante_praca.categoria = "Italiana"
print(restaurante_praca.categoria)


