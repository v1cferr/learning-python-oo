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

# https://cursos.alura.com.br/course/python-aplicando-orientacao-objetos/task/147014

# Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?

# Exercícios

#     Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
#     Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
#     Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
#     Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
#     Altere o valor do atributo nome para 'Bistrô'.
#     Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
#     Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
#     Mude o estado da instância restaurante_pizza para ativo.
#     Imprima no console o nome e a categoria da instância restaurante_praca.

# As opções de solução das atividades estão disponíveis na seção “Opinião da pessoa instrutora”.

restaurante_praca.categoria = "Italiana"
print(restaurante_praca.categoria)



