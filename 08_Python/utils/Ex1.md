# Ex1 — loading.py + requirements.txt + pyproject.toml

**Módulos autorizados:** `pandas`, `requests`, `matplotlib`, `numpy`, `sys`, `importlib`

---

## Comandos para a avaliação (execute na ordem)

```bash
cd ex1/

# 1. Testar SEM dependências instaladas
python3 loading.py
# saída esperada: [KO] + mensagem de erro + instrução de como instalar

# 2. Instalar com pip
pip install -r requirements.txt

# 3. Rodar com pip instalado
python3 loading.py
# saída esperada: [OK] para cada pacote + comparação pip vs Poetry + gráfico salvo

# 4. Testar com Poetry (se disponível)
poetry install
poetry run python loading.py
# saída esperada: mesma saída — Poetry só muda como gerencia, não como executa
```

---

## Perguntas que o avaliador vai fazer — e como responder

### "Qual a diferença entre pip e Poetry?"

| | pip | Poetry |
|---|---|---|
| Arquivo de deps | `requirements.txt` | `pyproject.toml` |
| Instalar | `pip install -r requirements.txt` | `poetry install` |
| Executar | `python3 loading.py` | `poetry run python loading.py` |
| Lock file | não tem (opcional: `pip freeze`) | `poetry.lock` gerado automaticamente |
| Resolução de conflitos | manual | automática |

**pip:** você escreve as dependências manualmente no `requirements.txt`.
Se dois pacotes precisam de versões incompatíveis, o pip não avisa — você descobre
quando o programa quebra.

**Poetry:** gera um arquivo `poetry.lock` com as versões exatas de tudo (inclusive
dependências de dependências). Qualquer pessoa que rodar `poetry install` terá
exatamente o mesmo ambiente — isso se chama reprodutibilidade.

### "Por que o gerenciamento de dependências é importante?"
Sem ele, cada desenvolvedor instala versões diferentes dos pacotes e o programa
funciona na máquina de um mas quebra na do outro. Em produção, isso pode derrubar
um sistema inteiro. O `requirements.txt` (pip) e o `pyproject.toml` (Poetry)
garantem que o ambiente seja replicável em qualquer máquina.

### "Como o programa detecta dependências ausentes?"
```python
from importlib import util, metadata

def check_spec(name: str) -> str | None:
    check = util.find_spec(name)   # retorna None se o módulo não existir
    if check:
        return metadata.version(name)  # retorna a versão instalada
    else:
        return None
```
`importlib.util.find_spec()` tenta localizar o módulo sem importá-lo.
Se retornar `None`, o pacote não está instalado. Assim o programa não quebra —
ele avisa o usuário de forma controlada.

### "Como você simula os dados? Por que não pode ser hardcoded?"
```python
import numpy as np

timestamps = np.linspace(0, 10, 1000)       # 1000 pontos de 0 a 10
signal     = np.random.uniform(0, 100, 1000) # 1000 números aleatórios
noise      = np.random.uniform(0, 100, 1000) # mais 1000 números aleatórios
```
Os dados vêm do numpy — são gerados aleatoriamente a cada execução.
O enunciado proíbe listas hardcoded (`[1, 2, 3, ...]`) e `range()` porque
eles não demonstram o uso de numpy para computação numérica.

---

## Saída esperada do programa

```
LOADING STATUS: Loading programs...

Checking dependencies:
[OK] pandas (2.x.x) - Data manipulation ready
[OK] numpy (1.x.x) - Numerical computation ready
[OK] matplotlib (3.x.x) - Visualization ready

Package Manager Comparison:

pip (requirements.txt):
 Install:    pip install -r requirements.txt
 Manage:     versions defined manually, no automatic lock file

Poetry (pyproject.toml):
 Install:    poetry install
 Run:        poetry run python loading.py
 Manage:     generates poetry.lock automatically (exact versions)

Main difference:
 pip:    you control versions manually
 Poetry: generates a lock file, ensuring reproducibility

Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...

Analysis complete!
Results saved to: matrix_analysis.png
```

---

## Sobre os arquivos de dependência

### requirements.txt (para pip)
```
pandas>=2.1.0
numpy>=1.25.0
matplotlib>=3.7.2
python-dotenv>=1.0.0
```
O `python-dotenv` está aqui porque o ex2 vai pedir para instalar a partir
deste arquivo. O avaliador vai verificar isso.

### pyproject.toml (para Poetry)
Usa o formato `[project]` compatível com PEP 621:
```toml
[project]
name = "matrix-loading"
version = "0.1.0"
requires-python = "^3.10"
dependencies = [
    "pandas (>=2.1.0)",
    "numpy (>=1.25.0)",
    "matplotlib (>=3.7.2)"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## Como funciona o fluxo do programa

```
1. check_dependencies() — verifica cada pacote com importlib.util.find_spec()
   - se faltar algum: imprime [KO] + instrução para instalar → encerra
   - se todos OK: imprime [OK] com a versão → continua

2. show_pip_poetry() — explica a diferença entre pip e Poetry

3. numpy gera os dados:
   - timestamps: 1000 pontos igualmente espaçados (np.linspace)
   - signal e noise: 1000 números aleatórios (np.random.uniform)

4. pandas organiza em DataFrame com colunas nomeadas

5. matplotlib gera o gráfico e salva como matrix_analysis.png
```

---

## Pontos de atenção na avaliação

- Os dados **devem vir do numpy** — não pode ser lista ou range()
- O programa deve rodar igual com pip e com Poetry
- `python-dotenv` **deve estar no requirements.txt** (o avaliador verifica)
- Erros de mypy em imports de numpy/pandas/matplotlib são **permitidos** pelo enunciado
