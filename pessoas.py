
import re


class Cliente:
    """Representa um cliente do banco."""

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.contas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str):
            raise ValueError("O e-mail precisa ser um texto.")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", valor):
            raise ValueError("Formato de e-mail inválido.")
        self._email = valor

    def adicionar_conta(self, conta):
        from contas import Conta

        if not isinstance(conta, Conta):
            raise TypeError("É necessário informar uma conta bancária.")
        if conta not in self.contas:
            self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome} | E-mail: {self.email}"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r})"
