from collections import Counter
from pprint import pprint

class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        print(f'-------------------- New record: skus {skus} --------------------')
        # Create inventory
        inventory = {
                    'A': {"regular_price": 50, "promo": '3A for 130, 5A for 200'},
                    'B': {"regular_price": 30, "promo": '2B for 45'},
                    'C': {"regular_price": 20, "promo": None},
                    'D': {"regular_price": 15, "promo": None},
                    'E': {"regular_price": 40, "promo": '2E get one B free'}
                }
        
        # Handle ValueErrors and bad chars.
        if skus == '' or skus == "":
            return 0
        
        if not isinstance(skus, str) or not skus.isalpha():
            return -1

        # Check the input SKU is actually available in the inventory lookup
        for sku in skus:
            if sku not in inventory.keys():
                return -1

        skus = Counter(skus)
        print('skus', skus)
        
