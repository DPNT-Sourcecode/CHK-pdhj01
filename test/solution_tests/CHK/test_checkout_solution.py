from solutions.TST import one
from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_sum(self):
        skus = 'A'
        assert CheckoutSolution.checkout(skus) == 50
