import dotenv
import os


class EnvUtils:
    _already_loaded = False

    @classmethod
    def get_env(cls, key, default=None):
        if not cls._already_loaded:
            cls._load_env()

        return os.getenv(key, default)

    @classmethod
    def _load_env(cls):
        dotenv.load_dotenv()
        cls._already_loaded = True
