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
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Table

# Tabela associativa entre as models Post e Tag (N:N)
posts_tags = Table(
    "tb_posts_tags", Base.metadata,
    Column("post_id", Integer, ForeignKey("tb_posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tb_tags.id"), primary_key=True)
)


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


class UserProfile(Base):

    __tablename__ = "tb_users_profiles"

    # Definimos a coluna id da tabela como chave primária e chave estrangeira
    id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(150))


class Post(Base):

    __tablename__ = "tb_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("tb_users.id"), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)


class Tag(Base):

    __tablename__ = "tb_tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)


class Comment(Base):

    __tablename__ = "tb_comments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("tb_posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("tb_users.id"), nullable=False)
    content = Column(String(200), nullable=False)
