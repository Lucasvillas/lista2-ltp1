from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial

    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def calcular_saldo(self):
        pass
    
    def exibir_informacoes(self):
        return f"Conta {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, saldo_inicial=0, limite_cheque_especial=1000):
        super().__init__(numero, titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo - valor < -self.limite_cheque_especial:
                print("Saldo insuficiente para realizar o saque, considerando o limite do cheque especial.")
            else:
                self.saldo -= valor
        else:
            print("Valor de saque deve ser positivo.")

    def calcular_saldo(self):
        return self.saldo

class ContaPoupanca(ContaBancaria):
    JUROS_MENSAL = 0.05

    def __init__(self, numero, titular, saldo_inicial=0):
        super().__init__(numero, titular, saldo_inicial)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo - valor < 0:
                print("Saldo insuficiente para realizar o saque.")
            else:
                self.saldo -= valor
        else:
            print("Valor de saque deve ser positivo.")

    def calcular_saldo(self):
        self.saldo += self.saldo * ContaPoupanca.JUROS_MENSAL
        return self.saldo

if __name__ == "__main__":
    conta_corrente = ContaCorrente(12345, "João Silva", 500, 1000)
    conta_poupanca = ContaPoupanca(67890, "Maria Oliveira", 2000)

    print(conta_corrente.exibir_informacoes())
    print(conta_poupanca.exibir_informacoes())

    print("\nOperações na Conta Corrente:")
    conta_corrente.depositar(300)
    print(conta_corrente.exibir_informacoes())
    
    conta_corrente.sacar(1000)
    print(conta_corrente.exibir_informacoes())
    
    conta_corrente.sacar(2000)
    print(conta_corrente.exibir_informacoes())

    print("\nOperações na Conta Poupança:")
    conta_poupanca.depositar(500)
    print(conta_poupanca.exibir_informacoes())
    
    conta_poupanca.sacar(1000)
    print(conta_poupanca.exibir_informacoes())
    
    conta_poupanca.sacar(3000)
    print(conta_poupanca.exibir_informacoes())

    conta_poupanca.calcular_saldo()
    print(f"Saldo da conta poupança após juros: R${conta_poupanca.calcular_saldo():.2f}")
