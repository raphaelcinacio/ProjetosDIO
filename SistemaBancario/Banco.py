nome_empresa = "BANKCARD"

menu = f"""
{nome_empresa.strip().center(60, "_")}

Qual operação deseja realizar hoje?
d - Depósito
s - saque
e - extrato
q - sair
"""

conta = {
    'saldo': 0,
    'quantidade_saques': 3,
    'limite_maximo_saque': 500
}

historico = []


def deposito(valor, conta):
    saldo = conta.get('saldo')
    if valor > 0:
        saldo += valor
        conta['saldo'] = saldo
        historico.append(('Deposito', valor))
    else:
        print('O depósito precisa ser um valor positivo')


def saque(valor, conta):
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


while True:

    print(menu)

    opcao = input('Digite a operação: ')
    match opcao:
        case 'd':
            valor = float(input("Digite o valor para depósito: "))
            deposito(valor, conta)
        case 's':
            valor = float(input("Digite o valor para saque: "))
            saque(valor, conta)
        case 'e':
            extrato(historico)
        case 'q':
            break
        case _:
            print('Opção inválida, tente novamente')
