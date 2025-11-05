
class SumSolution:
    
    def compute(self, x, y):
        if x or y and 0 <= x <= 100 and 0 <= y <= 100:
            return x + y
        else:
            raise ValueError(f'Invalid inputs, try again. X: {x}, Y: {y}')

