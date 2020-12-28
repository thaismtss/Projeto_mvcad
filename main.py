import csv
from pessoa import insert_pessoa, retorna_pessoas, retorna_pessoa,remove_pessoa

def ler_arquivo():
    with open('curso-mvcad.csv', encoding="utf8") as file:
        leitor = csv.DictReader(file, delimiter=',')

        for pessoa in leitor:
            cpf = pessoa['cpf'].replace('.', '')
            pessoa['cpf'] = cpf.replace('-', '')
            insert_pessoa(pessoa)

retorna_pessoas()
# ler_arquivo()

# pessoa = {
#     'nome': "Priscila",
#     'endereco': "Vila Nova",
#     'cpf': '01234567899',
#     'estado': "Santa Catarina",
#     'turma': "MVCAD Python 1",
#     'periodo': "matutino",
#     'modulo': "MVCAD"
# }
# insert_pessoa(pessoa)
