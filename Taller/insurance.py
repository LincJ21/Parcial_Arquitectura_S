from benefit import Benefit

class Insurance(Benefit):
    """
    Clase que representa un seguro, que hereda de la clase Benefit.
    """
    def __init__(self, name, coverage, premium):
        """
        Inicializa un seguro con su nombre, cobertura y prima.

        :param name: Nombre del seguro.
        :param coverage: Cobertura del seguro.
        :param premium: Prima del seguro.
        """
        super().__init__(name, rewards=None)
        self.coverage = coverage
        self.premium = premium
