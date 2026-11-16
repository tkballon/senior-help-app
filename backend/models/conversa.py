"""
Modelo de Conversa / Interação
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Conversa:
    id: Optional[int] = None
    usuario_id: int = 0
    tipo: str = "duvida"
    conteudo: str = ""
    respondido: bool = False
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "tipo": self.tipo,
            "conteudo": self.conteudo,
            "respondido": self.respondido,
            "criado_em": self.criado_em,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Conversa":
        return cls(
            id=data.get("id"),
            usuario_id=int(data.get("usuario_id", 0)),
            tipo=data.get("tipo", "duvida"),
            conteudo=data.get("conteudo", ""),
            respondido=bool(data.get("respondido", False)),
            criado_em=data.get("criado_em", datetime.now().isoformat()),
        )
