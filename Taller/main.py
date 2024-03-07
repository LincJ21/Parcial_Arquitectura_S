from user import User
from invoice import Invoice
from authentication_service import LDAPAuthenticationService
from benefit_manager import BenefitManager
from recommendation_engine import BasicRecommendationEngine
from user_interface import UserInterface

def main():
    authentication_service = LDAPAuthenticationService()
    recommendation_engine = BasicRecommendationEngine()
    benefit_manager = BenefitManager(recommendation_engine)
    user_interface = UserInterface(authentication_service, benefit_manager)
    
    # Pedir al usuario que ingrese sus datos
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    name = input("Ingrese su nombre: ")
    
    # Crear instancia de usuario con los datos ingresados por el usuario
    user = User(username, password, name)
    
    # Intentar iniciar sesión con los datos ingresados por el usuario
    user_interface.login(username, password)
    
    # Autenticación LDAP con los datos ingresados por el usuario
    if authentication_service.authenticate(username, password):
        print("Autenticación exitosa")
    else:
        print("Autenticación fallida")

if __name__ == "__main__":
    main()
