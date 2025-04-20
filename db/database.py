from db.oracle import conectar


def inserir_no_banco(agrotech: dict):
    """
    Insere uma nova agrotech no banco de dados.
    
    Args:
        agrotech (dict): Dicionário com os dados da agrotech a serem inseridos.
            Deve conter as chaves "nome", "estado" e "segmento".
    """
    connection = conectar()
    if connection is None:
        print("Erro ao conectar ao banco. Dados não foram inseridos.")
        return

    cursor = connection.cursor()

    try:
        sql = """
        INSERT INTO AGROTECHS (NOME, ESTADO, SEGMENTO)
        VALUES (:1, :2, :3)
        """
        cursor.execute(
            sql, (agrotech["nome"], agrotech["estado"], agrotech["segmento"])
        )
        connection.commit()
        print("Agrotech inserido com sucesso.")

    except Exception as e:
        print(f"Erro ao inserir no banco: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()
