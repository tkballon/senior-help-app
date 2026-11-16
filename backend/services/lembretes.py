"""
Avisos de lembretes — mensagens calmas e objetivas.
"""

from datetime import date
from typing import Any, Dict, List

from models import Lembrete


def _parse_data(s: str):
    try:
        return date.fromisoformat(s[:10])
    except Exception:
        return None


def obter_avisos(lembretes: List[Lembrete]) -> List[Dict[str, Any]]:
    hoje = date.today()
    avisos = []
    for l in lembretes:
        dv = _parse_data(l.data_vencimento)
        if not dv:
            continue
        dias = (dv - hoje).days
        if dias < 0:
            avisos.append({
                "lembrete_id": l.id,
                "titulo": l.titulo,
                "valor": l.valor,
                "data_vencimento": l.data_vencimento,
                "tipo": "atrasado",
                "mensagem": f"{l.titulo} venceu há {abs(dias)} dia(s). Valor: R$ {l.valor:.2f}.",
            })
        elif dias == 0:
            avisos.append({
                "lembrete_id": l.id,
                "titulo": l.titulo,
                "valor": l.valor,
                "data_vencimento": l.data_vencimento,
                "tipo": "hoje",
                "mensagem": f"{l.titulo} vence hoje. Valor: R$ {l.valor:.2f}.",
            })
        elif dias <= l.dias_antecedencia:
            avisos.append({
                "lembrete_id": l.id,
                "titulo": l.titulo,
                "valor": l.valor,
                "data_vencimento": l.data_vencimento,
                "tipo": "proximo",
                "mensagem": f"{l.titulo} vence em {dias} dia(s). Valor: R$ {l.valor:.2f}.",
            })
    return avisos
