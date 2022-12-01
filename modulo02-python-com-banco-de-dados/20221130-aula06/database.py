
import os

# O pacote python-dotenv é utilizado para ler valores de variáveis de ambiente do sistema
from dotenv import load_dotenv

# create_engine é a função utilizada para criar uma conexão com o banco de dados
from sqlalchemy import create_engine

# declarative_base serve para utilizarmos uma classe base como modelo para as nossas classes mapeadas
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker cria a sessão de acesso ao banco de dados
from sqlalchemy.orm import sessionmaker

# load_dotenv carrega as informações do arquivo .env e cria variáveis de ambiente com os seus valores
load_dotenv()

# Armazenando os valores das variáveis de ambiente
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# String de conexão ao banco de dados
# Fazemos isso para evitar que as credenciais de acesso a serviços externos fiquem expostas no código
connection_string = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# Podemos facilmente trocar de banco de dados apenas alterando a connection string
# connection_string = "sqlite:///aula_06.sqlite3"

# create_engine retorna um objeto engine, que é responsável por estabelecer a conexão com o banco de dados
# O parâmetro echo=True imprime no terminal os comandos SQL executados
engine = create_engine(connection_string, echo=True)

# declarative_base retorna a classe base a qual todas as classes do nosso projeto, que forem models, irão herdar.
# Precisamos fazer isso para ser possível mapear as classes para as tabelas no banco de dados.
Base = declarative_base()

# Criamos a sessão. Utilizando esse objeto session que o SQLAlchemy executa as instruções SQL no banco de dados
Session = sessionmaker(bind=engine)
session = Session()
