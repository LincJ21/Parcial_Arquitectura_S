class Location:
    """
    Clase para gestionar la ubicación de un usuario.
    """
    def __init__(self, user, city=None, country=None, neighborhood=None, street=None):
        """
        Inicializa una instancia de ubicación.

        :param user: El usuario al que se asocia esta ubicación.
        :param city: Ciudad de la ubicación (opcional).
        :param country: País de la ubicación (opcional).
        :param neighborhood: Barrio de la ubicación (opcional).
        :param street: Calle de la ubicación (opcional).
        """
        self.user = user
        self.city = city
        self.country = country
        self.neighborhood = neighborhood
        self.street = street

    def set_location(self, city, country, neighborhood, street):
        """
        Establece la ubicación del usuario.

        :param city: Ciudad de la ubicación.
        :param country: País de la ubicación.
        :param neighborhood: Barrio de la ubicación.
        :param street: Calle de la ubicación.
        """
        self.city = city
        self.country = country
        self.neighborhood = neighborhood
        self.street = street
        print(f"Ubicación actualizada para el usuario {self.user.username}: Ciudad {city}, País {country}, Barrio {neighborhood}, Calle {street}")

    def get_location(self):
        """
        Obtiene la ubicación actual del usuario.

        :return: Tupla (ciudad, país, barrio, calle) de la ubicación.
        """
        return self.city, self.country, self.neighborhood, self.street
