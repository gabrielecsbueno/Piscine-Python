# Ex2 — oracle.py + .env.example + .gitignore

**Módulos autorizados:** `os`, `sys`, `python-dotenv`, operações de arquivo

---

## ATENÇÃO — Passos preliminares que o avaliador vai pedir

O avaliador vai pedir para você demonstrar ANTES de qualquer teste:

```bash
# 1. Mostrar que python-dotenv está no requirements.txt do ex1
cat ../ex1/requirements.txt
# deve aparecer: python-dotenv>=1.0.0

# 2. Criar e ativar um venv
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências a partir do ex1
pip install -r ../ex1/requirements.txt

# 4. Agora sim rodar o programa
python3 oracle.py
```

Se `python-dotenv` não estiver no `requirements.txt`, a avaliação **para aqui**.

---

## Comandos para a avaliação (execute na ordem)

```bash
cd ex2/

# 1. Rodar SEM nenhuma variável configurada
python3 oracle.py
# saída esperada: ORACLE STATUS + WARNING com as variáveis faltando

# 2. Criar o .env a partir do exemplo
cp .env.example .env
# editar o .env se quiser (ou deixar os valores do exemplo)

# 3. Rodar COM o .env
python3 oracle.py
# saída esperada: "Configuration loaded:" com todos os valores + [DEV] ou [PROD]

# 4. Testar override por variável de ambiente (tem prioridade sobre o .env)
MATRIX_MODE=production API_KEY=secret123 python3 oracle.py
# saída esperada: Mode: production + mensagens [PROD]
```

---

## Perguntas que o avaliador vai fazer — e como responder

### "Por que variáveis de ambiente são importantes para segurança?"
Se você colocar senhas, chaves de API ou URLs de banco de dados diretamente
no código, elas ficam no histórico do git para sempre — mesmo que você apague
depois. Qualquer pessoa com acesso ao repositório vê esses segredos.

Com variáveis de ambiente, o segredo fica fora do código. O código só lê o
valor em tempo de execução com `os.getenv()`. Cada ambiente (desenvolvimento,
produção, máquina de outro desenvolvedor) pode ter valores diferentes sem
mudar uma linha de código.

### "Qual a diferença entre development e production?"

**Development (desenvolvimento):**
- Ambiente local do programador
- Logs detalhados para facilitar o debug
- Banco de dados local
- Todos os valores de config visíveis para diagnóstico
- No nosso programa: mensagens `[DEV]` com debug ativo

**Production (produção):**
- Ambiente real, acessado pelos usuários finais
- Logs mínimos — não expõe informações internas
- Banco de dados remoto e seguro
- Variáveis de ambiente configuradas no servidor, não em arquivos .env
- No nosso programa: mensagens `[PROD]` com logging mínimo

A variável `MATRIX_MODE` controla qual comportamento o programa adota.

### "Como o python-dotenv ajuda no gerenciamento de configuração?"
```python
from dotenv import load_dotenv

load_dotenv()
# lê o arquivo .env e carrega cada linha como variável de ambiente
# IMPORTANTE: não sobrescreve variáveis que já existem no sistema
# isso significa que variáveis definidas no terminal têm prioridade
```
Sem o python-dotenv, você teria que exportar cada variável manualmente no
terminal antes de rodar o programa (`export API_KEY=...`). O .env automatiza
isso para o ambiente de desenvolvimento local.

### "Como o programa lida com configuração faltando?"
```python
validation = [x for x in keys_env if not getenv(x)]

if validation:
    print("WARNING: Missing configuration variables:")
    for var in validation:
        print(f"  [MISSING] {var}")
    # instrui o usuário como configurar e encerra
    return
```
O programa sempre mostra o cabeçalho `ORACLE STATUS` — mesmo sem configuração.
Se alguma variável estiver faltando, lista todas as ausentes com `[MISSING]`
e mostra como resolver. Não quebra com erro de Python.

### "Por que o .env está no .gitignore e o .env.example não?"
O `.env` pode conter senhas e chaves reais — nunca deve ser commitado.
O `.env.example` é um template com valores fictícios que mostra quais variáveis
o projeto precisa. Qualquer desenvolvedor que clonar o repositório sabe o que
configurar sem ter acesso aos segredos reais.

### "Como as variáveis de ambiente do sistema têm prioridade sobre o .env?"
`load_dotenv()` só define uma variável se ela ainda não existir no ambiente.
Se você rodar `MATRIX_MODE=production python3 oracle.py`, o `MATRIX_MODE`
já está definido no sistema — o `load_dotenv()` não o sobrescreve.
Isso é o comportamento correto: o sistema de produção define as variáveis
diretamente, sem usar .env.

---

## Saída esperada do programa

**Sem .env (variáveis faltando):**
```
ORACLE STATUS: Reading the Matrix...

WARNING: Missing configuration variables:
  [MISSING] MATRIX_MODE
  [MISSING] DATABASE_URL
  [MISSING] API_KEY
  [MISSING] LOG_LEVEL
  [MISSING] ZION_ENDPOINT

To configure, run:
  cp .env.example .env
  # Edit .env with your values
  python3 oracle.py
```

**Com .env (MATRIX_MODE=development):**
```
ORACLE STATUS: Reading the Matrix...

Configuration loaded:
Mode: development
Database: postgresql://host:port/dbname
API Access: my_key_secret
Log Level: DEBUG
Zion Network: http://your-endpoint

Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available

[DEV] Debug mode active - verbose logging enabled
[DEV] Using local database instance
[DEV] All config values visible for debugging

The Oracle sees all configurations.
```

**Com MATRIX_MODE=production no terminal:**
```
ORACLE STATUS: Reading the Matrix...

Configuration loaded:
Mode: production
...

[PROD] Production mode - minimal logging active
[PROD] Remote database - secure connection required
[PROD] Use env vars directly, not .env files in production

The Oracle sees all configurations.
```

---

## Como funciona o fluxo do programa

```
1. load_dotenv() — carrega o .env (sem sobrescrever vars do sistema)

2. Cria lista com os nomes de todas as variáveis obrigatórias

3. Sempre imprime o cabeçalho ORACLE STATUS

4. Verifica quais variáveis estão faltando (getenv retorna None se ausente)
   - se alguma faltar: mostra [MISSING] + instruções → encerra com return
   - se todas OK: continua

5. Imprime cada variável carregada

6. Verifica MATRIX_MODE e mostra comportamento diferente:
   - development → mensagens [DEV]
   - production  → mensagens [PROD]
```

---

## Verificação de segurança que o avaliador vai fazer

| Verificação | O que espera encontrar |
|---|---|
| `.env.example` | valores fictícios, sem senhas reais |
| `.gitignore` | `.env` listado |
| `oracle.py` | nenhum segredo hardcoded no código |
| `python-dotenv` | usado com `load_dotenv()`, não parser manual |

---

## Pontos de atenção na avaliação

- O `.env` **não deve existir no repositório** — criar na hora com `cp .env.example .env`
- O `python-dotenv` **deve estar no requirements.txt do ex1**
- Você deve demonstrar que o override de variável de ambiente funciona
- O programa deve mostrar saídas **visivelmente diferentes** para dev e production
