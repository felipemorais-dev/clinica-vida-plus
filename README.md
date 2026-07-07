# clinica-vida-plus
Sistema de gestão de clínica desenvolvido em Python, aplicando conceitos de 
Programação Orientada a Objetos (POO).

## Descrição 

O sistema permite gerenciar pacientes de uma clínica médica via terminal, 
oferecendo funcionalidades de cadastro, busca, listagem e estatísticas.
O projeto está em evolução contínua, com integração de banco de dados, 
e interface web planejadas para a próxima etapa.

## Tecnologias

- Python 3.14.4
- Programação Orientada a Objetos (POO)
- SQLite3 (banco de dados local)

## Como executar 

1. Clone o repositório:
    git clone https://github.com/felipemorais-dev/clinica-vida-plus.git

2. Acesse a pasta do projeto:
    cd clinica-vida-plus

3. Execute o sistema:
    python clinica.py

## Funcionalidades

- Cadastro de pacientes (nome, idade, telefone)
- Listagem de todos os pacientes cadastrados
- Busca de paciente por nome (parcial e sem distinção de maiúsculas)
- Estatísticas: total de pacientes, média de idade, mais novo e mais velho

## Estrutura do projeto

│
|-- clinica.py       # Código principal com as classes Paciente e Clinica
|-- README.md        # Documentação do projeto

## Próximos passos

- [x] Integração com banco de dados SQLite
- [] Expansão das funcionalidades: cadastro de médicos e agendamentos
- [] Interface web com Flask

## Autor

Felipe Morais - github.com/felipemorais-dev