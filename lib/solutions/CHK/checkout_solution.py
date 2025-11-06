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
                print('sku_freq', sku_freq)
                if inventory[sku]["promo"] is None:
                    total += inventory[sku]["price"]
                    
                else:
                    # Get regular price and promotion from inventory lookup
                    regular_price = inventory[sku]["price"]
                    promo = inventory[sku]["promo"]

                    # Split promotion into three parts
                    promo_qty_sku, _, promo_price = tuple(promo.split(' '))

                    # Extract promo quantity and sku
                    min_promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
                    promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]

                    # print('| min_promo_qty', min_promo_qty, '| promo_price', promo_price, '| promo_sku', promo_sku, '| promo_sku', promo_sku)
                    print('sku_freq', sku_freq, 'min_promo_qty', min_promo_qty)
                    # If minimum promotion quantity exceeded, apply discount
                    if sku_freq >= min_promo_qty:
                        print('promo condition met')
                        multiplier, remainder = divmod(sku_freq, min_promo_qty)
                        total = (multiplier * promo_price) + (remainder * regular_price)

                print('total', total)
            return total








