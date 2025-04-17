import os
import json

arquivo_nome = "Registro_alunos.txt"

# Garante que o arquivo existe antes de tentar escrever nele (Caso o arquivo já exista. GARANTIR QUE ELE ESTEJA APENAS COM [])
if not os.path.exists(arquivo_nome):
    with open(arquivo_nome, "w") as arquivo:
        json.dump([], arquivo) 

while True: 
    menu = int(input('''
    Selecione a opção desejada:
    1 - Adicionar novos alunos 
    2 - Visualizar cadastro de alunos
    3 - Excluir registro de aluno 
    4 - Encerrar programa

    opção: '''))

    if os.path.exists("Registro_alunos.txt"):
        
        if menu == 1:
            while menu == 1:
                print("\n   Você selecionou adicionar novos alunos")
                nome = str(input("     Digite o nome do colaborador: "))
                cargo = str(input("     Digite o cargo do colaborador: "))
                curso = str(input("     Digite o curso do colaborador: "))

                # Crio o dicionário e inputo os dados.
                dados_registro_dicionario = {"nome": nome, "cargo": cargo, "curso": curso}

                # Lê o arquivo.txt existente e converte em lista.
                with open(arquivo_nome, "r") as arquivo:
                    lista_registro = json.load(arquivo)

                # Adiciona o dicionário novo dentro da lista existente.
                lista_registro.append(dados_registro_dicionario)

                # Adiciona o novo valor da lista dentro do arquivo.
                with open(arquivo_nome, "w") as arquivo:
                    json.dump(lista_registro, arquivo, indent=4)

                print("\n   Aluno cadastrado com sucesso!")

                submenu = int(input('''\n   Você deseja adicionar mais algum aluno:
    1 - Sim
    2 - Não

    Opção: '''))
                if submenu == 1:
                    continue
                elif submenu == 2:
                    break
                else:
                    print("\n   ### Opção inválida ###")
        elif menu == 2: 
            print("\n   Lista de alunos cadastrados:\n")

            try:
                with open(arquivo_nome, "r") as arquivo:
                    lista_registro = json.load(arquivo)
                    if not lista_registro:
                        print("Nenhum aluno cadastrado.")
                    else:
                        # Percorre todo o arquivo txt e printa o registro dos alunos.
                        for i, aluno in enumerate(lista_registro):
                            print(f"   Aluno {i+1}:")
                            print(f"    Nome: {aluno['nome']}")
                            print(f"    Cargo: {aluno['cargo']}")
                            print(f"    Curso: {aluno['curso']}\n")

            except (json.JSONDecodeError, FileNotFoundError):
                print(" Erro ao carregar os registros ou arquivo não encontrado.")

        elif menu == 3:
            try:
                with open(arquivo_nome, "r") as arquivo:
                    lista_registro = json.load(arquivo)

                if not lista_registro:
                    print(" Nenhum aluno cadastrado para excluir.")
                else:
                    nome_excluir = input("  Digite o nome do aluno que deseja excluir: ")

                    # Filtra a lista removendo o aluno com o nome digitado
                    nova_lista = [aluno for aluno in lista_registro if aluno["nome"].lower() != nome_excluir.lower()]

                    if len(nova_lista) == len(lista_registro):
                        print(f"    Nenhum aluno encontrado com o nome '{nome_excluir}'.")
                    else:
                        # Sobrescreve o arquivo com a lista atualizada
                        with open(arquivo_nome, "w") as arquivo:
                            json.dump(nova_lista, arquivo, indent=4)
                        print(f"    Aluno '{nome_excluir}' removido com sucesso!")

            except (json.JSONDecodeError, FileNotFoundError):
                print(" Erro ao carregar os registros ou arquivo não encontrado.")

        elif menu == 4:
            print(" Programa encerrado.")
            break
        else:
            print(" ### Opção inválida ###")
    else:
        print(" O arquivo não existe.")