"""Japanese."""
from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class Japanese:
    """Classe para controle dos registros da tabela JapaneseWords."""

    def get_data_to_insert(self, word: str, complementar_word: str):
        """Busca do modelo necessário para cadastro de uma nova palavra.

        Args:
            word (str): Palavra para inserção
            complementar_word (str): Palavra complementar para inserção
        """
        return {"japanese_word_romaji": word, "japanese_word_kanji": complementar_word}
