lista_de_alunos = []

def calcular_media(aluno):

    count = 0
    soma = 0

    for nota in range(4):
        nota = int(input('Notas: '))
        if nota > (aluno["maior nota"]):
            (aluno["maior nota"]) = nota
            count += 1
            soma = (soma + nota)
            aluno["media"] = (soma/count)
        else:
            pass

while True:

    comando = input('Comando: ')

    if comando == 'continue':

        aluno = {
        'matricula': int(input('Matricula: ')),
        'nome': input('Nome: '),
        'sobrenome' : input('Sobrenome: '),
        'idade' : int(input('Idade: ')),
        'email': input('Email: '),
        'maior nota': int(0),
        'media': int(0)
        
        }

        print(calcular_media(aluno))
        print(aluno)
        lista_de_alunos.append(aluno)

    elif comando == 'fim':
        break
