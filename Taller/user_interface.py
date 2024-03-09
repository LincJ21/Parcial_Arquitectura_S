from user import User
from benefit_manager import BenefitManager

class UserInterface:
    def __init__(self, authentication_service, benefit_manager):
        self.authentication_service = authentication_service
        self.benefit_manager = benefit_manager
        self.is_authenticated = False

    def login(self, username, password):
        if self.authentication_service.authenticate(username, password):
            print("Inicio de sesión exitoso.")
            self.benefit_manager.set_authenticated(True)  # Agregar este método en BenefitManager
        else:
            print("Error de autenticación.")


    def logout(self):
        print("Cierre de sesión exitoso.")
        self.is_authenticated = False

    def load_users_from_file(self, filename):
        """
        Carga usuarios desde un archivo.

        :param filename: El nombre del archivo que contiene los datos de los usuarios.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                username, password, name = line.strip().split(',')
                user = User(username, password, name)
                self.authentication_service.add_user(user)


# benefit.py
class Benefit:
    def __init__(self, name, rewards):
        self.name = name
        self.rewards = rewards
        self.loans = {}  # Diccionario para almacenar los préstamos

    def register_loan(self, user, amount):
        """
        Registra un préstamo para un usuario dado.

        :param user: El usuario que solicita el préstamo.
        :param amount: La cantidad prestada.
        """
        if self.benefit_manager.user_interface.is_authenticated:
            if user.username in self.benefit_manager.authentication_service.logged_users:
                if user.name in self.loans:
                    self.loans[user.name] += amount
                else:
                    self.loans[user.name] = amount
                print(f"Préstamo de {amount} registrado para {user.name}")
            else:
                print("Error: Usuario no autenticado.")
        else:
            print("Error: Usuario no autenticado.")


# authentication_service.py
class AuthenticationService:
    def __init__(self):
        self.users = []
        self.logged_users = set()

    def add_user(self, user):
        self.users.append(user)

    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_users.add(user.username)
                return True
        return False
