"""
Modelo de Receita
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Receita:
    id: Optional[int] = None
    usuario_id: int = 0
    descricao: str = ""
    valor: float = 0.0
    frequencia: str = "mensal"
    data_recebimento: str = ""
    observacoes: str = ""
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "descricao": self.descricao,
            "valor": self.valor,
            "frequencia": self.frequencia,
            "data_recebimento": self.data_recebimento,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Receita":
        return cls(
            id=data.get("id"),
            usuario_id=int(data.get("usuario_id", 0)),
            descricao=data.get("descricao", ""),
            valor=float(data.get("valor", 0)),
            frequencia=data.get("frequencia", "mensal"),
            data_recebimento=data.get("data_recebimento", ""),
            observacoes=data.get("observacoes", ""),
            criado_em=data.get("criado_em", datetime.now().isoformat()),
        )
