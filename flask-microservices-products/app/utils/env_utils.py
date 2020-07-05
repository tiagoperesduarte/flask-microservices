import os

import dotenv


class EnvUtils:
    _alreadyLoaded = False

    @classmethod
    def get_env(cls, key, default=None):
        if not cls._alreadyLoaded:
            cls._load_env()

        return os.getenv(key, default)

    @classmethod
    def _load_env(cls):
        dotenv.load_dotenv()
        cls._alreadyLoaded = True
