"""Portuguese."""
from prisma import Prisma
from prisma.errors import UniqueViolationError
from app.utils.logger import Logger


class Portuguese:
    """Classe para controle dos registros da tabela PortugueseWords."""

    def get_data_to_insert(self, word: str):
        """Busca do modelo necessário para cadastro de uma nova palavra.

        Args:
            word (str): Palavra para inserção
        """
        return {"portuguese_word": word}
