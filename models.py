class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if quantity == 0:
            raise ValueError

        return self.quantity >= quantity

    def buy(self, quantity):
        if not self.check_quantity(quantity):
            raise ValueError

        self.quantity -= quantity


    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        if quantity == 0:
            raise ValueError

        if product in self.products:
            quantity = self.products.get(product) + quantity

        self.products.update({product: quantity})

    def remove_product(self, product: Product, quantity=None):
        if product not in self.products:
            return

        if quantity is None:
            del self.products[product]
            return

        current_quantity = self.products.get(product)
        if current_quantity <= quantity:
            del self.products[product]
            return

        self.products.update({product: current_quantity - quantity})

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        total_sum = 0.0
        for product in self.products.keys():
            total_sum += self.products.get(product) * product.price

        return total_sum

    def buy(self):
        for product in self.products.keys():
            product.buy(self.products.get(product))

        self.clear()