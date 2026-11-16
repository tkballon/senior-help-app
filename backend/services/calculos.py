"""
Cálculos de totais e resumo mensal.
"""

from typing import Any, Dict, List, Optional

from models import Receita, Despesa


def total_receitas(receitas: List[Receita]) -> float:
    return round(sum(r.valor for r in receitas), 2)


def total_despesas(despesas: List[Despesa]) -> float:
    return round(sum(d.valor for d in despesas), 2)


def total_despesas_pagas(despesas: List[Despesa]) -> float:
    return round(sum(d.valor for d in despesas if d.paga), 2)


def total_despesas_pendentes(despesas: List[Despesa]) -> float:
    return round(sum(d.valor for d in despesas if not d.paga), 2)


def saldo(receitas: List[Receita], despesas: List[Despesa]) -> float:
    return round(total_receitas(receitas) - total_despesas(despesas), 2)


def resumo_mes(
    receitas: List[Receita],
    despesas: List[Despesa],
    mes: Optional[str] = None,
) -> Dict[str, Any]:
    return {
        "mes": mes,
        "total_receitas": total_receitas(receitas),
        "total_despesas": total_despesas(despesas),
        "despesas_pagas": total_despesas_pagas(despesas),
        "despesas_pendentes": total_despesas_pendentes(despesas),
        "saldo": saldo(receitas, despesas),
        "qtd_receitas": len(receitas),
        "qtd_despesas": len(despesas),
    }
