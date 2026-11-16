"""
Cliente Supabase para o Senior Help.
"""

from functools import lru_cache

from config import SUPABASE_URL, SUPABASE_KEY, USE_SUPABASE


@lru_cache(maxsize=1)
def get_supabase():
    if not USE_SUPABASE:
        raise RuntimeError(
            "Supabase não configurado. Defina SUPABASE_URL e SUPABASE_KEY no .env"
        )
    from supabase import create_client

    return create_client(SUPABASE_URL, SUPABASE_KEY)


def supabase_ok() -> bool:
    return USE_SUPABASE
