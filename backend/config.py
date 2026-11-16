"""
Configurações do backend do Senior Help.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Banco de dados SQLite
DATABASE_PATH = BASE_DIR / "db" / "senior_help.db"

DIAS_ANTECEDENCIA_PADRAO = 5

CATEGORIAS_DESPESA = [
    "Moradia",
    "Saúde",
    "Alimentação",
    "Contas",
    "Transporte",
    "Lazer",
    "Outros"
]

FREQUENCIAS = [
    "unica",
    "mensal",
    "bimestral",
    "trimestral",
    "anual"
]
