"""
Repositório — CRUD via Supabase.
"""

from datetime import datetime, date, timedelta
from typing import Any, Dict, List, Optional

from models import Usuario, Receita, Despesa, Lembrete, Conversa
from persistence.supabase_client import get_supabase


def _now() -> str:
    return datetime.now().isoformat()


class Repository:
    def criar_usuario(self, dados: Dict[str, Any]) -> Usuario:
        sb = get_supabase()
        payload = {
            "nome": dados.get("nome", ""),
            "data_nascimento": dados.get("data_nascimento"),
            "contato_confianca_nome": dados.get("contato_confianca_nome", ""),
            "contato_confianca_telefone": dados.get("contato_confianca_telefone", ""),
            "receber_lembretes": dados.get("receber_lembretes", True),
            "dias_antecedencia_aviso": int(dados.get("dias_antecedencia_aviso", 5)),
            "criado_em": _now(),
            "atualizado_em": _now(),
        }
        res = sb.table("usuarios").insert(payload).execute()
        return Usuario.from_dict(res.data[0])

    def buscar_usuario(self, usuario_id: int) -> Optional[Usuario]:
        sb = get_supabase()
        res = sb.table("usuarios").select("*").eq("id", usuario_id).limit(1).execute()
        if not res.data:
            return None
        return Usuario.from_dict(res.data[0])

    def atualizar_usuario(self, usuario_id: int, dados: Dict[str, Any]) -> Optional[Usuario]:
        sb = get_supabase()
        dados = {**dados, "atualizado_em": _now()}
        dados.pop("id", None)
        dados.pop("criado_em", None)
        res = sb.table("usuarios").update(dados).eq("id", usuario_id).execute()
        if not res.data:
            return None
        return Usuario.from_dict(res.data[0])

    def adicionar_receita(self, dados: Dict[str, Any]) -> Receita:
        sb = get_supabase()
        payload = {
            "usuario_id": int(dados["usuario_id"]),
            "descricao": dados.get("descricao", ""),
            "valor": float(dados.get("valor", 0)),
            "frequencia": dados.get("frequencia", "mensal"),
            "data_recebimento": dados.get("data_recebimento", ""),
            "observacoes": dados.get("observacoes", ""),
            "criado_em": _now(),
        }
        res = sb.table("receitas").insert(payload).execute()
        return Receita.from_dict(res.data[0])

    def listar_receitas(self, usuario_id: int, mes: Optional[str] = None) -> List[Receita]:
        sb = get_supabase()
        q = sb.table("receitas").select("*").eq("usuario_id", usuario_id)
        if mes:
            q = q.like("data_recebimento", f"{mes}%")
        res = q.order("data_recebimento", desc=True).execute()
        return [Receita.from_dict(r) for r in res.data]

    def adicionar_despesa(self, dados: Dict[str, Any]) -> Despesa:
        sb = get_supabase()
        payload = {
            "usuario_id": int(dados["usuario_id"]),
            "descricao": dados.get("descricao", ""),
            "valor": float(dados.get("valor", 0)),
            "categoria": dados.get("categoria", "Outros"),
            "data_vencimento": dados.get("data_vencimento", ""),
            "paga": bool(dados.get("paga", False)),
            "observacoes": dados.get("observacoes", ""),
            "criado_em": _now(),
        }
        res = sb.table("despesas").insert(payload).execute()
        return Despesa.from_dict(res.data[0])

    def listar_despesas(self, usuario_id: int, mes: Optional[str] = None) -> List[Despesa]:
        sb = get_supabase()
        q = sb.table("despesas").select("*").eq("usuario_id", usuario_id)
        if mes:
            q = q.like("data_vencimento", f"{mes}%")
        res = q.order("data_vencimento", desc=True).execute()
        return [Despesa.from_dict(r) for r in res.data]

    def marcar_despesa_paga(self, despesa_id: int) -> Optional[Despesa]:
        sb = get_supabase()
        res = sb.table("despesas").update({"paga": True}).eq("id", despesa_id).execute()
        if not res.data:
            return None
        return Despesa.from_dict(res.data[0])

    def criar_lembrete(self, dados: Dict[str, Any]) -> Lembrete:
        sb = get_supabase()
        payload = {
            "usuario_id": int(dados["usuario_id"]),
            "titulo": dados.get("titulo", ""),
            "valor": float(dados.get("valor", 0)),
            "data_vencimento": dados.get("data_vencimento", ""),
            "frequencia": dados.get("frequencia", "mensal"),
            "status": dados.get("status", "pendente"),
            "dias_antecedencia": int(dados.get("dias_antecedencia", 5)),
            "observacoes": dados.get("observacoes", ""),
            "criado_em": _now(),
        }
        res = sb.table("lembretes").insert(payload).execute()
        return Lembrete.from_dict(res.data[0])

    def listar_lembretes_pendentes(self, usuario_id: int) -> List[Lembrete]:
        sb = get_supabase()
        res = (
            sb.table("lembretes")
            .select("*")
            .eq("usuario_id", usuario_id)
            .eq("status", "pendente")
            .order("data_vencimento")
            .execute()
        )
        return [Lembrete.from_dict(r) for r in res.data]

    def listar_lembretes_proximos(self, usuario_id: int, dias: int = 7) -> List[Lembrete]:
        pendentes = self.listar_lembretes_pendentes(usuario_id)
        hoje = date.today()
        limite = hoje + timedelta(days=dias)
        resultado = []
        for l in pendentes:
            try:
                dv = date.fromisoformat(l.data_vencimento[:10])
            except Exception:
                continue
            if hoje <= dv <= limite:
                resultado.append(l)
        return resultado

    def marcar_lembrete_pago(self, lembrete_id: int) -> Optional[Lembrete]:
        sb = get_supabase()
        res = sb.table("lembretes").update({"status": "pago"}).eq("id", lembrete_id).execute()
        if not res.data:
            return None
        return Lembrete.from_dict(res.data[0])

    def registrar_conversa(self, dados: Dict[str, Any]) -> Conversa:
        sb = get_supabase()
        payload = {
            "usuario_id": int(dados["usuario_id"]),
            "tipo": dados.get("tipo", "duvida"),
            "conteudo": dados.get("conteudo", ""),
            "respondido": bool(dados.get("respondido", False)),
            "criado_em": _now(),
        }
        res = sb.table("conversas").insert(payload).execute()
        return Conversa.from_dict(res.data[0])

    def listar_conversas(self, usuario_id: int, limite: int = 20) -> List[Conversa]:
        sb = get_supabase()
        res = (
            sb.table("conversas")
            .select("*")
            .eq("usuario_id", usuario_id)
            .order("criado_em", desc=True)
            .limit(limite)
            .execute()
        )
        return [Conversa.from_dict(r) for r in res.data]
