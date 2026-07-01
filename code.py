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

class Clinica:
    """
    Representa o sistema de gestão da clínica.
    Centraliza a lista de pacientes e todas as operações sobre ela,
    garantindo que os dados só sejam manipulados através dos métodos 
    definidos nesta classe.
    """
    def __init__(self):
        """
        Inicializa o sistema com uma lista vazia de pacientes.
        Todos os pacientes cadastrados serão armazenados aqui.
        """
        self.pacientes = []

    def cadastrar_pacientes(self, paciente):
        """
        Recebe um objeto Paciente e o adiciona à lista do sistema.
        Separando da coleta de dados para permitir que o cadastro 
        seja acionado por diferentes fontes no futuro
        (input do usuário, arquivo, bando de dados, API).
        """
        self.pacientes.append(paciente)

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
        print("Paciente cadastrado com sucesso!")

    def ver_estatisticas(self):
        """
        Calcula e exibe estatísticas dos pacientes cadastrados:
        total, média de idade, paciente mais novo e mais velho.
        Utiliza funções nativas do Python (sum, min, max) com lambda
        para determinar o critério de comparação entre objetos Paciente.
        """
        if len(self.pacientes) == 0:
            print("Nenhum paciente cadastrado.")
            return
        total = len(self.pacientes)
        media_idade = sum(p.idade for p in self.pacientes) / total 
        # Lambda define o critério de comparação: o atributo idade de cada objeto Paciente 
        mais_novo = min(self.pacientes, key=lambda p: p.idade)
        mais_velho = max(self.pacientes, key=lambda p: p.idade)
        print(f"Total de pacientes: {total}")
        print(f"Idade média: {media_idade:.1f} anos")
        print(f"Mais novo: {mais_novo.nome} ({mais_novo.idade} anos)")
        print(f"Mais velho: {mais_velho.nome} ({mais_velho.idade} anos)")

    def buscar_pacientes(self):
        """
        Solicita um nome via input e percorre a lista de pacientes
        buscando correspondências parciais, sem distinção de maiúsculas
        e minúsculas. Exibe todos os pacientes cujo nome contenha
        o termo digitado.
        """
        nome_busca = input("Digite o nome do paciente: ").lower()
        encontrados = [p for p in self.pacientes if nome_busca in p.nome.lower()]
        if len(encontrados) == 0:
            print("Nenhum paciente encontrado.")
        else:
            for p in encontrados:
                print(f"\nNome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone}")

    def listar_pacientes(self):
        """
        Percorre a lista completa de pacientes e exibe todos os registros
        enumerados a partir do índice 1, sem aplicar nenhum filtro.
        """
        if len(self.pacientes) == 0:
            print("Nenhum paciente encontrado.")
            return
        
        print("\n===== LISTA DE PACIENTES =====\n")
        for i, p in enumerate(self.pacientes, start=1):
            print(f"{i}. {p.nome} | {p.idade} anos | {p.telefone}") 

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
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

