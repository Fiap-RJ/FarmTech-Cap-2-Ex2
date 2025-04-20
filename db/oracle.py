import cx_Oracle
import os
from dotenv import load_dotenv, find_dotenv()

# Carrega variáveis do .env
load_dotenv(find_dotenv())


def conectar():
    try:
        username = os.getenv("ORACLE_USERNAME")
        password = os.getenv("ORACLE_PASSWORD")
        dsn = os.getenv("ORACLE_DSN")

        if not all([username, password, dsn]):
            raise ValueError("Variáveis de ambiente para conexão Oracle não definidas.")

        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        return connection
    except cx_Oracle.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None
