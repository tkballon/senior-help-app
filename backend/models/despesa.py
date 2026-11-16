"""
Modelo de Despesa
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Despesa:
    id: Optional[int] = None
    usuario_id: int = 0
    descricao: str = ""
    valor: float = 0.0
    categoria: str = "Outros"
    data_vencimento: str = ""
    paga: bool = False
    observacoes: str = ""
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "descricao": self.descricao,
            "valor": self.valor,
            "categoria": self.categoria,
            "data_vencimento": self.data_vencimento,
            "paga": self.paga,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Despesa":
        return cls(
            id=data.get("id"),
            usuario_id=int(data.get("usuario_id", 0)),
            descricao=data.get("descricao", ""),
            valor=float(data.get("valor", 0)),
            categoria=data.get("categoria", "Outros"),
            data_vencimento=data.get("data_vencimento", ""),
            paga=bool(data.get("paga", False)),
            observacoes=data.get("observacoes", ""),
            criado_em=data.get("criado_em", datetime.now().isoformat()),
        )
