import random
import sys


class NumberUtils:
    @classmethod
    def get_random_number(cls, min=0, max=sys.maxsize, precision=2):
        return round(random.uniform(min, max), precision)
