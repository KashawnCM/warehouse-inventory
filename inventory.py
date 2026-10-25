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


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.sku] = item

    def get_item(self,sku):
        return self.items.get(sku)

    def low_stock_report(self):
        print("\nLow Stock Report")
        for item in self.items.values():
            if item.is_low_stock():
                print(item)


# Test it
warehouse = Inventory()

warehouse.add_item(Item("SKU-1001", "Insulin Pens", 40, "A-01-03", 50))
warehouse.add_item(Item("SKU-1002", "Syringes", 500, "B-02-01", 100))
warehouse.add_item(Item("SKU-1003", "Alcohol Swabs", 20, "C-04-02", 75))

pens = warehouse.get_item("SKU-1001")
pens.receive(30)
print(pens)

warehouse.low_stock_report()