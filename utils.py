from models import Pessoas, Usuarios

#Insere dados na tabela pesssoa
def insere_pessoas():
    pessoas = Pessoas(nome='Santhiago', idade=8)
    print(pessoas)
    pessoa.save()

#Consulta dados na tabela pesssoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoas = Pessoas.query.filter_by(nome='Santhiago').first()
    print(pessoas.idade)

#Altera dados na tabela pesssoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.nome = 'Fabio'
    pessoa.save()

#Exclui pessoa na tabela pesssoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fabio').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('fabio', '1234')
    insere_usuario('santhiago', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()