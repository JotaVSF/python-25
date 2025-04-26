from datetime import datetime

anoAtual = datetime.now().year

#Informações dos colaboradores:
funcionarios = [
    {
        "id": 1, "Nome": "João Silva", "CPF": "123.456.789-00", "RG": "12.345.678-9", 
        "Data de Nascimento": "15/05/1985", "Cargo": "Analista de TI", "Departamento": "Tecnologia", 
        "Salário": 7500.00, "Data de Admissão": "10/03/2020", "Status": "Ativo",
        "Endereço": {"Rua": "Av. Paulista, 1000", "Cidade": "São Paulo", "Estado": "SP", "CEP": "01310-100"},
        "Contato": {"Telefone": "(11) 98765-4321", "Email": "joao.silva@empresa.com"},
        "Dependentes": [{"Nome": "Maria Silva", "Parentesco": "Cônjuge"}, {"Nome": "Pedro Silva", "Parentesco": "Filho"}]
    },
    {
        "id": 2, "Nome": "Ana Oliveira", "CPF": "987.654.321-00", "RG": "98.765.432-1", 
        "Data de Nascimento": "22/11/1990", "Cargo": "Gerente de Vendas", "Departamento": "Comercial", 
        "Salário": 9500.00, "Data de Admissão": "05/07/2018", "Status": "Ativo",
        "Endereço": {"Rua": "Rua das Flores, 200", "Cidade": "Rio de Janeiro", "Estado": "RJ", "CEP": "22010-010"},
        "Contato": {"Telefone": "(21) 99876-5432", "Email": "ana.oliveira@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 3, "Nome": "Carlos Souza", "CPF": "456.789.123-00", "RG": "45.678.912-3", 
        "Data de Nascimento": "30/01/1978", "Cargo": "Assistente Administrativo", "Departamento": "Administração", 
        "Salário": 3500.00, "Data de Admissão": "15/01/2023", "Status": "Ativo",
        "Endereço": {"Rua": "Rua das Palmeiras, 50", "Cidade": "Belo Horizonte", "Estado": "MG", "CEP": "30130-050"},
        "Contato": {"Telefone": "(31) 98765-1234", "Email": "carlos.souza@empresa.com"},
        "Dependentes": [{"Nome": "Luiza Souza", "Parentesco": "Filha"}]
    },
    {
        "id": 4, "Nome": "Mariana Costa", "CPF": "111.222.333-44", "RG": "11.223.344-5",
        "Data de Nascimento": "12/09/1992", "Cargo": "Desenvolvedora Front-end", "Departamento": "Tecnologia",
        "Salário": 6800.00, "Data de Admissão": "20/05/2021", "Status": "Ativo",
        "Endereço": { "Rua": "Rua dos Pinheiros, 300", "Cidade": "Curitiba", "Estado": "PR", "CEP": "80520-000"},
        "Contato": { "Telefone": "(41) 98765-6789", "Email": "mariana.costa@empresa.com"},
        "Dependentes": [ {"Nome": "Rafael Costa", "Parentesco": "Cônjuge"}]
    },
    {
        "id": 5, "Nome": "Lucas Martins", "CPF": "555.666.777-88", "RG": "55.667.778-9",
        "Data de Nascimento": "03/04/1988", "Cargo": "Analista Financeiro", "Departamento": "Financeiro",
        "Salário": 5200.00, "Data de Admissão": "10/11/2019", "Status": "Ativo",
        "Endereço": { "Rua": "Av. Brasil, 1500", "Cidade": "Porto Alegre", "Estado": "RS", "CEP": "90010-001"},
        "Contato": { "Telefone": "(51) 99876-5432", "Email": "lucas.martins@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 6, "Nome": "Fernanda Lima", "CPF": "999.888.777-66", "RG": "99.887.776-6",
        "Data de Nascimento": "25/12/1980", "Cargo": "Gerente de Marketing", "Departamento": "Marketing",
        "Salário": 10500.00, "Data de Admissão": "15/08/2017", "Status": "Ativo",
        "Endereço": {"Rua": "Rua das Orquídeas, 45", "Cidade": "Florianópolis", "Estado": "SC", "CEP": "88010-500"},
        "Contato": {"Telefone": "(48) 98765-1234", "Email": "fernanda.lima@empresa.com"},
        "Dependentes": [{"Nome": "Gabriel Lima", "Parentesco": "Filho"},{"Nome": "Isabela Lima", "Parentesco": "Filha"}]
    },
    {
        "id": 7, "Nome": "Ricardo Alves", "CPF": "222.333.444-55", "RG": "22.334.445-6",
        "Data de Nascimento": "18/07/1975", "Cargo": "Diretor de Operações", "Departamento": "Diretoria",
        "Salário": 25000.00, "Data de Admissão": "01/01/2015", "Status": "Ativo",
        "Endereço": {"Rua": "Av. Atlântica, 200", "Cidade": "Rio de Janeiro", "Estado": "RJ", "CEP": "22010-000"},
        "Contato": {"Telefone": "(21) 99876-6543", "Email": "ricardo.alves@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 8, "Nome": "Patrícia Nunes", "CPF": "777.888.999-00", "RG": "77.889.990-1",
        "Data de Nascimento": "30/03/1995", "Cargo": "Estagiária em RH", "Departamento": "Recursos Humanos",
        "Salário": 1500.00, "Data de Admissão": "02/02/2023", "Status": "Ativo",
        "Endereço": {"Rua": "Rua das Acácias, 30", "Cidade": "Brasília", "Estado": "DF", "CEP": "70000-100"},
        "Contato": {"Telefone": "(61) 98765-9876", "Email": "patricia.nunes@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 9, "Nome": "Gustavo Henrique", "CPF": "444.555.666-77", "RG": "44.556.667-8",
        "Data de Nascimento": "05/10/1982", "Cargo": "Analista de Logística", "Departamento": "Operações",
        "Salário": 4800.00, "Data de Admissão": "12/12/2020", "Status": "Afastado (Licença Médica)",
        "Endereço": {"Rua": "Rua dos Coqueiros, 120", "Cidade": "Salvador", "Estado": "BA", "CEP": "40000-200"},
        "Contato": {"Telefone": "(71) 99876-1122", "Email": "gustavo.henrique@empresa.com"},
        "Dependentes": [{"Nome": "Sofia Henrique", "Parentesco": "Filha"}]
    },
    {
        "id": 10, "Nome": "Juliana Pereira", "CPF": "666.777.888-99", "RG": "66.778.889-0",
        "Data de Nascimento": "14/02/1991", "Cargo": "Designer Gráfico", "Departamento": "Marketing",
        "Salário": 4200.00, "Data de Admissão": "22/04/2022", "Status": "Ativo",
        "Endereço": {"Rua": "Rua das Margaridas, 80", "Cidade": "Campinas", "Estado": "SP", "CEP": "13010-000"},
        "Contato": {"Telefone": "(19) 98765-3344", "Email": "juliana.pereira@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 11, "Nome": "Roberto Campos", "CPF": "333.444.555-66", "RG": "33.445.556-7",
        "Data de Nascimento": "08/06/1970", "Cargo": "Consultor Jurídico", "Departamento": "Jurídico",
        "Salário": 12000.00, "Data de Admissão": "03/03/2016", "Status": "Ativo",
        "Endereço": {"Rua": "Av. das Nações, 500", "Cidade": "Belo Horizonte", "Estado": "MG", "CEP": "30000-000"},
        "Contato": {"Telefone": "(31) 99876-5566", "Email": "roberto.campos@empresa.com"},
        "Dependentes": [{"Nome": "Beatriz Campos", "Parentesco": "Cônjuge"}]
    },
    {
        "id": 12, "Nome": "Amanda Santos", "CPF": "888.999.000-11", "RG": "88.990.001-2",
        "Data de Nascimento": "19/11/1987", "Cargo": "Coordenadora de Vendas", "Departamento": "Comercial",
        "Salário": 8500.00, "Data de Admissão": "07/07/2019", "Status": "Ativo",
        "Endereço": {"Rua": "Rua dos Lírios, 25", "Cidade": "Recife", "Estado": "PE", "CEP": "50000-300"},
        "Contato": {"Telefone": "(81) 98765-7788", "Email": "amanda.santos@empresa.com"},
        "Dependentes": []
    },
    {
        "id": 13,"Nome": "Diego Oliveira", "CPF": "123.987.456-00", "RG": "12.398.745-6",
        "Data de Nascimento": "27/09/1993", "Cargo": "Analista de Customer Success", "Departamento": "Atendimento",
        "Salário": 3900.00, "Data de Admissão": "10/10/2021", "Status": "Demitido",
        "Endereço": {"Rua": "Rua das Violetas, 10", "Cidade": "Fortaleza", "Estado": "CE", "CEP": "60000-400"},
        "Contato": {"Telefone": "(85) 99876-9900", "Email": "diego.oliveira@ex-empresa.com"},
        "Dependentes": []
    }
]

#Adcionando novos colaboradores.
anoAtual = float(2025)
def Add_Colaboradores():
    tamanhoLista = len(funcionarios)
    novoId = tamanhoLista + 1
    novoNome = input("Nome do colaborador: ")
    CPF = input("Cpf do colaborador: ")
    RG = input("RG do colaborador: ")
    while True:
        try:
            data_nasc_input = input("Data de nascimento (dd/mm/aaaa): ")
            data_nasc = datetime.strptime(data_nasc_input, "%d/%m/%Y") #Permite organizar a data com numeros e barras.
            idade = anoAtual - data_nasc.year #Subtrai o ano atual - ano de nascimento e retorna a idade do colaborador.
            break
        except ValueError:
            print("Formato inválido! Use dd/mm/aaaa.")
    Cargo = input("Cargo: ")
    Departamento = input("Departamento: ")
    Salario = float(input("Salario: "))
    while True:
        try:
            data_adm_input = input("Data de admissão (dd/mm/aaaa): ")
            datetime.strptime(data_adm_input, "%d/%m/%Y") #Permite organizar a data com numeros e barras.
            break
        except ValueError:
            print("Formato inválido! Use dd/mm/aaaa.")
    Status = input("Status do colaborador: ")
    Endereço = {
            "Rua": input("Rua: "),
            "Cidade": input ("Cidade: "),
            "Estado": input("Estado: "),
            "Cep": input("CEP: ")
        },
    Contato = {
            "Telefone": input("Telefone: "),
            "Email": input("Email: ")
        },
    Dependentes = []
    if input("Possui dependentes (S/SIM)? "):
        while True:
            Nome = input("Insira o nome - (Ou deixe vazio para sair.): ")
            if not Nome:
                break
            Parentesco = input("Parentesco: ")
            Dependentes.append({"Nome": Nome, "Parentesco": Parentesco})
#Inserindo as informações do novo colaborador a lista.
    novoColaborador = {
        "Id": novoId,
        "Nome": novoNome,
        "Cpf": CPF,
        "RG": RG,
        "Data de nascimento": data_nasc_input,
        "Idade": idade, "anos"
        "Cargo": Cargo,
        "Departamento": Departamento,
        "Salario": Salario,
        "Data da admissão": data_adm_input,
        "Status": Status,
        "Endereço": Endereço,
        "Contato": Contato,
        "Dependentes": Dependentes
        }
    funcionarios.append(novoColaborador)
    print(funcionarios)

#Tornar tudo visivel.
def listar_Cadastros():
    for cadastros in funcionarios:
        print('-'*200)
        for chave, valor in cadastros.items():
            print(f"{chave} : {valor}")
Add_Colaboradores()
listar_Cadastros()






