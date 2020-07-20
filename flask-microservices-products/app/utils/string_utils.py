import random
import string


class StringUtils:
    @classmethod
    def is_empty(cls, str):
        if str and str.strip():
            return False

        return True

    @classmethod
    def is_not_empty(cls, str):
        return not StringUtils.is_empty(str)

    @classmethod
    def get_random_string(cls, length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    @classmethod
    def get_first_word(cls, str):
        if StringUtils.is_empty(str):
            return None

        return str.split()[0]
