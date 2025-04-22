import oracledb
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def conectar():
    try:
        username = os.getenv("DATABASE_USER")
        password = os.getenv("DATABASE_PASSWORD")
        host = os.getenv("DATABASE_HOST")
        port = os.getenv("DATABASE_PORT")
        service_name = os.getenv("DATABASE_NAME")

        if not all([username, password, host]):
            raise ValueError("Variáveis de ambiente para conexão Oracle não definidas.")

        connection = oracledb.connect(user=username, password=password, host=host, port=port, service_name=service_name)
        return connection
    except oracledb.Error as e:
        print("Erro ao conectar ao banco:", e)
        return None
