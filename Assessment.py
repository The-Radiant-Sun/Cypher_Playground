# Interactive cryptography playground


class Cypher:
    @staticmethod
    def get_input(string):
        user_input = input('Please enter {}: '.format(string))
        while user_input == '':
            user_input = Cypher.get_input(string)
        return user_input
