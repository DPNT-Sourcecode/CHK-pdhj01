from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        total = 0
        inventory = {
                    'A': {"price": 50, "promo": '3A for 130'},
                    'B': {"price": 30, "promo": '2B for 45'},
                    'C': {"price": 20, "promo": None},
                    'D': {"price": 15, "promo": None}
                }

        if not isinstance(skus, str) or skus.upper() != skus or skus == '' or not skus.isalpha():
            return -1
        
        else:
            for sku, freq in Counter(skus).items():
                if inventory[sku]["promo"] is None:
                    total += inventory[sku]["price"]
            print('total: ', total)
            return total
                    # else:
                    #     promo = items[sku]["promo"]

                    #     quantity_price, _, promo_price = tuple(promo.split(' '))
                    #     promo_price = int(promo_price)
                    #     quantity = [i for i in quantity_price if i.isnumeric()][0]
                    #     sku = [i for i in quantity_price if i.isalpha()][0]
                    #     # total += promo_price

                    #     # if sku_len >= quantity:
                    #     #     sku_len

                    #     print('quantity: ', quantity, 'sku: ', sku, 'promo_price', promo_price)


            #     total += items[sku]["price"]


