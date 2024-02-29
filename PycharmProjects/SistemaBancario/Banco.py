nome_empresa = "BANKCARD"

menu = f"""
{nome_empresa.strip().center(60, "_")}

Qual operação deseja realizar hoje?
d - depósito
s - saque
e - extrato
u - criar usuário
c - criar conta
lc - listar contas
lu - listar usuarios
q - sair
"""

usuarios = []

contas = []

cpfs = set()

conta = {
    'saldo': 0,
    'quantidade_saques': 3,
    'limite_maximo_saque': 500
}

historico = []


def deposito(valor, conta, /):
    saldo = conta.get('saldo')
    if valor > 0:
        saldo += valor
        conta['saldo'] = saldo
        historico.append(('Deposito', valor))
    else:
        print('O depósito precisa ser um valor positivo')


def saque(*, valor, conta):
    saldo = conta.get('saldo')
    if (saldo - valor) < 0:
        print('Saldo insuficiente')
    elif conta.get('quantidade_saques') <= 0:
        print('Atingiu o número máximo de saques diários')
    elif valor > 500:
        print(f'Limite máximo para saque é de R${conta['limite_maximo_saque']}')
    else:
        saldo -= valor
        historico.append(('Saque', valor))
        conta['saldo'] = saldo
        conta['quantidade_saques'] -= 1


def extrato(historico_conta):
    # if not historico ou if historico == []
    if len(historico_conta) == 0:
        print('Não há extrato a ser exibido')
    for funcao, valor in historico_conta:
        print(f'{funcao} no valor de R${valor:.2f}')


def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf_formatado = tratar_dados_documento(cpf)
    if cpf not in cpfs:
        usuarios.append(
            {"nome": nome, "data de nascimento": data_nascimento, "cpf": cpf_formatado, "endereço": endereco})
        cpfs.add(cpf)
    else:
        print("Usuário já cadastrado")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Não há usuários cadastrados")
    else:
        for usuario in usuarios:
            print(usuario)


def filtrar_usuarios(documento):
    for u in usuarios:
        if u.get("cpf") == documento:
            return u
    print("Usuário não encontrado")


def criar_conta_corrente(usuario):
    agencia = "0001"
    if len(contas) == 0:
        numero_conta = 1
    else:
        numero_conta = contas[-1].get("numero conta") + 1

    contas.append(
        {
            "agencia": agencia,
            "numero conta": numero_conta,
            "usuario": usuario,
            'saldo': 0,
            'quantidade_saques': 3,
            'limite_maximo_saque': 500
        }
    )


def listar_contas():
    if len(contas) == 0:
        print("Não há contas cadastradas")
    else:
        for conta in contas:
            print(conta)


def tratar_dados_documento(documento):
    documento_formatado = str(documento).replace(".", "").replace("-", "").strip()
    if len(documento_formatado) != 11:
        print("Documento inválido")
        exit()
    return documento_formatado



while True:

    print(menu)

    opcao = input('Digite a operação: ')
    match opcao:
        case 'd':
            conta = int(input("Digite o número da conta"))
            valor = float(input("Digite o valor para depósito: "))
            deposito(valor, contas[conta-1])
        case 's':
            conta = int(input("Digite o número da conta"))
            valor = float(input("Digite o valor para saque: "))
            saque(valor=valor, conta=contas[conta-1])
        case 'e':
            extrato(historico_conta=historico)
        case 'u':
            nome = input("Digite o nome do usuário")
            data_nascimento = input("Digite a data de nascimento")
            cpf = input("Digite o cpf")
            endereco = input("Digite o endereco")
            criar_usuario(nome, data_nascimento, cpf, endereco)
        case 'c':
            documento = input("Digite o cpf para criar a conta")
            usuario = filtrar_usuarios(documento)
            criar_conta_corrente(usuario)
        case 'lc':
            listar_contas()
        case 'lu':
            listar_usuarios()
        case 'q':
            break
        case _:
            print('Opção inválida, tente novamente')

