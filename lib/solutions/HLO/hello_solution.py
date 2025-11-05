
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if isinstance(friend_name, str):
            return f'Hello {friend_name}'
        else:
            raise ValueError('Input is not a string')
