"""
Senior Help - Backend
Ponto de entrada e exemplo de uso das funções principais.
"""

from api import FuncoesAPI
from datetime import datetime


def exemplo_uso():
    api = FuncoesAPI()

    print("=== Senior Help - Backend ===\n")

    print("1. Criando usuário...")
    resultado = api.criar_usuario({
        "nome": "Maria Silva",
        "data_nascimento": "1955-03-12",
        "contato_confianca_nome": "João (filho)",
        "contato_confianca_telefone": "11999998888",
    })
    print(resultado)
    usuario_id = resultado["usuario"]["id"]
    print()

    print("2. Adicionando receita...")
    resultado = api.adicionar_receita({
        "usuario_id": usuario_id,
        "descricao": "Aposentadoria INSS",
        "valor": 2800.00,
        "frequencia": "mensal",
        "data_recebimento": datetime.now().strftime("%Y-%m-%d"),
    })
    print(resultado)
    print()

    print("3. Adicionando despesa...")
    resultado = api.adicionar_despesa({
        "usuario_id": usuario_id,
        "descricao": "Conta de luz",
        "valor": 185.50,
        "categoria": "Contas",
        "data_vencimento": datetime.now().strftime("%Y-%m-%d"),
        "paga": False,
    })
    print(resultado)
    print()

    print("4. Criando lembrete...")
    resultado = api.criar_lembrete({
        "usuario_id": usuario_id,
        "titulo": "Conta de água",
        "valor": 90.00,
        "data_vencimento": "2026-11-25",
        "frequencia": "mensal",
    })
    print(resultado)
    print()

    print("5. Resumo do mês...")
    resultado = api.obter_resumo_mes(usuario_id)
    print(resultado)
    print()

    print("6. Avisos de lembretes...")
    resultado = api.obter_avisos_lembretes(usuario_id)
    print(resultado)
    print()

    print("=== Fim do exemplo ===")


if __name__ == "__main__":
    exemplo_uso()
