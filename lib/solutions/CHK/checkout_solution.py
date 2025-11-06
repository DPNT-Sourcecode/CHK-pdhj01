class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        total = 0
        items = {
                    'A': {"price": 50, "promo": '3A for 130'},
                    'B': {"price": 30, "promo": '2B for 45'},
                    'C': {"price": 20, "promo": None},
                    'D': {"price": 15, "promo": None}
                }
        if skus is not isinstance(skus, str) or skus.upper() != skus or skus == '':
            print('exception')
            return -1
        
        else:
            for sku in skus:
                print('cond')
                total += items[sku]["price"]
                print(total)
                return total



c = CheckoutSolution()
c.checkout('A')

# if items[sku]["promo"] is None:
#     total += items[sku]["price"]
# else:
#     promo = items[sku]["promo"]
#     quantity_price, _, promo_price = tuple(promo.split(' '))
#     promo_price = int(promo_price)
#     quantity = [i for i in quantity_price if i.isnumeric()][0]
#     sku = [i for i in quantity_price if i.isalpha()][0]
#     print('promo_price: ', promo_price)
#     total += promo_price


