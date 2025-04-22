from agrotech_service import (
  cadastrar_agrotech,
  listar_agrotechs,
  buscar_por_estado
)
from utils import limpar_tela
from db.database import criar_tabela_se_nao_existir

def menu():
    criar_tabela_se_nao_existir()
    while True:
        limpar_tela()
        print("=== SISTEMA DE AGROTECHS ===")
        print("1. Cadastrar Agrotech")
        print("2. Listar Agrotechs")
        print("3. Buscar Agrotechs por Estado")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_agrotech()
        elif opcao == "2":
            listar_agrotechs()
        elif opcao == "3":
            estado = input("Digite a sigla do estado (UF): ").upper()
            buscar_por_estado(estado)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    menu()
