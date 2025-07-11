from LIST_NUMEROS import lista_numeros


class calculadora:
    def __init__(self):
        self.objlista = lista_numeros()

    def pedir_numero(self):
        while True:
            try:
                numero1 = float(input("numero 1: "))
                numero2 = float(input("numero 2: "))
                return numero1, numero2
            except ValueError:
                print("Por favor, ingresa solo números válidos.")

    def almacenar_numero(self, numero1, numero2):
        dato_numero = [numero1, numero2]
        print(f"Números a guardar: {dato_numero}")
        self.objlista.guardar_numero(dato_numero)
        print(f"Lista actual: {self.objlista.lista_numero}")


# Código principal
if __name__ == "__main__":
    objcalculadora = calculadora()
    auxnum1, auxnum2 = objcalculadora.pedir_numero()
    objcalculadora.almacenar_numero(auxnum1, auxnum2)