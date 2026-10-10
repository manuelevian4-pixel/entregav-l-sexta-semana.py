
class Banco:
    """Gerencia clientes e contas bancárias."""
    def __init__(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do banco não pode ficar vazio.")

        self.nome = nome.strip()
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, cliente):
        from pessoas import Cliente

        if not isinstance(cliente, Cliente):
            raise TypeError("O cadastro exige um objeto Cliente.")
        if cliente not in self.clientes:
            self.clientes.append(cliente)

    def cadastrar_conta(self, conta, cliente):
        if cliente not in self.clientes:
            raise ValueError("Cadastre o cliente antes da conta.")
        if any(c.numero == conta.numero for c in self.contas):
            raise ValueError("Já existe uma conta com esse número.")

        cliente.adicionar_conta(conta)
        self.contas.append(conta)

    def __str__(self):
        return (
            f"Banco {self.nome} | "
            f"Clientes: {len(self.clientes)} | "
            f"Contas: {len(self.contas)}"
        )

    def __repr__(self):
        return f"Banco(nome={self.nome!r})"

