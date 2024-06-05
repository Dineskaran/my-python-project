class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total_price(self):
        total_price = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_price

    def free_delivery(self):
        total_price = self.calculate_total_price()
        return total_price >= 1000

    def tex(self):
        total_price = self.calculate_total_price()
        return total_price * 0.18

    def final_price(self):
        total_price = self.calculate_total_price()
        if total_price >= 1000:
            return total_price + self.tex()
        else:
            return total_price + self.tex() + 50
            # Adding delivery charge if total < 1000