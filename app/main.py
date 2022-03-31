import click
import asyncio

from app.tasks.word_inserter import WordInserter


@click.group()
@click.option("--debug", envvar="DEBUG", help="Define debug variable.")
@click.pass_context
def cli(ctx, debug):
    """CLI para inserção de novas palavras."""
    ctx.debug = debug


@cli.command("insert_japanese_word")
@click.option("--word", prompt=True, help="Japanese word to insert.", type=str)
def insert_portuguese_word(word: str):
    asyncio.run(WordInserter(language="pt", word=word).insert_word())


@cli.command("insert_portuguese_word")
@click.option("--romaji", prompt=True, help="Portuguese word to insert.", type=str)
@click.option("--kanji", prompt=True, help="Portuguese word to insert.", type=str)
def insert_japanese_word(romaji: str, kanji: str):
    asyncio.run(WordInserter(language="jp", word=romaji, complementar_word=kanji).insert_word())
