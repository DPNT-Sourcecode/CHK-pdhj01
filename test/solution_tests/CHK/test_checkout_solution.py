from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        checkout = CheckoutSolution()
        # Illegal chars and values
        assert checkout.checkout('') == -1
        assert checkout.checkout(1) == -1
        assert checkout.checkout('-') == -1
        assert checkout.checkout('4') == -1

        # # Lookup
        assert checkout.checkout('a') == -1

        # # Regular Price Only
        assert checkout.checkout('C') == 20
        assert checkout.checkout('D') == 15
        assert checkout.checkout('CD') == 15 + 20

        # # promos and regulars
        assert checkout.checkout('A') == 50
        assert checkout.checkout('AA') == 100
        assert checkout.checkout('AAC') == 120
        assert checkout.checkout('AAAAAACC') == 250 + 40
        assert checkout.checkout(9*'A') == 380
        
        # Buy one get one free
        assert checkout.checkout('EA') == 40

        

