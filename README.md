
# Language Generator

Projeto para aprendizado de uma nova lingua.

O objetivo do projeto é a conversão das palavras cadastradas em sua lingua materna para a lingua que deseja aprender, utilizando flashcards para a memorização das palavras.

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/VictorAugustoBarros/language_learner.git
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o container MYSQL para armazenamento dos dados.

```bash
  docker-compose -f docker/mysql.yml up --build -d
```

Para cadastro de novas palavras via CLI.

```bash
  pip install .

  learner --help
```
## Roadmap

- Construção API para cadastro das palavras.

- Construção deploy automatizado com CI/CD 

- Testes reconhecimento de voz para identificação de novas palavras.

- Conversão das palvras para outra lingua.

- Construção do Front-End.


## Roadmap

**Front-End**: 

**Back-End**: Python, Prisma
## Autores

- [@VictorAugustoBarros](https://github.com/VictorAugustoBarros)

