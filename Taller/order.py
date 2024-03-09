class Order:
    def __init__(self, user, items=None):
        self.user = user
        self.items = items or []

    def add_item(self, item):
        """
        Agrega un artículo a la orden.

        :param item: El artículo a añadir.
        """
        self.items.append(item)
        print(f"Artículo '{item}' agregado a la orden.")

    def remove_item(self, item):
        """
        Elimina un artículo de la orden.

        :param item: El artículo a eliminar.
        """
        if item in self.items:
            self.items.remove(item)
            print(f"Artículo '{item}' eliminado de la orden.")
        else:
            print(f"El artículo '{item}' no está en la orden.")

    def view_order(self):
        """
        Muestra los artículos en la orden.
        """
        if self.items:
            print("Artículos en la orden:")
            for item in self.items:
                print(item)
        else:
            print("La orden está vacía.")

