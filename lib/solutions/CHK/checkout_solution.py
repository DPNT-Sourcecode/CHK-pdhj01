from collections import Counter
from pprint import pprint

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        input = skus
        total_no_promo, total_promo = 0, 0
        inventory = {
                    'A': {"regular_price": 50, "promo": '3A for 130, 5A for 200'},
                    'B': {"regular_price": 30, "promo": '2B for 45'},
                    'C': {"regular_price": 20, "promo": None},
                    'D': {"regular_price": 15, "promo": None},
                    'E': {"regular_price": 40, "promo": '2E get one B free'}
                }
        # Parse and build the inventory lookup

        for sku, _ in inventory.items():
            promo_list = []
            promo = inventory[sku]["promo"] 
            print('sku:', sku, 'promo', promo)
            
            if promo and ',' in promo:
                print("promo exists")
                promos = [i.strip() for i in promo.split(',')]
                promo_list.extend(promos)
                inventory[sku]["promo"] = promo_list
            else:
                # promo_list.append()
                pass

        

        pprint(inventory)

            # else:
            #     if promos:
            #         for promo in promos:
            #             # Split promotion into three parts
            #             promo_qty_sku, _, promo_price = tuple(promo.split(' '))

            #             # Extract promo quantity and sku
            #             min_promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
            #             promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]

            #             inventory[sku]['min_promo_qty'] = min_promo_qty
            #             inventory[sku]['promo_sku'] = promo_sku
            #             inventory[sku]['promo_price'] = promo_price

            #             promo_list.append({
            #                     'min_promo_qty':min_promo_qty,
            #                     'promo_sku':promo_sku,
            #                     'promo_price':promo_price
            #                 })  
            #         inventory[sku]['promo'] = promo_list
            #     else:
            #         promo_qty_sku, _, promo_price = tuple(promo.split(' '))

            #         # Extract promo quantity and sku
            #         min_promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
            #         promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]

            #         inventory[sku]['min_promo_qty'] = min_promo_qty
            #         inventory[sku]['promo_sku'] = promo_sku
            #         inventory[sku]['promo_price'] = promo_price

            #         promo_list.append({
            #                 'min_promo_qty':min_promo_qty,
            #                 'promo_sku':promo_sku,
            #                 'promo_price':promo_price
            #             })  
            #         inventory[sku]['promo'] = promo_list


        # # Handle non-alpha values and illegal characters
        # if skus == '':
        #     return 0
        # elif not isinstance(skus, str) or skus.upper() != skus or skus == '' or not skus.isalpha():
        #     return -1
        
        # else:
        #     # Build a counter with all the SKUs bought and their quantities
        #     c = Counter(skus)

        #     # Iterate through one item and its quantity at a time
        #     for sku, sku_freq in c.items():
        #         sku_freq = int(sku_freq)

        #         # Begin with non-promos
        #         if inventory[sku]["promo"] is None:
        #             total_no_promo += inventory[sku]["regular_price"] * sku_freq
                    
        #         else:
        #             # If minimum promotion quantity NOT exceeded
        #             min_promo_qty = inventory[sku]['min_promo_qty']
        #             regular_price = inventory[sku]["regular_price"]
        #             promo_price = inventory[sku]["promo_price"]


        #             if sku_freq < min_promo_qty:
        #                 total_promo += regular_price * sku_freq

        #             # If minimum promotion quantity exceeded, apply discount
        #             else:
        #                 multiplier, remainder = divmod(sku_freq, min_promo_qty)
        #                 total_promo += (int(multiplier) * int(promo_price)) + (int(remainder) * int(regular_price))
            
        #     print('input:', input, 'total_no_promo', total_no_promo, 'total_promo', total_promo)

        #     return total_no_promo + total_promo









