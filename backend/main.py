"""
Senior Help - Backend
Teste rápido da conexão com Supabase.
"""

from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

from api import FuncoesAPI
from persistence import supabase_ok
from datetime import datetime


def exemplo_uso():
    print("=== Senior Help - Backend ===\n")

    if not supabase_ok():
        print("Supabase NÃO configurado.")
        print("1. Copie backend/.env.example para backend/.env")
        print("2. Preencha SUPABASE_URL e SUPABASE_KEY")
        print("3. Rode o SQL em backend/supabase_schema.sql no SQL Editor do Supabase")
        return

    print("Supabase configurado. Testando...\n")
    api = FuncoesAPI()

    print("1. Criando usuário...")
    resultado = api.criar_usuario({
        "nome": "Maria Silva",
        "data_nascimento": "1955-03-12",
        "contato_confianca_nome": "João (filho)",
        "contato_confianca_telefone": "11999998888",
    })
    print(resultado)
    if not resultado.get("ok"):
        return
    usuario_id = resultado["usuario"]["id"]
    print()

    print("2. Adicionando receita...")
    print(api.adicionar_receita({
        "usuario_id": usuario_id,
        "descricao": "Aposentadoria INSS",
        "valor": 2800.00,
        "frequencia": "mensal",
        "data_recebimento": datetime.now().strftime("%Y-%m-%d"),
    }))
    print()

    print("3. Adicionando despesa...")
    print(api.adicionar_despesa({
        "usuario_id": usuario_id,
        "descricao": "Conta de luz",
        "valor": 185.50,
        "categoria": "Contas",
        "data_vencimento": datetime.now().strftime("%Y-%m-%d"),
        "paga": False,
    }))
    print()

    print("4. Criando lembrete...")
    print(api.criar_lembrete({
        "usuario_id": usuario_id,
        "titulo": "Conta de água",
        "valor": 90.00,
        "data_vencimento": "2026-11-25",
        "frequencia": "mensal",
    }))
    print()

    print("5. Resumo do mês...")
    print(api.obter_resumo_mes(usuario_id))
    print()

    print("6. Avisos de lembretes...")
    print(api.obter_avisos_lembretes(usuario_id))
    print()

    print("=== OK ===")


if __name__ == "__main__":
    exemplo_uso()
