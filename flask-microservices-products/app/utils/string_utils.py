import random
import string


class StringUtils:
    @classmethod
    def get_random_string(cls, length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
