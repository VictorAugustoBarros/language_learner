from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class Japanese:
    def __init__(self):
        pass

    def get_data_to_insert(self, word: str, complementar_word: str):
        return {"japanese_word_romaji": word, "japanese_word_kanji": complementar_word}
