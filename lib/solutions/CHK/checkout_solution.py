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
            for sku, sku_freq in Counter(skus).items():
                sku_freq = int(sku_freq)
                if inventory[sku]["promo"] is None:
                    total += inventory[sku]["price"]
                    
                else:
                    regular_price = inventory[sku]["price"]
                    promo = inventory[sku]["promo"]
                    promo_qty_sku, _, promo_price = tuple(promo.split(' '))
                    promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
                    promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]
                    print('| promo_qty', promo_qty, '| promo_price', promo_price, '| promo_sku', promo_sku)

                    if sku_freq >= promo_qty:
                        multiplier, remainder = divmod(sku_freq, promo_qty)
                        total = (multiplier * promo_price) + (remainder * regular_price)


            return total







