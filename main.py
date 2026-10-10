
from contas import ContaCorrente, ContaPoupanca
from pessoas import Cliente
from bancos import Banco


def main():
    banco = Banco("Banco Aprendiz")

    clientes = []
    contas = []

    # Criando 10 clientes e 10 contas
    for i in range(1, 11):
        cliente = Cliente(
            f"Cliente {i}",
            f"cliente{i}@email.com"
        )

        if i % 2 == 0:
            conta = ContaPoupanca(
                i, cliente.nome, saldo=100 * i
            )
        else:
            conta = ContaCorrente(
                i, cliente.nome, saldo=100 * i
            )

        banco.cadastrar_cliente(cliente)
        banco.cadastrar_conta(conta, cliente)

        clientes.append(cliente)
        contas.append(conta)

    print("=== SISTEMA BANCÁRIO ===")
    print(banco)

    # Demonstração de polimorfismo
    print("\n=== CÁLCULO DOS RENDIMENTOS ===")

    for conta in contas:
        print(conta)
        print(
            f"Saldo após cálculo: "
            f"R$ {conta.calcular_rendimento():.2f}\n"
        )

    # Testando depósito e saque
    print("=== OPERAÇÕES ===")
    conta = contas[0]

    conta.depositar(50)
    print(f"Saldo após depósito: R$ {conta.saldo:.2f}")

    conta.sacar(20)
    print(f"Saldo após saque: R$ {conta.saldo:.2f}")

    # Testando exceções
    print("\n=== TESTES DE ERROS ===")

    try:
        conta.depositar(-100)
    except ValueError as erro:
        print(f"Erro no depósito: {erro}")

    try:
        conta.sacar(100000)
    except ValueError as erro:
        print(f"Erro no saque: {erro}")

    try:
        Cliente("Pessoa Teste", "email_invalido")
    except ValueError as erro:
        print(f"Erro no cadastro: {erro}")

    try:
        ContaCorrente(20, "Pessoa Teste", saldo=-50)
    except ValueError as erro:
        print(f"Erro no saldo: {erro}")

    # Demonstração de __repr__ e __eq__
    print("\n=== MÉTODOS ESPECIAIS ===")
    print(repr(clientes[0]))
    print(repr(contas[0]))
    print(f"Contas com o mesmo número são iguais: "
          f"{contas[0] == ContaCorrente(1, 'Outro Titular')}")

    print("\nSistema executado com sucesso!")


if __name__ == "__main__":
    main()
