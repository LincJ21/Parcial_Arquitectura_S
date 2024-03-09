from benefit import Benefit

class CreditCard(Benefit):
    """
    Clase que representa una tarjeta de crédito, que hereda de la clase Benefit.
    """
    def __init__(self, name, rewards, annual_fee, username, password, user_name):
        """
        Inicializa una tarjeta de crédito con su nombre, recompensas, cuota anual y credenciales de usuario.

        :param name: Nombre de la tarjeta de crédito.
        :param rewards: Recompensas asociadas a la tarjeta de crédito.
        :param annual_fee: Cuota anual de la tarjeta de crédito.
        :param username: Nombre de usuario para la tarjeta de crédito.
        :param password: Contraseña de la tarjeta de crédito.
        :param user_name: Nombre del titular de la tarjeta de crédito.
        """
        super().__init__(name, rewards)
        self.annual_fee = annual_fee
        self.username = username
        self.password = password
        self.user_name = user_name
        self.credit_card_number = None
        self.expiry_date = None

    def add_credit_card_info(self, credit_card_number, expiry_date):
        """
        Añade información de la tarjeta de crédito.

        :param credit_card_number: Número de la tarjeta de crédito.
        :param expiry_date: Fecha de vencimiento de la tarjeta de crédito.
        """
        self.credit_card_number = credit_card_number
        self.expiry_date = expiry_date
        
    def view_credit_card_info(self):
        """
        Muestra la información de la tarjeta de crédito.
        """
        if self.credit_card_number and self.expiry_date:
            print("Información de la tarjeta de crédito:")
            print("Número de tarjeta de crédito:", self.credit_card_number)
            print("Fecha de vencimiento:", self.expiry_date)
        else:
            print("No hay información de tarjeta de crédito disponible.")
