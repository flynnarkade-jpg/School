class Product:
    def __init__(self, sku, name, price, stock=0):
        self.sku = sku
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, quantity):
        self.stock += quantity

    def sell(self, quantity):
        if quantity > self.stock:
            raise ValueError(f"Not enough stock for {self.name}")
        self.stock -= quantity
        return self.price * quantity

    def apply_discount(self, percent):
        self.price = round(self.price * (1 - percent / 100), 2)

    def __str__(self):
        return f"{self.sku} - {self.name}: ${self.price:.2f} ({self.stock} in stock)"


if __name__ == "__main__":
    item = Product("SKU-001", "USB Cable", 9.99, stock=50)
    print(item)

    total = item.sell(3)
    print(f"Sold 3 for ${total:.2f}")

    item.apply_discount(15)
    item.restock(20)
    print(item)
