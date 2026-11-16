-- Senior Help — Schema Supabase
-- Execute no SQL Editor do Supabase (Dashboard > SQL Editor > New query)

-- ===================== USUARIOS =====================
create table if not exists usuarios (
  id bigserial primary key,
  nome text not null default '',
  data_nascimento text,
  contato_confianca_nome text not null default '',
  contato_confianca_telefone text not null default '',
  receber_lembretes boolean not null default true,
  dias_antecedencia_aviso integer not null default 5,
  criado_em timestamptz not null default now(),
  atualizado_em timestamptz not null default now()
);

-- ===================== RECEITAS =====================
create table if not exists receitas (
  id bigserial primary key,
  usuario_id bigint not null references usuarios(id) on delete cascade,
  descricao text not null default '',
  valor numeric(12,2) not null default 0,
  frequencia text not null default 'mensal',
  data_recebimento text not null default '',
  observacoes text not null default '',
  criado_em timestamptz not null default now()
);

create index if not exists idx_receitas_usuario on receitas(usuario_id);

-- ===================== DESPESAS =====================
create table if not exists despesas (
  id bigserial primary key,
  usuario_id bigint not null references usuarios(id) on delete cascade,
  descricao text not null default '',
  valor numeric(12,2) not null default 0,
  categoria text not null default 'Outros',
  data_vencimento text not null default '',
  paga boolean not null default false,
  observacoes text not null default '',
  criado_em timestamptz not null default now()
);

create index if not exists idx_despesas_usuario on despesas(usuario_id);

-- ===================== LEMBRETES =====================
create table if not exists lembretes (
  id bigserial primary key,
  usuario_id bigint not null references usuarios(id) on delete cascade,
  titulo text not null default '',
  valor numeric(12,2) not null default 0,
  data_vencimento text not null default '',
  frequencia text not null default 'mensal',
  status text not null default 'pendente',
  dias_antecedencia integer not null default 5,
  observacoes text not null default '',
  criado_em timestamptz not null default now()
);

create index if not exists idx_lembretes_usuario on lembretes(usuario_id);
create index if not exists idx_lembretes_status on lembretes(status);

-- ===================== CONVERSAS =====================
create table if not exists conversas (
  id bigserial primary key,
  usuario_id bigint not null references usuarios(id) on delete cascade,
  tipo text not null default 'duvida',
  conteudo text not null default '',
  respondido boolean not null default false,
  criado_em timestamptz not null default now()
);

create index if not exists idx_conversas_usuario on conversas(usuario_id);

-- ===================== RLS =====================
alter table usuarios enable row level security;
alter table receitas enable row level security;
alter table despesas enable row level security;
alter table lembretes enable row level security;
alter table conversas enable row level security;

create policy "dev_all_usuarios" on usuarios for all using (true) with check (true);
create policy "dev_all_receitas" on receitas for all using (true) with check (true);
create policy "dev_all_despesas" on despesas for all using (true) with check (true);
create policy "dev_all_lembretes" on lembretes for all using (true) with check (true);
create policy "dev_all_conversas" on conversas for all using (true) with check (true);
