# Senior Help – Backend (Pessoa 2)

Backend em Python responsável pela lógica de negócio, modelos de dados, cálculos, lembretes e persistência.

## Estrutura

```
backend/
├── api/
│   └── funcoes.py          # Funções que o frontend consome
├── models/
│   ├── usuario.py
│   ├── receita.py
│   ├── despesa.py
│   ├── lembrete.py
│   └── conversa.py
├── persistence/
│   ├── database.py         # SQLite
│   └── repository.py       # CRUD
├── services/
│   ├── calculos.py         # Totais, saldos e resumos
│   ├── lembretes.py        # Sistema de lembretes
│   └── alertas.py          # Alertas calmos e educativos
├── config.py
├── main.py                 # Exemplo de uso
└── requirements.txt
```

## Como rodar o exemplo

```bash
cd backend
python main.py
```

O banco SQLite será criado automaticamente.

## Funções principais (para o frontend)

### Usuário
- `criar_usuario(dados)`
- `buscar_usuario(usuario_id)`
- `atualizar_usuario(usuario_id, dados)`

### Receitas e Despesas
- `adicionar_receita(dados)`
- `listar_receitas(usuario_id, mes=None)`
- `adicionar_despesa(dados)`
- `listar_despesas(usuario_id, mes=None)`
- `marcar_despesa_paga(despesa_id)`
- `obter_resumo_mes(usuario_id, mes=None)`

### Lembretes
- `criar_lembrete(dados)`
- `listar_lembretes_pendentes(usuario_id)`
- `listar_lembretes_proximos(usuario_id, dias=7)`
- `marcar_lembrete_pago(lembrete_id)`
- `obter_avisos_lembretes(usuario_id)`

### Apoio / Conversas
- `registrar_conversa(dados)`
- `listar_conversas(usuario_id, limite=20)`

## Regras importantes

- Tudo é **educativo e informativo**.
- Nunca dá recomendação de investimento.
- Mensagens de alerta são sempre **calmas e simples**.
- Não armazena dados sensíveis de banco.
- Linguagem clara, pensada para idosos.
