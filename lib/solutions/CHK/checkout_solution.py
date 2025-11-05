import re

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        total = 0
        items = {
                    'A': {"price": 50, "promo": '3A for 130'},
                    'B': {"price": 30, "promo": '2B for 45'},
                    'C': {"price": 20, "promo": None},
                    'D': {"price": 15, "promo": None}
                }
        if isinstance(skus, str):
            for sku in skus:
                if sku in items.keys():
                    if items[sku]["promo"] is None:
                        total += items[sku]["price"]
                    else:
                        promo = items[sku]["promo"]
                        pattern = r'()'
                        match = re.search('', promo)
                        # regexp = quantitySKU for total
                        total += items[sku]["price"]

            return total
        else:
            return -1
            # raise ValueError('Wrong input datatype.')



c = CheckoutSolution()
skus = 'AB'
output = c.checkout(skus)
print(output)