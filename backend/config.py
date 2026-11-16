"""
Configurações do backend do Senior Help.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# --- Supabase ---
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

DATABASE_PATH = BASE_DIR / "db" / "senior_help.db"
USE_SUPABASE = bool(SUPABASE_URL and SUPABASE_KEY)

DIAS_ANTECEDENCIA_PADRAO = 5

CATEGORIAS_DESPESA = [
    "Moradia",
    "Saúde",
    "Alimentação",
    "Contas",
    "Transporte",
    "Lazer",
    "Outros",
]

FREQUENCIAS = [
    "unica",
    "mensal",
    "bimestral",
    "trimestral",
    "anual",
]
