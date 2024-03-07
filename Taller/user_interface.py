class UserInterface:
    def __init__(self, authentication_service, benefit_manager):
        self.authentication_service = authentication_service
        self.benefit_manager = benefit_manager

    def login(self, username, password):
        if self.authentication_service.authenticate(username, password):
            # Lógica para mostrar la interfaz de usuario
            pass
        else:
            print("Error de autenticación")
