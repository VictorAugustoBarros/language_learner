from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class Portuguese:
    def __init__(self):
        pass

    def get_data_to_insert(self, word: str):
        return {"portuguese_word": word}
