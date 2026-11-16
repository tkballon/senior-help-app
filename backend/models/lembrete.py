"""
Modelo de Lembrete de Conta
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Lembrete:
    id: Optional[int] = None
    usuario_id: int = 0
    titulo: str = ""
    valor: float = 0.0
    data_vencimento: str = ""
    frequencia: str = "mensal"
    status: str = "pendente"
    dias_antecedencia: int = 5
    observacoes: str = ""
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "titulo": self.titulo,
            "valor": self.valor,
            "data_vencimento": self.data_vencimento,
            "frequencia": self.frequencia,
            "status": self.status,
            "dias_antecedencia": self.dias_antecedencia,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Lembrete":
        return cls(
            id=data.get("id"),
            usuario_id=int(data.get("usuario_id", 0)),
            titulo=data.get("titulo", ""),
            valor=float(data.get("valor", 0)),
            data_vencimento=data.get("data_vencimento", ""),
            frequencia=data.get("frequencia", "mensal"),
            status=data.get("status", "pendente"),
            dias_antecedencia=int(data.get("dias_antecedencia", 5)),
            observacoes=data.get("observacoes", ""),
            criado_em=data.get("criado_em", datetime.now().isoformat()),
        )
