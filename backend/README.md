# Senior Help – Backend

Python + Supabase.

## Setup rápido

1. **Criar projeto no Supabase**  
   https://supabase.com → New project

2. **Rodar o schema**  
   No dashboard: **SQL Editor** → cole o conteúdo de `supabase_schema.sql` → Run

3. **Credenciais**  
   Project Settings → API  
   - Project URL → `SUPABASE_URL`  
   - `service_role` (secret) → `SUPABASE_KEY`

4. **Arquivo .env**
   ```bash
   cd backend
   cp .env.example .env
   # edite .env com URL e KEY
   ```

5. **Instalar e testar**
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

## Estrutura

```
backend/
├── api/funcoes.py
├── models/
├── persistence/
│   ├── supabase_client.py
│   └── repository.py
├── services/
├── supabase_schema.sql
├── config.py
├── main.py
└── .env.example
```

## Funções principais

- `criar_usuario` / `buscar_usuario` / `atualizar_usuario`
- `adicionar_receita` / `listar_receitas`
- `adicionar_despesa` / `listar_despesas` / `marcar_despesa_paga`
- `obter_resumo_mes`
- `criar_lembrete` / `listar_lembretes_pendentes` / `obter_avisos_lembretes`
- `registrar_conversa` / `listar_conversas`

## Segurança

- Backend usa **service_role** (não exponha no frontend).
- RLS ligado; policies abertas só para desenvolvimento.
- Depois do login de usuário, ajuste as policies.
