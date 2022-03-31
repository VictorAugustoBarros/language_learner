from app.languages.portuguese import Portuguese
from app.languages.japanese import Japanese
from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class WordInserter:
    def __init__(self, language: str, word: str, complementar_word: str = None):
        self.db = Prisma()
        self.word = word
        self.complementar_word = complementar_word
        self.language = language

    def create_insert(self):
        if self.language == "pt":
            return self.db.portuguesewords, Portuguese().get_data_to_insert(word=self.word)

        elif self.language == "jp":
            return self.db.japanesewords, Japanese().get_data_to_insert(
                word=self.word, complementar_word=self.complementar_word
            )

        return None

    async def insert_word(self):
        await self.db.connect()
        language, data = self.create_insert()

        try:
            await language.create(data=data)
            Logger().success({"message": "Insert word success.", "word": self.word})

        except UniqueViolationError:
            Logger().warning({"message": "Word already exists.", "word": self.word})

        await self.db.disconnect()
