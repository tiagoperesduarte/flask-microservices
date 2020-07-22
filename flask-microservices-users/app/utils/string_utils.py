import random
import string
import unicodedata


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

    @classmethod
    def remove_accents(cls, str):
        nfkd_form = unicodedata.normalize('NFKD', str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

    @classmethod
    def sanitize_string(cls, str):
        if StringUtils.is_empty(str):
            return None

        str = StringUtils.remove_accents(str)
        str = str.replace(' ', '-')
        str = str.lower()

        return str
