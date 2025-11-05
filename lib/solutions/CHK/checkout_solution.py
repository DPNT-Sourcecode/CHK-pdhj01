import pandas as pd

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        items = 0
        if isinstance(skus, str):
            for sku in skus:
                print(sku)  
        #     t = [
        #         ('A', 50, '3A for 130'),
        #         ('B', 30, '2B for 45'),
        #         ('C', 20, None),
        #         ('D', 15, None)
        #         ]
            
        #     #  - @return = an integer representing the total checkout value of the items
        #     return sum(items)
        else:
            raise ValueError('Wrong input datatype.')



c = CheckoutSolution()
skus = 'AB'
c.checkout(skus)

