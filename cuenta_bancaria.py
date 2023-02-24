class CuentaBancaria:

    # atributos de clase
    saldo = 0
    account_balance = 0
    general_cuentas = []

    def __init__(self, tasa_int, account_balance):
        # atributos de instancia
        self.tasa_int = tasa_int
        self.account_balance = account_balance
        CuentaBancaria.general_cuentas.append(self)

    # Métodos
    # Métodos de Instancia
    def deposito(self, saldo):
        self.account_balance += saldo
        return self

    def retiro(self, saldo):
        if self.account_balance >= saldo:
            self.account_balance -= saldo
        else:
            self.account_balance -= 5
            print(
                f"Fondos insuficientes: cobrando una tarifa de $5")
        return self

    def generar_interes(self):
        if self.account_balance >= 0:
            self.account_balance += self.account_balance * self.tasa_int
        else:
            self.account_balance
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.account_balance}")
        return self

    # Metodos de clase
    @classmethod
    def mostrar_cuentas(cls):
        for cuenta in cls.general_cuentas:
            print('Balance general: $', cuenta.account_balance)


Cuenta1 = CuentaBancaria(0.01, 0)
Cuenta2 = CuentaBancaria(0.01, 0)

Cuenta1.deposito(100).deposito(200).deposito(
    150).retiro(100).generar_interes().mostrar_info_cuenta()

Cuenta2.deposito(300).deposito(150).retiro(
    100).retiro(200).retiro(100).retiro(60).generar_interes().mostrar_info_cuenta()

CuentaBancaria.mostrar_cuentas()
