# encoding: utf8

from flask import Flask

def create_app():
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
    
    return myapp

def main():
    '''Função principal
    '''
    print("Execute: poetry run flask --app factory run --debug")
    return 0

if __name__ == '__main__':
    main()
