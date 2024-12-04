# Usando o Python 3.13

# Criando uma classe
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

# Instanciando a classe Restaurante em um objeto
restaurante_1 = Restaurante()

# Atribuindo valores ao objeto
restaurante_1.nome = "Potato"
restaurante_1.categoria = "Comida"
restaurante_1.ativo = True

restaurante_2 = Restaurante()

array_restaurantes = [restaurante_1, restaurante_2]

# print(array_restaurantes) # Saída: apenas referencia o objeto na memória com endereços hexadecimais

print(vars(restaurante_1)) # Saída: {'nome': 'teste', 'categoria': 'teste', 'ativo': 0}

# ------------------------------------------------------------

class Musica:
    nome = ""
    artista = ""
    duracao = 0

musica_1 = Musica()
musica_1.nome = "Breezeblocks"
musica_1.artista = "Alt-J"
musica_1.duracao = 227000
