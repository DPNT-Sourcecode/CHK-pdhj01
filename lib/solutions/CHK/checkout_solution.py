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
        if skus == '' or not isinstance(skus, str) or not skus.isalpha():
            return -1

        # Check the input SKU is actually available in the inventory lookup
        for sku in skus:
            if sku not in inventory.keys():
                return -1
        
        # Parse and build the inventory lookup to account for promos
        for sku, _ in inventory.items():
            # if promo, 
            promo_list = []
            promo = inventory[sku]["promo"]
            discount_type = 'no_discount'
            if promo:
                promos = [i.strip() for i in promo.split(',')]
                promo_list.extend(promos)

                # If an SKU contains more than one promotion, parse them individually
                for i in range(len(promo_list)):

                    # Bulk discount
                    promo_item = promo_list[i]

                    # If bulk discount
                    if 'for' in promo_item:
                        promo_qty_sku, _, promo_price = tuple(promo_item.split(' '))
                        free_sku = None
                        discount_type = 'bulk'

                    # Else, Buy X get Y free 
                    else:
                        promo_qty_sku, _, _, free_sku, _ = tuple(promo_item.split(' '))
                        promo_price = None
                        discount_type = 'get_free'

                    min_promo_qty = int([i for i in promo_qty_sku if i.isnumeric()][0])
                    promo_sku = [i for i in promo_qty_sku if i.isalpha()][0]

                    promo_list[i] = {
                            'min_promo_qty':min_promo_qty,
                            'promo_sku':promo_sku,
                            'promo_price':promo_price,
                            'free_sku': free_sku, 
                        }
            

            # Insert blank list if no promos
            else:
                promo_list.extend('')
            
            # Compile all the items
            inventory[sku]["promo"] = promo_list
            
            # Mark discount type at SKU Level
            inventory[sku]["discount_type"] = discount_type

        # Use a counter to apply discounts
        total_cost = 0
        skus = Counter(skus)

        # Assume promotions exist
        for sku in skus:
            print(inventory[sku])
            total_skus = skus[sku]
            print('sku: ', sku, '| total_skus: ', total_skus)
            promos = inventory[sku]["promo"]
            discount_type = inventory[sku]["discount_type"]

            # Add up all SKUs without promos
            if discount_type == 'no_discount':
                print('no_discount')
                total_cost += inventory[sku]["regular_price"]
            
            # If buy X get Y free
            elif discount_type == 'get_free':
                print('remainder;', 7%3)
                # print(' get_free')
                # for promo in promos:
                #     free_items, regular_items = skus[sku] % promo["min_promo_qty"]
                #     print('free_items, regular_items: ', free_items, regular_items)

                # free_skus = promo["free_sku"]
                # skus[sku] = 

            # If bulk discount
            # else:
            #     pass

        print('total_cost: ', total_cost)
        return total_cost



