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
        
        # Parse and build the inventory lookup to account for promos
        for sku, _ in inventory.items():
            # if promo, 
            promo_list = []
            promo_dict = {}
            promo = inventory[sku]["promo"]
            discount_type = 'no_discount'
            min_promo_qtys = []
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

                    min_promo_qtys.append(min_promo_qty)
   
                    promo_dict[min_promo_qty] = {
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
            inventory[sku]["sorted_min_quantities"] = sorted(min_promo_qtys, reverse=True)
            inventory[sku]["promo"] = promo_dict

        skus = Counter(skus)
        print('skus', skus)

        total_price = 0
        price_to_deduct = 0
        for sku in skus:
            discount_type = inventory[sku]['discount_type']
            remaining_items = skus[sku]
            promos = inventory[sku]["promo"]
            print(f'-------- processing sku: {sku}')
            pprint(inventory[sku])
                        
            # Apply bulk discounts to total
            if discount_type == 'bulk':
                for min_qty in inventory[sku]["sorted_min_quantities"]:
                    quotient, remainder = divmod(remaining_items, min_qty)
                    remaining_items -= quotient * min_qty
                    total_price += int(promos[min_qty]['promo_price']) * quotient

                total_price += int(inventory[sku]["regular_price"]) * int(remainder)
                print('bulk_total_price', total_price)

            # If buy X get Y free
            elif discount_type == 'get_free':
                # If free, add the price, then deduct at the end
                total_price += inventory[sku]["regular_price"] * skus[sku]
                for min_qty in inventory[sku]["sorted_min_quantities"]:
                    quotient, remainder = divmod(remaining_items, min_qty)
                    remaining_items -= quotient * min_qty
                    free_sku = promos[min_qty]['free_sku']
                    print('quotient, remainder', quotient, remainder)
                    if free_sku in skus:
                        price_to_deduct = quotient * inventory[free_sku]["regular_price"]
                    print('price_to_deduct', price_to_deduct)

           # Add up all SKUs without promos
            else:                    
                print('skus[sku]', inventory[sku]["regular_price"])
                total_price += inventory[sku]["regular_price"] * skus[sku]
                print('other_total_price', total_price)

            print('total_cost before deductions ', total_price)

        total_price -= price_to_deduct

        print('total_price: ', total_price)
        return int(total_price)


