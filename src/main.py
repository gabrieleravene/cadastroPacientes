# funcionalidades do sistema:
#- Cadastrar paciente: nome, cpf, data de nascimento, contato
# Buscar pacientes;
# Visualizar pacientes cadastrados;
# Excluir cadastro de pacientes;
from idlelib.run import exit_now
# tkinter p/ interface gráfica ?

# criar lista p/ nomes, lista p/ cpf, lista p/ dn, lista p/ contato
pacientes = []

def cadastrar_pacientes():
    """ Função para cadastrar pacientes """
    nome = input('Digite o nome completo: ')
    cpf = input('Digite o CPF: ')
    dn = input('Digite a data de nascimento: ')
    contato = input('Digite um telefone para contato: ')

    paciente = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": dn,
        "contato": contato
    }

    pacientes.append(paciente)

    print("Paciente cadastrado com sucesso.")

    mais_cadastros = input('Deseja realizar mais cadastros? ')
    if mais_cadastros == 'SIM':
        cadastrar_pacientes()
    else:
        exibir_menu()

def ver_cadastros():
    """ Função para exibir lista de cadastro """
    for paciente in pacientes:
        print(paciente)
    continuar = input('Deseja voltar ao menu?')
    if continuar == 'SIM':
        exibir_menu()

def buscar_paciente():
    """ Função para buscar paciente """
    paciente_procurado = input('Digite o CPF do paciente que deseja consultar: ')
    encontrado = False
    for paciente in pacientes:
        if paciente["cpf"] == paciente_procurado:
            encontrado = True
            print('Paciente encontrado.')
            print(paciente)
    if not encontrado:
        print('Paciente não cadastrado.')
        realizar_cadastro = input('Deseja realizar o cadastro? ')
        if realizar_cadastro == 'SIM':
            cadastrar_pacientes()
        else:
            exibir_menu()

def eliminar_cadastro():
    """ Função para eliminar o paciente do sistema de cadastro """
    paciente_eliminado = input("Digite o CPF do paciente a ser eliminado: ")
    encontrado = False # variável para controle

    for paciente in pacientes:
        if paciente["cpf"] == paciente_eliminado:
            pacientes.remove(paciente)
            print('Cadastro eliminado.')
            encontrado = True
            break

    if not encontrado:
        print('Paciente não encontrado.')

    voltar_menu = input('Deseja voltar ao menu?')
    if voltar_menu == 'SIM':
        exibir_menu()

def exibir_menu():
    """ Função que exibe opções para usuário escolher sua ação """
    print("Opção 1: Cadastrar de pacientes \n"
    "Opção 2: Ver lista de cadastros \n"
    "Opção 3: Procurar paciente \n"
    "Opção 4: Eliminar cadastro \n"
    "Opção 5: Encerrar  o programa")
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
       cadastrar_pacientes()

    if opcao == 2:
       ver_cadastros()

    if opcao == 3:
        buscar_paciente()

    if opcao == 4:
        eliminar_cadastro()

    if opcao == 5:
        print('Programa encerrado.')

exibir_menu()