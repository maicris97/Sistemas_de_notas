import os
import sqlite3
import sys

def pasta_do_programa():
    '''Descobre a pasta onde o programa está.'''
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

CAMINHO_BANCO = os.path.join(pasta_do_programa(), "alunos.db")

def conectar():
    return sqlite3.connect(CAMINHO_BANCO)

def criar_tabela():
    '''Criar a tabela de alunos se ela ainda não existir.'''
    connect = conectar()
    connect.execute('''
      CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL
      )
    ''')
    connect.commit()
    connect.close()

def inserir_aluno(nome,nota1,nota2):
    '''Devolve uma lista de tuplas: (id,nome,nota1,nota2).'''
    connect = conectar()
    connect.execute(
        'INSERT INTO alunos(nome, nota1, nota2) VALUES(?, ?, ?)',
        (nome, nota1, nota2)
    )
    connect.commit()
    connect.close()

def listar_alunos():
    connect = conectar()
    linhas = connect.execute(
        'SELECT id,nome,nota1,nota2 FROM alunos ORDER BY nome'
    ).fetchall()
    connect.close()
    return linhas

def buscar_por_nome(texto):
    '''Buscar aluno cujo nome contém o texto(ignorando maiúsculas).'''
    connect = conectar()
    linhas = connect.execute(
        'SELECT id,nome,nota1,nota2 FROM alunos WHERE nome LIKE ? ORDER BY nome',(f'%{texto}%',),

    ).fetchall()
    connect.close()
    return linhas

def buscar_por_id(id_aluno):
    '''Devolve o aluno com esse id ou None se não existir.'''
    connect = conectar()
    aluno = connect.execute(
        'SELECT id, nome, nota1, nota2 FROM alunos WHERE id = ?',(id_aluno,)
    ).fetchone()
    connect.close()
    return aluno

def atualizar_notas(id_aluno, nota1, nota2):
    connect = conectar()
    connect.execute(
        'UPDATE alunos SET nota1 = ?, nota2 = ? WHERE id = ?', (nota1, nota2, id_aluno)
    )
    connect.commit()
    connect.close()

def remover_aluno(id_aluno):
    connect = conectar()
    connect.execute(
        'DELETE FROM alunos WHERE id = ?', (id_aluno,)
    )
    connect.commit()
    connect.close()
    