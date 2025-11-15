from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkout(self):
        checkout = CheckoutSolution()
        # Illegal chars and values
        assert checkout.checkout('') == -1
        assert checkout.checkout(1) == -1
        assert checkout.checkout('-') == -1
        assert checkout.checkout('4') == -1


        # Lookup
        assert checkout.checkout('a') == -1

        # Regular Price Only
        assert checkout.checkout('C') == 20
        assert checkout.checkout('D') == 15
        assert checkout.checkout('CD') == 15 + 20


        # promos and regulars
        assert checkout.checkout('E') == 40
        # assert checkout.checkout('AA') == 50
        # assert checkout.checkout('D') == 15
        # assert checkout.checkout('AB') == 80
        # assert checkout.checkout('CCC') == 60
        # assert checkout.checkout('AAAA') == 180

        # # Edge
        # assert checkout.checkout('AAABA') == 210
        # assert checkout.checkout('AAABB') == 130 + 45
        # assert checkout.checkout('AAABBB') == 205
        # assert checkout.checkout('AAABBC') == 130 + 45 + 20
        # assert checkout.checkout('AAABBCC') == 130 + 45 + 2*20 #215

        # # assert checkout.checkout('AABB') == 215
        # assert checkout.checkout('ABCDABCD') == 215
        


