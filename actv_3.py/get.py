class CuentaBancaria:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    # GET
    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    # SET
    def set_saldo(self, monto):
        if monto >= 0:
            self.__saldo = monto
        else:
            print("El saldo no puede ser negativo.")

# Uso
cuenta = CuentaBancaria("123-456", 1000)

print("Número de cuenta:", cuenta.get_numero())
print("Saldo inicial:", cuenta.get_saldo())

cuenta.set_saldo(1500)
print("Saldo actualizado:", cuenta.get_saldo())