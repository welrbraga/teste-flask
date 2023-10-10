# encoding: utf8

from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def home():
    return "Pagina inicial"

@myapp.route("/about/")
def about():
    return "Aplicação de teste criada por welrbraga"

@myapp.route("/nome/")
@myapp.route("/nome/<nome>/")
def view_nome(nome=None):
    if nome:
        return f"Olá {nome}"
    return "Olá estranho"

def main():
    '''Função principal
    '''
    print("Execute: poetry run flask --app simples run --debug")
    return 0

if __name__ == '__main__':
    main()
