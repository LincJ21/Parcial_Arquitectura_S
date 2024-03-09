class UserInterface:
    def __init__(self, authentication_service, benefit_manager):
        self.authentication_service = authentication_service
        self.benefit_manager = benefit_manager
        self.is_authenticated = False

    def login(self, username, password):
        if self.authentication_service.authenticate(username, password):
            print("Inicio de sesión exitoso.")
            self.is_authenticated = True
        else:
            print("Error de autenticación.")
            self.is_authenticated = False

    def logout(self):
        print("Cierre de sesión exitoso.")
        self.is_authenticated = False
