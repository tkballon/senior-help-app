"""
Funções que o frontend (ou scripts) consomem.
"""

from datetime import datetime
from typing import Any, Dict, Optional

from persistence import Repository
from services import resumo_mes, obter_avisos


class FuncoesAPI:
    def __init__(self):
        self.repo = Repository()

    def criar_usuario(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        u = self.repo.criar_usuario(dados)
        return {"ok": True, "usuario": u.to_dict()}

    def buscar_usuario(self, usuario_id: int) -> Dict[str, Any]:
        u = self.repo.buscar_usuario(usuario_id)
        if not u:
            return {"ok": False, "erro": "Usuário não encontrado"}
        return {"ok": True, "usuario": u.to_dict()}

    def atualizar_usuario(self, usuario_id: int, dados: Dict[str, Any]) -> Dict[str, Any]:
        u = self.repo.atualizar_usuario(usuario_id, dados)
        if not u:
            return {"ok": False, "erro": "Usuário não encontrado"}
        return {"ok": True, "usuario": u.to_dict()}

    def adicionar_receita(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        r = self.repo.adicionar_receita(dados)
        return {"ok": True, "receita": r.to_dict()}

    def listar_receitas(self, usuario_id: int, mes: Optional[str] = None) -> Dict[str, Any]:
        lista = self.repo.listar_receitas(usuario_id, mes)
        return {"ok": True, "receitas": [r.to_dict() for r in lista]}

    def adicionar_despesa(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        d = self.repo.adicionar_despesa(dados)
        return {"ok": True, "despesa": d.to_dict()}

    def listar_despesas(self, usuario_id: int, mes: Optional[str] = None) -> Dict[str, Any]:
        lista = self.repo.listar_despesas(usuario_id, mes)
        return {"ok": True, "despesas": [d.to_dict() for d in lista]}

    def marcar_despesa_paga(self, despesa_id: int) -> Dict[str, Any]:
        d = self.repo.marcar_despesa_paga(despesa_id)
        if not d:
            return {"ok": False, "erro": "Despesa não encontrada"}
        return {"ok": True, "despesa": d.to_dict()}

    def obter_resumo_mes(self, usuario_id: int, mes: Optional[str] = None) -> Dict[str, Any]:
        if not mes:
            mes = datetime.now().strftime("%Y-%m")
        receitas = self.repo.listar_receitas(usuario_id, mes)
        despesas = self.repo.listar_despesas(usuario_id, mes)
        return {"ok": True, "resumo": resumo_mes(receitas, despesas, mes)}

    def criar_lembrete(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        l = self.repo.criar_lembrete(dados)
        return {"ok": True, "lembrete": l.to_dict()}

    def listar_lembretes_pendentes(self, usuario_id: int) -> Dict[str, Any]:
        lista = self.repo.listar_lembretes_pendentes(usuario_id)
        return {"ok": True, "lembretes": [l.to_dict() for l in lista]}

    def listar_lembretes_proximos(self, usuario_id: int, dias: int = 7) -> Dict[str, Any]:
        lista = self.repo.listar_lembretes_proximos(usuario_id, dias)
        return {"ok": True, "lembretes": [l.to_dict() for l in lista]}

    def marcar_lembrete_pago(self, lembrete_id: int) -> Dict[str, Any]:
        l = self.repo.marcar_lembrete_pago(lembrete_id)
        if not l:
            return {"ok": False, "erro": "Lembrete não encontrado"}
        return {"ok": True, "lembrete": l.to_dict()}

    def obter_avisos_lembretes(self, usuario_id: int) -> Dict[str, Any]:
        pendentes = self.repo.listar_lembretes_pendentes(usuario_id)
        return {"ok": True, "avisos": obter_avisos(pendentes)}

    def registrar_conversa(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        c = self.repo.registrar_conversa(dados)
        return {"ok": True, "conversa": c.to_dict()}

    def listar_conversas(self, usuario_id: int, limite: int = 20) -> Dict[str, Any]:
        lista = self.repo.listar_conversas(usuario_id, limite)
        return {"ok": True, "conversas": [c.to_dict() for c in lista]}
