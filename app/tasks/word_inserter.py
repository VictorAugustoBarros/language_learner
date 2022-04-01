"""Word Inserter."""
from app.languages.portuguese import Portuguese
from app.languages.japanese import Japanese
from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class WordInserter:
    """Classe para Inserçãod de novas palavras."""

    def __init__(self, language: str, word: str, complementar_word: str = None):
        """Contrutor da classe.

        Args:
            language (str): Linguagem especificada
            word (str): Palavra a ser cadastrada
            complementar_word (str): Palavra complementar a ser cadastrada
        """
        self.db = Prisma()
        self.word = word
        self.complementar_word = complementar_word
        self.language = language

    def create_insert(self):
        """Busca das informações necessárias para inserção da palavra."""
        if self.language == "pt":
            return self.db.portuguesewords, Portuguese().get_data_to_insert(word=self.word)

        elif self.language == "jp":
            return self.db.japanesewords, Japanese().get_data_to_insert(
                word=self.word, complementar_word=self.complementar_word
            )

        return None

    async def insert_word(self):
        """Cadastro de uma nova palavra no banco de dados."""
        await self.db.connect()
        language, data = self.create_insert()

        try:
            await language.create(data=data)
            Logger().success({"message": "Insert word success.", "word": self.word})

        except UniqueViolationError:
            Logger().warning({"message": "Word already exists.", "word": self.word})

        await self.db.disconnect()
