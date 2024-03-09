class Invoice:
    """
    Clase que representa una factura.
    """
    def __init__(self, user, amount, items):
        """
        Inicializa una factura con el usuario, el monto y los elementos.

        :param user: Usuario al que se emite la factura.
        :param amount: Monto total de la factura.
        :param items: Elementos o productos de la factura.
        """
        self.user = user
        self.amount = amount
        self.items = items

    def calculate_total(self):
        """
        Calcula el total de la factura sumando los montos de los elementos.

        :return: Total de la factura.
        """
        total = sum(item.amount for item in self.items)
        return total

    def generate_invoice(self):
        """
        Genera el formato de la factura.

        :return: Cadena de texto con la factura generada.
        """
        invoice_str = f"Factura para {self.user.name}:\n"
        for item in self.items:
            invoice_str += f"- {item.name}: ${item.amount}\n"
        invoice_str += f"Total: ${self.amount}\n"
        return invoice_str

    def print_invoice(self):
        """
        Imprime la factura generada.
        """
        print(self.generate_invoice())
