class Item:
    def __init__(self, sku, name, quantity, location, reorder_point):

        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.location = location
        self.reorder_point = reorder_point

    def is_low_stock(self):
        return self.quantity <= self.reorder_point

    def receive(self, amount):
        self.quantity += amount

    def ship(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print("not enough in stock")

    def __str__(self):
        return f"{self.sku} | {self.name} | Qty: {self.quantity} | Loc: {self.location} | ReorderPoint: {self.reorder_point}"


# Test it
item = Item("SKU-1001", "Insulin pens", 40, "A-01-03", 50)
print(item)
print(f"Low stock? {item.is_low_stock()}")

item.receive(20)
print(item)

item.ship(100)
print(item)
