# Iniciando

<https://www.freecodecamp.org/news/how-to-use-oop-in-python/>

> Em **programação orientada a objetos (OO)**, uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

```python
class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_teste = Restaurante()
```
> Instanciando a classe `Restaurante` em um objeto ^

```python
python .\restaurante.py
[<__main__.Restaurante object at 0x000001E4A4636A50>, <__main__.Restaurante object at 0x000001E4A48C8A50>]
```
> Referenciando um objeto na memória (Endereço Hexadecimal) ^

## Boas práticas da [PEP 8](https://www.dio.me/articles/voce-sabe-o-que-e-pep-8-guia-para-um-codigo-limpo-e-eficiente)

```python
class Restaurante:
    def __init__(self, nome="", categoria="", ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

# Instanciando a classe
restaurante_teste = Restaurante()
```
> Convenções da [PEP 8](https://www.dio.me/articles/voce-sabe-o-que-e-pep-8-guia-para-um-codigo-limpo-e-eficiente) (com espaçamento adequado)

