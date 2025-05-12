tarefas = [

    {"Id": 1, "Nome": "Treinar", "Descriçao": "Academia", "Prioridade": 2, "Categoria": "Saude", "Concluido": False},
    {"Id": 2, "Nome": "Estudar", "Descriçao": "POO", "Prioridade": 1, "Categoria": "Estudo", "Concluido": False},
    {"Id": 3, "Nome": "Escovar os dentes", "Descriçao": "Higiene", "Prioridade": 1, "Categoria": "Saude", "Concluido": True}
]

def addTarefas():
    tamanho_lista = len(tarefas)
    novoId = tamanho_lista + 1
    nome = input('Insira o nome da nova tarefa: ')
    descricao = input('Insira a descrição: ')
    prioridade = int(input('Insira a prioridade da tarefa atraves de (1-2-3): '))
    categoria = input('Insira a categoria: ')

    nova_tarefa = {
        "Id": novoId,
        "Nome": nome,
        "Descriçao": descricao,
        "Prioridade": prioridade,
        "Categoria": categoria,
        "Concluido": False
    }
    tarefas.append(nova_tarefa)

def listar_tarefas():
    if not tarefas:
        print("\n⚠️ Nenhuma tarefa cadastrada.\n")
        return
      
    print("\n📋 Lista de Tarefas:")
    for tarefa in tarefas:
        status = "✅" if tarefa["Concluido"] else "❌"
        print('-' * 50)
        print(f"ID: {tarefa['Id']}")
        print(f"Nome: {tarefa['Nome']}")
        print(f"Descriçao: {tarefa['Descriçao']}")
        print(f"Prioridade: {tarefa['Prioridade']}")
        print(f"Categoria: {tarefa['Categoria']}")
        print(f"Concluido: {status}")
    print('-' * 50 + '\n')

def marcar_tarefas():
    listar_tarefas()
    if not tarefas:
        return
    
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa concluída: "))
        for tarefa in tarefas:
            if tarefa["Id"] == id_tarefa:
                tarefa["Concluído"] = True
                print("\nTarefa marcada como concluída!\n")
                return
        print("\nTarefa não encontrada.\n")
    except ValueError:
        print("\nID inválido. Digite um número.\n")

def exibir_tarefas():
    prioridade = int(input('Insira a prioridade (1-3): '))
    filtro = [t for t in tarefas if t["Prioridade"] == prioridade]

    if not filtro:
        print(f"\nNenhuma tarefa com prioridade {prioridade}.\n")
        return
    
    print(f"\n📋 Tarefas com Prioridade {prioridade}:")
    for tarefa in filtro:
        status = "✅" if tarefa["Concluido"] else "❌"
        print('-' * 50)
        print(f"ID: {tarefa['Id']} | Nome: {tarefa['Nome']} | Concluído: {status}")
    print('-' * 50 + '\n')
    
    if tarefas == 1:
        print(f'Exbindo de maior prioridade:', tarefas)

addTarefas()
listar_tarefas()
exibir_tarefas()