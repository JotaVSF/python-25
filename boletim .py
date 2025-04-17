class Cores:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'

import os
import json

# Configuração inicial
nome_do_arquivo = 'boletim_alunos.json'  # Troquei para .json por convenção

# Inicializa o arquivo se não existir
if not os.path.exists(nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        json.dump([], arquivo)

# Carrega dados existentes
with open(nome_do_arquivo, 'r') as arquivo:
    alunos = json.load(arquivo)

def calcular_media(notas):
    return sum(notas) / len(notas)

def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Nome completo: ").title()
    idade = int(input("Idade: "))
    email = input("Email: ").lower()
    
    while True:
        try:
            matematica = float(input("Nota de Matemática (0-10): "))
            portugues = float(input("Nota de Português (0-10): "))
            historia = float(input("Nota de História (0-10): "))
            
            if all(0 <= nota <= 10 for nota in [matematica, portugues, historia]):
                break
            else:
                print(f"{Cores.VERMELHO}❌ Erro: Notas devem estar entre 0 e 10!{Cores.RESET}")
        except ValueError:
            print(f"{Cores.VERMELHO}❌ Erro: Digite apenas números!{Cores.RESET}")

    aluno = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'notas': {
        'matematica': matematica,
        'portugues': portugues,
        'historia': historia
        }
    }
    
    alunos.append(aluno)
    
    with open(nome_do_arquivo, 'w') as arquivo:
        json.dump(alunos, arquivo, indent=4)
    
    print(f"{Cores.VERDE}✅ Aluno {nome} cadastrado com sucesso!{Cores.RESET}")

def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in alunos:
        notas = aluno['notas']
        media = calcular_media([notas['matematica'], notas['portugues'], notas['historia']])
        
        print(f"""
        Nome: {aluno['nome']}
        Idade: {aluno['idade']}
        Email: {aluno['email']}
        Notas:
        Matemática: {notas['matematica']}
        Português: {notas['portugues']}
        História: {notas['historia']}
        Média: {media:.1f}
        {'='*30}""")

def melhor_media():
    print("\n--- MELHOR MÉDIA ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    melhor = max(alunos, key=lambda x: calcular_media([
        x['notas']['matematica'],
        x['notas']['portugues'],
        x['notas']['historia']
    ]))
    
    notas = melhor['notas']
    media = calcular_media([notas['matematica'], notas['portugues'], notas['historia']])
    
    print(f"""
    🏆 Aluno com melhor média:
    Nome: {melhor['nome']}
    Idade: {melhor['idade']}
    Email: {melhor['email']}
    Notas:
    Matemática: {notas['matematica']}
    Português: {notas['portugues']}
    História: {notas['historia']}
    Média: {media:.1f}
    """)
def status_aprovacao(media):
    if media >= 7:
        return f"{Cores.VERDE}✅ Aprovado{Cores.RESET}"
    elif media >= 5:
        return f"{Cores.AMARELO}⚠️ Recuperação{Cores.RESET}"
    else:
        return f"{Cores.VERMELHO}❌ Reprovado{Cores.RESET}"
#Ranking media dos alunos
def ranking_alunos():
    print(f'\n{Cores.AMARELO}🏆 Ranking de médias 🏆{Cores.RESET}')
    if not alunos:
        return 'Nenhum aluno cadastrado. '
    
    alunos_media = []
    for aluno in alunos:
        try:
            notas = aluno['notas']
            media = calcular_media([notas['matematica'], notas['portugues'], notas['historia']])
            alunos_media.append({
                'aluno': aluno,
                'media': float(media)
            })
        except (KeyError, TypeError) as e:
            print(f"{Cores.VERMELHO}⚠️ Dados inválidos do aluno {aluno.get('nome', '[nome não encontrado]')} - ignorado{Cores.RESET}")
            continue
    try:
        ranking = sorted(alunos_media, key=lambda x: x['media'], reverse= True ) #Organiza do maior para o menor.
    except Exception as e:
        print(f"{Cores.VERMELHO}❌ Erro ao gerar ranking: {e} {Cores.RESET}")
        return
    for posicao, item in enumerate(ranking, start=1): #Exibe da primeira a ultima posição.
        aluno = item['aluno']
        media = item['media']

        medalha =  '🥇' if posicao == 1 else \
                 '🥈' if posicao == 2 else \
                 '🥉' if posicao == 3 else ' '

        print(f"""
        {medalha} Posição #{posicao}
        Nome: {aluno['nome']}
        Média: {media:.1f} ({status_aprovacao(media)})
        Notas: 
        Matemática: {aluno['notas']['matematica']}
        Português: {aluno['notas']['portugues']}
        História: {aluno['notas']['historia']}
        {'-'*40}""")
    
# Menu principal
while True:
    try:
        opcao = int(input(f"""{Cores.AZUL}
        📚 SISTEMA DE BOLETIM ESCOLAR
        ----------------------------
        1 ➔ Cadastrar aluno
        2 ➔ Lista alunos
        3 ➔ Melhor média
        4 ➔ Ranking de médias
        5 ➔ Sair
        Opção: {Cores.RESET}"""))
        
        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            melhor_media()
        elif opcao == 4:
            ranking_alunos()
        elif opcao == 5:
            print("\nSaindo do sistema... Até logo! 👋")
        else:
            print(f"\n{Cores.VERMELHO}❌ Opção inválida! Digite 1-5.{Cores.RESET}")
    
    except ValueError:
        print(f"\n{Cores.VERMELHO}❌ Erro: Digite apenas números!{Cores.RESET}")

    
    

        
    

    
    
