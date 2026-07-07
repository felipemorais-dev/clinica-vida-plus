class Paciente:
    """
    Representa um paciente da clínica.
    Define os dados que cada paciente possui (nome, idade, telefone)
    e os comportamentos associados a ele.
    """
    def __init__ (self, nome, idade, telefone):
        """
        Inicializa um novo paciente associando os atributos
        nome, idade e telefone ao objeto criado.
        """
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def exibir(self):
        """
        Exibe os dados do paciente formatado. 
        A responsabilidade de formatar a exibição pertence ao próprio
        objeto Paciente - qualquer alteração no formato é feita aqui,
        sem impactar o restante do código. (encapsulamento)
        """
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nTelefone: {self.telefone}")

import sqlite3
class Clinica:
    """
    Representa o sistema de gestão da clínica.
    Centraliza a lista de pacientes e todas as operações sobre ela,
    garantindo que os dados só sejam manipulados através dos métodos 
    definidos nesta classe.
    """
    def __init__(self):
        """
        Inicializa o sistema conectando ao banco de dados e
        criando a tabela de pacientes caso ainda não exista.
        """
        self.conexao = sqlite3.connect("clinica.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                telefone TEXT NOT NULL
            )                
        """)
        self.conexao.commit()

    def cadastrar_pacientes(self, paciente):
        """
        Recebe um objeto Paciente e o insere no banco de dados.
        Separado da coleta de dados para permitir que o cadastro 
        seja acionado por diferentes fontes no futuro
        (input do usuário, arquivo, API).
        """
        self.cursor.execute("""
            INSERT INTO pacientes (nome, idade, telefone )
            VALUES (?, ?, ?)
        """, (paciente.nome, paciente.idade, paciente.telefone))
        self.conexao.commit()
        print("Paciente cadastrado com sucesso!")

    def coletar_e_cadastrar(self):
        """
        Coleta os dados do paciente via input e aciona o cadastro.
        Separando do método cadastrar_pacientes para isolar a responsabilidade
        de coleta de dados da responsabilidade de persistência - 
        facilitando futuras integrações com banco de dados.
        """
        nome = input("Nome do paciente: ")
        try:
            idade = int(input("Idade: "))
        except ValueError:
                print("Idade inválida. Digite apenas números.")
                return
        telefone  = input("Telefone: ")
        paciente = Paciente(nome, idade, telefone)
        self.cadastrar_pacientes(paciente)
        

    def ver_estatisticas(self):
        """
        Consulta o banco de dados e calcula estatísticas dos pacientes:
        total, médida de idade, paciente mais novo e mais velho.
        Utiliza funções nativas do Python (sum, min, max) com lambda
        para determinar o critério de comparação pelo índice de idade
        nas tuplas retornadas pelo banco.
        """
        self.cursor.execute("SELECT * FROM pacientes")
        pacientes = self.cursor.fetchall()
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return
        total = len(pacientes)
        media_idade = sum(p[2] for p in pacientes) / total 
        # Lambda define o critério de comparação: índice p[2] corresponde à idade na tupla
        mais_novo = min(pacientes, key=lambda p: p[2])
        mais_velho = max(pacientes, key=lambda p: p[2])
        print(f"Total de pacientes: {total}")
        print(f"Idade média: {media_idade:.1f} anos")
        print(f"Mais novo: {mais_novo[1]} ({mais_novo[2]} anos)")
        print(f"Mais velho: {mais_velho[1]} ({mais_velho[2]} anos)")

    def buscar_pacientes(self):
        """
        Solicita um nome via input e consulta o banco de dados
        buscando correspondências parciais, sem distinção de maiúsculas
        e minúsculas. Exibe todos os pacientes cujo nome contenha
        o termo digitado.
        """
        nome_busca = input("Digite o nome do paciente: ").lower()
        self.cursor.execute("SELECT * FROM pacientes WHERE LOWER(nome) LIKE ?",
                            (f"%{nome_busca}%",)
        )
        encontrados = self.cursor.fetchall()
        if len(encontrados) == 0:
            print("Nenhum paciente encontrado.")
        else:
            for p in encontrados:
                print(f"\nNome: {p[1]} | Idade: {p[2]} | Telefone: {p[3]}")

    def listar_pacientes(self):
        """
        Consulta todos os pacientes cadastrados no banco de dados
        e exibe os registros enumerados a partir do índice 1,
        sem aplicar nenhum filtro.
        """     
        self.cursor.execute("SELECT * FROM pacientes")
        pacientes = self.cursor.fetchall()
        if len(pacientes) == 0:
            print("Nenhum paciente encontrado.")
            return
        
        print("\n===== LISTA DE PACIENTES =====\n")
        for i, p in enumerate(pacientes, start=1):
            print(f"{i}. {p[1]} | {p[2]} anos | {p[3]}") 

    def fechar_conexao(self):
        """
        Encerra a conexão com o banco de dados.
        Deve ser chamado ao finalizar o programa para 
        liberar os recursos corretamente.
        """
        self.conexao.close()

# Instancia o sistema da clínica uma única vez, fora do loop.
# Isso garante que os dados cadastrados persistam durante
# toda a execução do programa - se instanciado dentro do loop,
# todos os registros seriam perdidos a cada iteração.
clinica = Clinica()

# Loop principal do menu - mantém o sistema ativo até o usuário escolher sair (opção 5)
while True:
    print("\n===== SISTEMA CLÍNICA VIDA+ =====")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clinica.coletar_e_cadastrar()
    elif opcao == "2":
        clinica.ver_estatisticas()
    elif opcao == "3":
        clinica.buscar_pacientes()
    elif opcao == "4":
        clinica.listar_pacientes()
    elif opcao == "5":
        clinica.fechar_conexao()
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")