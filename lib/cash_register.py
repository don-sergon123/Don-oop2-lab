#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        total_price = price * quantity
        self.total += total_price

        self.items.extend([item] * quantity)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        if not self.previous_transactions or self.total == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        self.previous_transactions.pop()

        formatted_total = int(
            self.total) if self.total.is_integer() else self.total
        print(f"After the discount, the total comes to ${formatted_total}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        last_transaction = self.previous_transactions.pop()
        item_total = last_transaction["price"] * last_transaction["quantity"]
        self.total -= item_total

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
