def ler_texto(mensagem):
    '''Pede um texto e repete até o usuário digitar algo(não vazio).'''
    while True:
        texto = input(mensagem).strip()
        if texto !='':
            return texto
        print("Este campo não pode ficar vazio.")

def ler_inteiro(mensagem):
    '''Pede um número inteiro até o usuário digitar certo.'''
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")

def ler_nota(mensagem):
    '''Pede uma nota entre 0 e 10. Aceita vírgula ou ponto.'''
    while True:
        try:
            nota = float(input(mensagem).replace(",","."))
        except ValueError:
            print("Digite um número, por exemplo, 7.5")
            continue
        if 0 <= nota <= 10:
            return nota
        print("A nota deve estar entre 0 e 10.")

def calcular_media(nota1,nota2):
    '''Devolve a média simples de duas notas'''
    return (nota1 + nota2)/2

def situacao(media):
    '''Devolve a situação do aluno de acordo com a média.'''
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Recuperação"
    else:
        return "Reprovado"
       
       