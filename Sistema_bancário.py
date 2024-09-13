import random

class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.historico = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 500:
            print("Valor do saque excede o limite diário.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            self.saques_diarios += 1

    def extrato(self):
        print(f"Extrato da Conta {self.numero_conta} - Titular: {self.titular}")
        for movimentacao in self.historico:
            print(movimentacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

def menu():
    print("\nBem-vindo ao Robson_Bank!")
    print("1. Cadastrar nova conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Extrato")
    print("5. Sair")
    return int(input("Digite a opção desejada: "))

# Criação da conta
titular = input("Digite o nome do titular da conta: ")
numero_conta = random.randint(1, 10)
conta = ContaBancaria(titular, numero_conta)

# Loop principal do sistema
while True:
    opcao = menu()

    if opcao == 1:
        print("Conta já cadastrada.")  # Opção de cadastro só disponível uma vez
    elif opcao == 2:
        valor = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor)
    elif opcao == 3:
        valor = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor)
    elif opcao == 4:
        conta.extrato()
    elif opcao == 5:
        print("Obrigado por utilizar as nossas agências!")
        break
    else:
        print("Opção inválida.")