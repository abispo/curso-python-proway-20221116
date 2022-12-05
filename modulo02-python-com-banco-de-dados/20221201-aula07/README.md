# ORM

Instalar as seguintes bibliotecas:
* alembic
* pymysql
* python-dotenv
* sqlalchemy

Elas podem ser instaladas pela aba `Packages` do PyCharm ou pelo comando `pip install <biblioteca>`

## alembic

Alembic é a ferramenta utilizada para gerenciar as "versões" das nossas models.

Para gerar uma nova revision:
`python revision --autogenerate -m "mensagem"`

Para aplicar a última revision
`python upgrade head`