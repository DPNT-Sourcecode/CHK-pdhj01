from solutions.TST import one
from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_sum(self):
        checkout = CheckoutSolution()
        assert checkout.checkout('A') == 50

