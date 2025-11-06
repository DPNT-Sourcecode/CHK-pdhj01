from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        checkout = CheckoutSolution()
        assert checkout.checkout('a') == -1
        assert checkout.checkout('') == -1
        assert checkout.checkout(20) == -1
        assert checkout.checkout('A') == 50
        assert checkout.checkout('B') == 30
        assert checkout.checkout('C') == 20
        assert checkout.checkout('D') == 15
        assert checkout.checkout('AB') == 80
        assert checkout.checkout('CCC') == 60



        assert checkout.checkout('-') == -1
        assert checkout.checkout('C') == 20
        assert checkout.checkout('AAAA') == 180
        assert checkout.checkout('AAABA') == 210
        assert checkout.checkout('AAABB') == 130 + 45
        assert checkout.checkout('AAABBB') == 205
        assert checkout.checkout('AAABBC') == 130 + 45 + 20
        assert checkout.checkout('AAABBCC') == 130 + 45 + 2*20 #215

        # assert checkout.checkout('AABBCCDD') == 215
        # assert checkout.checkout('ABCDABCD') == 215
        



