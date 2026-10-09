# Programa principal: menu e telas.
import banco
import utilidades

def mostrar_menu():
    print("\n===========================================")
    print("SISTEMA DE NOTAS ESCOLAR")
    print("=============================================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno por nome")
    print("4 - Atualizar notas")
    print("5 - Remover aluno")
    print("6 - Relatório da turma")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def mostrar_aluno(aluno):
    """Mostra uma linha com os dados de um aluno."""
    id_aluno, nome, nota1, nota2 = aluno
    media = utilidades.calcular_media(nota1,nota2)
    situacao = utilidades.situacao(media)
    print(f"[{id_aluno:>3}] {nome:<22}" 
          f"N1: {nota1:>4.1f} N2:{nota2:>4.1f}" 
          f"Média: {media:>4.1f} {situacao}")

def cadastrar_aluno():
    print("\n--- Cadastrar aluno ---")
    nome = utilidades.ler_texto("Nome: ")
    nota1 = utilidades.ler_nota("Nota 1 (0 a 10): ")
    nota2 = utilidades.ler_nota("Nota 2 (0 a 10): ")
    banco.inserir_aluno(nome, nota1, nota2)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\n--- Listar aluno ---")
    alunos = banco.listar_alunos()
    if len(alunos) == 0:
        print("Nenhum aluno encontrado.")
        return
    for aluno in alunos:
        mostrar_aluno()

def buscar_aluno():
    print("\n--- Buscar aluno ---")
    texto = utilidades.ler_texto("Digite parte do nome: ")
    alunos = banco.buscar_por_nome(texto)
    if len(alunos) == 0:
        print("Nenhum aluno encontrado.")
        return
    for aluno in alunos:
        mostrar_aluno()

def atualizar_notas():
    print("\n--- Atualizar notas ---")
    id_aluno = utilidades.ler_inteiro("Digite o ID do aluno: ")
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    mostrar_aluno()
    nota1 = utilidades.ler_nota("Nova nota 1: ")
    nota2 = utilidades.ler_nota("Nova nota 2: ")
    banco.atualizar_notas(id_aluno, nota1, nota2)
    print("Notas atualizadas")

def remover_aluno():
    print("\n--- Remover aluno ---")
    id_aluno = utilidades.ler_inteiro("Digite o ID do aluno: ")
    aluno = banco.buscar_por_id(id_aluno)
    if aluno is None:
        print("Aluno não encontrado.")
        return
    mostrar_aluno()
    confirmar = input("Tem certeza que deseja remover? (s/n): ").lower()
    if confirmar == "s":
        banco.remover_aluno(id_aluno)
        print("Aluno Removido.")
    else:
        print("Remoção cancelada.")

def mostrar_relatorio():
    print("\n--- Relatório da turma ---")
    alunos= banco.listar_alunos()
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    soma_medias = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    melhor_nome = ""
    melhor_media = -1

    for id_aluno, nome, nota1, nota2 in alunos:
        media = utilidades.calcular_media(nota1, nota2)
        soma_medias +=1

        situacao = utilidades.situacao(media)
        if situacao == "Aprovado":
            aprovados +=1
        elif situacao == "Recuperação":
            recuperacao +=1
        else:
            reprovados +=1

        if media > melhor_media:
            melhor_media = media
            melhor_nome = nome

    print(f"Total de alunos: {len(alunos)}")
    print(f"Média da turma : {soma_medias / len(alunos):.2f}")
    print(f"Aprovados      : {aprovados}")
    print(f"Em recuperação : {recuperacao}")
    print(f"Reprovados     : {reprovados}")
    print(f"Melhor média   : {melhor_nome} ({melhor_media:.1f})")