from benefit import Benefit


class LoyaltyProgram(Benefit):
    """
    Clase que representa un programa de lealtad, que hereda de la clase Benefit.
    """
    def __init__(self, name, rewards, membership_fee):
        """
        Inicializa un programa de lealtad con su nombre, recompensas y cuota de membresía.

        :param name: Nombre del programa de lealtad.
        :param rewards: Recompensas asociadas al programa de lealtad.
        :param membership_fee: Cuota de membresía del programa de lealtad.
        """
        super().__init__(name, rewards)
        self.membership_fee = membership_fee

    def apply_membership(self, user):
        """
        Aplica la membresía del programa de lealtad a un usuario.

        :param user: Usuario al cual se aplica la membresía.
        :return: Mensaje indicando si la membresía se aplicó correctamente.
        """
        user.loyalty_programs.append(self)
        return f"Se ha aplicado la membresía del programa de lealtad '{self.name}' al usuario {user.username}."

    def calculate_membership_discount(self, user, purchase_amount):
        """
        Calcula el descuento de membresía aplicable a una compra para un usuario.

        :param user: Usuario para el cual se calcula el descuento.
        :param purchase_amount: Monto total de la compra.
        :return: Descuento de membresía aplicable.
        """
        if self in user.loyalty_programs:
            discount = self.membership_fee * 0.1  # Por ejemplo, un 10% del costo de la membresía como descuento
            return min(discount, purchase_amount)
        else:
            return 0
