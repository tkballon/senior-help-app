"""
Modelo de Usuário (Idoso)
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Usuario:
    id: Optional[int] = None
    nome: str = ""
    data_nascimento: Optional[str] = None
    contato_confianca_nome: str = ""
    contato_confianca_telefone: str = ""
    receber_lembretes: bool = True
    dias_antecedencia_aviso: int = 5
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())
    atualizado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "contato_confianca_nome": self.contato_confianca_nome,
            "contato_confianca_telefone": self.contato_confianca_telefone,
            "receber_lembretes": self.receber_lembretes,
            "dias_antecedencia_aviso": self.dias_antecedencia_aviso,
            "criado_em": self.criado_em,
            "atualizado_em": self.atualizado_em,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Usuario":
        return cls(
            id=data.get("id"),
            nome=data.get("nome", ""),
            data_nascimento=data.get("data_nascimento"),
            contato_confianca_nome=data.get("contato_confianca_nome", ""),
            contato_confianca_telefone=data.get("contato_confianca_telefone", ""),
            receber_lembretes=bool(data.get("receber_lembretes", True)),
            dias_antecedencia_aviso=int(data.get("dias_antecedencia_aviso", 5)),
            criado_em=data.get("criado_em", datetime.now().isoformat()),
            atualizado_em=data.get("atualizado_em", datetime.now().isoformat()),
        )
