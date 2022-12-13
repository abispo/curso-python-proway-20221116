# Python com Banco de dados

Nesse módulo, vamos precisar instalar essas 3 bibliotecas
* Django (WEB Framework)
* python-dotenv (Lib para ler arquivos .env)
* mysqlclient (Lib utilizada pelo Django para acessar bancos MySQL/MariaBD)

Como utilizaremos a biblioteca python-dotenv, sempre em um novo projeto, vamos precisar criar o arquivo `.env` com o seguinte conteúdo:

DB_NAME=financas_pessoais
DB_USER=root
DB_PASS=admin
DB_HOST=localhost
DB_PORT=3306

**DETALHE**: Os dados acima podem mudar de acordo com as credenciais de acesso que foram criadas para acessar o servidor de banco de dados local.