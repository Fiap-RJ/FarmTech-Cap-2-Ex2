from utils import validar_uf, obter_dados_json, salvar_dados_json
from db.database import inserir_no_banco

ARQUIVO_JSON = "data/agrotechs.json"


def cadastrar_agrotech():
    print("Cadastro de Agrotech")
    nome = input("Nome da agrotech: ").strip()
    estado = input("Estado (sigla): ").strip().upper()
    segmento = input("Segmento (ex: gestão, sensores, biotecnologia): ").strip()

    if not validar_uf(estado):
        print("UF inválida.")
        return

    agrotech = {"nome": nome, "estado": estado, "segmento": segmento}

    dados = obter_dados_json(ARQUIVO_JSON)
    dados.append(agrotech)
    salvar_dados_json(ARQUIVO_JSON, dados)

    # inserir_no_banco(agrotech)

    print("Agrotech cadastrada com sucesso!")
    input("Pressione Enter para continuar...")


def listar_agrotechs():
    print("Lista de Agrotechs")
    dados = obter_dados_json(ARQUIVO_JSON)
    if not dados:
        print("Nenhuma agrotech cadastrada.")
    for a in dados:
        print(f"- {a['nome']} ({a['estado']}): {a['segmento']}")
    input("Pressione Enter para continuar...")


def buscar_por_estado(uf):
    dados = obter_dados_json(ARQUIVO_JSON)
    filtrados = [a for a in dados if a["estado"] == uf]
    if not filtrados:
        print("Nenhuma agrotech encontrada nesse estado.")
    for a in filtrados:
        print(f"- {a['nome']} ({a['estado']}): {a['segmento']}")
    input("Pressione Enter para continuar...")
