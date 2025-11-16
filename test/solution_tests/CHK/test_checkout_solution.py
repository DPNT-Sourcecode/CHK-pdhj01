from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        checkout = CheckoutSolution()
        # Illegal chars and values
        assert checkout.checkout('') == 0
        assert checkout.checkout(1) == -1
        assert checkout.checkout('-') == -1
        assert checkout.checkout('4') == -1

        # # Lookup
        assert checkout.checkout('a') == -1

        # # Regular Price Only
        assert checkout.checkout('C') == 20
        assert checkout.checkout('D') == 15
        assert checkout.checkout('CD') == 15 + 20

        # promos and regulars
        assert checkout.checkout('A') == 50
        # assert checkout.checkout('AA') == 100
        # assert checkout.checkout('AAC') == 120
        # assert checkout.checkout('AAAAAACC') == (1 * 200) + (1 * 50) + (2 * 20) #290
        # assert checkout.checkout(9*'A') == 380
        
        # # # Buy one get one free
        # assert checkout.checkout('EA') == 90
        # assert checkout.checkout('EE') == 80
        # assert checkout.checkout('EEB') == 80
        # assert checkout.checkout('EEAB') == 2*40 + 50 + 0
        # assert checkout.checkout('EEAAAB') == 2*40 + 130 + 0

        # assert checkout.checkout('EEEEBB') == 4 * 40 #160
        # assert checkout.checkout('BEBEEE') == 160
        # assert checkout.checkout('ABCDEABCDE') == 280



