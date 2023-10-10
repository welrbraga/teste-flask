# encoding: utf8

from flask import Flask

class MyApp:

    def __init__(self) -> None:
        '''Inicializador da classe.
        
        Inicia um objeto Flask e associa as views do Flask as respectivas
        funções/métodos'''
        self.myapp = Flask(__name__)

        self.myapp.add_url_rule("/", view_func=self.view_home )
        self.myapp.add_url_rule("/about/", view_func=self.view_about )
        self.myapp.add_url_rule("/nome/", view_func=self.view_nome )
        self.myapp.add_url_rule("/nome/<nome>/", view_func=self.view_nome )

    def run(self) -> Flask:
        '''Esta é função que retorna a instância Flask'''
        return self.myapp

    def view_home(self) -> str:
        '''View home'''
        return "Pagina inicial"

    def view_about(self) -> str:
        '''View about'''
        return "Aplicação de teste criada por welrbraga"

    def view_nome(self, nome:str=None) -> str:
        '''View nome
        Recebe, opcionalmente, um nome a ser exibido.'''
        if nome:
            return f"Olá {nome}"
        
        return "Olá estranho"

def create_app() -> Flask:
    '''Função que inicializa a aplicação Flask'''
    myapp = MyApp()
    return myapp.run()

def main() -> int:
    '''Função principal
    '''
    print("Execute: poetry run flask --app classes run --debug")
    return 0

if __name__ == '__main__':
    main()
