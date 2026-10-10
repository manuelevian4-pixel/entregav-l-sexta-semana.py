
from abc import ABC, abstractmethod


class Conta(ABC):
    """Representa uma conta bancária genérica."""

    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("O número da conta deve ser um inteiro positivo.")
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome do titular não pode ficar vazio.")
        self._titular = valor.strip()

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O saldo precisa ser numérico.")
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    def depositar(self, valor):
        """Adiciona dinheiro à conta."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O depósito precisa ser numérico.")
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")
        self.saldo += valor

    def sacar(self, valor):
        """Retira dinheiro, se houver saldo suficiente."""
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("O saque precisa ser numérico.")
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento conforme o tipo de conta."""
        pass

    def __str__(self):
        return (
            f"Conta {self.numero} | Titular: {self.titular} "
            f"| Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"numero={self.numero}, titular={self.titular!r}, "
            f"saldo={self.saldo})"
        )

    def __eq__(self, outra):
        if not isinstance(outra, Conta):
            return NotImplemented
        return self.numero == outra.numero

class ContaCorrente(Conta):
    """Conta bancária que cobra uma tarifa de manutenção."""

    def __init__(self, numero, titular, saldo=0, tarifa=15):
        super().__init__(numero, titular, saldo)
        self.tarifa = tarifa

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("A tarifa precisa ser numérica.")
        if valor < 0:
            raise ValueError("A tarifa não pode ser negativa.")
        self._tarifa = valor

    def calcular_rendimento(self):
        """Retorna o saldo após descontar a tarifa."""
        return max(0, self.saldo - self.tarifa)

    def __str__(self):
        return f"{super().__str__()} | Tarifa: R$ {self.tarifa:.2f}"


class ContaPoupanca(Conta):
    """Conta bancária que calcula rendimento percentual."""

    def __init__(self, numero, titular, saldo=0, taxa=0.01):
        super().__init__(numero, titular, saldo)
        self.taxa = taxa

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("A taxa precisa ser numérica.")
        if not 0 <= valor <= 1:
            raise ValueError("A taxa deve estar entre 0 e 1.")
        self._taxa = valor

    def calcular_rendimento(self):
        """Calcula o saldo com o rendimento percentual."""
        return self.saldo * (1 + self.taxa)

    def __str__(self):
        return f"{super().__str__()} | Taxa: {self.taxa:.1%}"


