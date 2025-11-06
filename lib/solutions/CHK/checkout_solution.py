from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        total_no_promo, total_promo = 0, 0
        inventory = {
                    'A': {"price": 50, "promo": '3A for 130'},
                    'B': {"price": 30, "promo": '2B for 45'},
                    'C': {"price": 20, "promo": None},
                    'D': {"price": 15, "promo": None}
                }

        if not isinstance(skus, str) or skus.upper() != skus or skus == '' or not skus.isalpha():
            return -1
        
        else:
            c = Counter(skus)
            for sku, sku_freq in c.items():
                sku_freq = int(sku_freq)

                # No promo, check if a given SKU has a promo
                if inventory[sku]["promo"] is None:
                    total_no_promo += inventory[sku]["price"]
                    
                else:
                    # Get regular price and promotion from inventory lookup
                    regular_price = inventory[sku]["price"]
                    promo = inventory[sku]["promo"]

                    # Split promotion into three parts
                    promo_qty_sku, _, promo_price = tuple(promo.split(' '))

                    # Extract promo quantity and sku
                    min_promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
                    promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]

                    # If minimum promotion quantity NOT exceeded
                    if sku_freq < min_promo_qty:
                        total_promo += inventory[promo_sku]["price"]

                    # If minimum promotion quantity exceeded, apply discount
                    else:
                        multiplier, remainder = divmod(sku_freq, min_promo_qty)

                        total_promo += (int(multiplier) * int(promo_price)) + (int(remainder) * int(regular_price))

            print('total_no_promo', total_no_promo)
            return total_no_promo + total_promo




