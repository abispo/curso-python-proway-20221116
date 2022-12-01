"""
Classes que são mapeadas para tabelas no banco de dados

User                -> tb_users
UserProfile         -> tb_users_profiles
Post                -> tb_posts
Tag                 -> tb_tags (categorias)
Comment             -> tb_comments
"""

from database import Base

# Classes que representam os tipos de dados que as colunas terão
from sqlalchemy import Column, Integer, String


class User(Base):

    # User  -> user -> users
    # __tablename__ permite definir o nome da tabela mapeada no banco de dados
    __tablename__ = "tb_users"

    # Os atributos abaixo serã os nomes das colunas da tabela tb_users

    # id será a chave primária da tabela, do tipo inteiro e com auto incremento
    id = Column(Integer, primary_key=True, autoincrement=True)

    # email será um campo string de tamanho máximo 100, e que não permite valores nulos
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
