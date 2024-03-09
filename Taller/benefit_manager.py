from insurance import Insurance
from credit_card import CreditCard
from loyalty_program import LoyaltyProgram


class BenefitManager:
    """
    Gestor de beneficios para los usuarios.
    """
    def __init__(self, recommendation_engine):
        """
        Inicializa el gestor de beneficios.

        :param recommendation_engine: Motor de recomendación.
        """
        self.recommendation_engine = recommendation_engine
        self.is_authenticated = False

    def set_authenticated(self, value):
        """
        Establece el estado de autenticación del usuario.

        :param value: Valor booleano para establecer el estado de autenticación.
        """
        self.is_authenticated = value

    def recommend_benefits(self, user):
        """
        Recomienda beneficios personalizados para un usuario.

        :param user: Usuario para el cual se generan las recomendaciones.
        :return: Lista de beneficios recomendados.
        """
        return self.recommendation_engine.recommend(user)

    def apply_insurance(self, user, insurance_type):
        """
        Aplica un seguro para un usuario.

        :param user: Usuario al cual se aplica el seguro.
        :param insurance_type: Tipo de seguro a aplicar.
        :return: Mensaje indicando si el seguro se aplicó correctamente.
        """
        insurance = Insurance(insurance_type)
        user.insurances.append(insurance)
        return f"Se ha aplicado el seguro {insurance_type} al usuario {user.username}."

    def apply_credit_card(self, user, name, rewards, annual_fee):
        """
        Aplica una tarjeta de crédito para un usuario.

        :param user: Usuario al cual se aplica la tarjeta de crédito.
        :param name: Nombre de la tarjeta de crédito.
        :param rewards: Beneficios asociados a la tarjeta de crédito.
        :param annual_fee: Cuota anual de la tarjeta de crédito.
        :return: Mensaje indicando si la tarjeta de crédito se aplicó correctamente.
        """
        credit_card = CreditCard(name, rewards, annual_fee)
        user.credit_cards.append(credit_card)
        return f"Se ha aplicado la tarjeta de crédito '{name}' al usuario {user.username}."

    def enroll_in_loyalty_program(self, user, program_name):
        """
        Inscribir al usuario en un programa de lealtad.

        :param user: Usuario que se inscribe en el programa de lealtad.
        :param program_name: Nombre del programa de lealtad.
        :return: Mensaje indicando si la inscripción se realizó correctamente.
        """
        loyalty_program = LoyaltyProgram(program_name)
        user.loyalty_programs.append(loyalty_program)
        return f"El usuario {user.username} se ha inscrito en el programa de lealtad '{program_name}'."
