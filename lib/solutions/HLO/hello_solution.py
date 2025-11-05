
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if isinstance(friend_name, str):
            # return f'Hello {friend_name}'
            return "Hello, World!"
        else:
            raise TypeError('Input is not a string')
