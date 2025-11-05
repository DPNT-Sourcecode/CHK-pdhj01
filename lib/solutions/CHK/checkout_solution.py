import pandas as pd

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        items = 0
        lookup = [
                    'A': ('A', 50, '3A for 130'),
                    ('B', 30, '2B for 45'),
                    ('C', 20, None),
                    ('D', 15, None)
                ]
        if isinstance(skus, str):
            for sku in skus:


            sku, price, promo = lookup[0]
            print(sku)
        else:
            raise ValueError('Wrong input datatype.')



c = CheckoutSolution()
skus = 'AB'
c.checkout(skus)


