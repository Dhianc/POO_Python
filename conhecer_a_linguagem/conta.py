"""
Quarto código do curso Python e orientação a objetos
Aula -> Python: entendendo a Orientação a Objetos

"""

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero       # torna o atributo privado com __, para ser usado somente através dos métodos
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor
        print(f"Novo saldo de {self.__saldo} do titular {self.__titular}")

    def __pode_sacar(self, valor_a_sacar):    # torna o método privado com __
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} pasosu o limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property   # propriedade GET
    def saldo(self):
        return self.__saldo    # um get sempre tem retorno

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter   # propriedade SET
    def limite(self, limite):
         self.__limite = limite

    @staticmethod   # acessível sem ter um objeto da classe Conta
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
