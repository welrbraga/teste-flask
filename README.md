# Teste com aplicações Flask

Há três exemplos de teste com uma aplicação simples em Flask

* simples - usando funções indepedentes como views do Flask
* factory - usando uma função factory aplication
* classes - usando uma classe

## Inicialização do ambiente

O ambiente de teste usa o [Poetry](https://python-poetry.org/docs/) como gerenciador de pacotes Python. Caso não o tenha instalado, siga o link acima para ver o procedimetno de instalação.

Com o poetry instalado faça o download deste repositório e inicialize o ambiente do Poetry

```shell
cd teste-flask
poetry init
```

## Exemplo simples

1- Iniciar a aplicação

```shell
poetry run flask --app simples run --debug
```

* Como a aplicação é um pacote, ela pode ser invocada apenas pelo nome.
* Se o nome do pacote fosse app ou wsgi, ou ainda se fosse apenas um módulo chamado app.py ou wsgi.py, no diretório atual, o parâmetro --app seria desnecessário.

2- Testar a aplicação

```shell
tests/testes.sh
```

## Exemplo factory function

A função de contrução da aplicação deve obrigatoriamente chamada "create_app()".

1- Iniciar a aplicação

```shell
poetry run flask --app factory run --debug
```

* Como a aplicação é um pacote, ela pode ser invocada apenas pelo nome.
* Se o nome do pacote fosse app ou wsgi, ou ainda se fosse apenas um módulo chamado app.py ou wsgi.py, no diretório atual, o parâmetro --app seria desnecessário.

2- Testar a aplicação

```shell
tests/testes.sh
```

## Exemplo com classes

A função de contrução da aplicação deve obrigatoriamente chamada "create_app()".

1- Iniciar a aplicação

```shell
poetry run flask --app classes run --debug
```

* Como a aplicação é um pacote, ela pode ser invocada apenas pelo nome.
* Se o nome do pacote fosse app ou wsgi, ou ainda se fosse apenas um módulo chamado app.py ou wsgi.py, no diretório atual, o parâmetro --app seria desnecessário.

2- Testar a aplicação

```shell
tests/testes.sh
```
