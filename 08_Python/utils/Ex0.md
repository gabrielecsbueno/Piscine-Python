# Ex0 — construct.py (Ambientes Virtuais)

**Módulos autorizados:** `sys`, `os`, `site`, `print()`

---

## Comandos para a avaliação (execute na ordem)

```bash
# 1. Rodar FORA do venv
cd ex0/
python3 construct.py
# saída esperada: "MATRIX STATUS: You're still plugged in" + instruções

# 2. Criar o venv
python3 -m venv matrix_env

# 3. Ativar o venv
source matrix_env/bin/activate   # Mac/Linux
# matrix_env\Scripts\activate    # Windows

# 4. Rodar DENTRO do venv
python3 construct.py
# saída esperada: "MATRIX STATUS: Welcome to the construct" + caminhos

# 5. Desativar no final
deactivate
```

---

## Perguntas que o avaliador vai fazer — e como responder

### "O que é um ambiente virtual e por que é importante?"
Um ambiente virtual é uma cópia isolada do Python criada para um projeto específico.
Sem ele, todos os pacotes são instalados globalmente no sistema — o que causa
conflitos quando dois projetos precisam de versões diferentes da mesma biblioteca.
Com o venv, cada projeto tem seu próprio `pip`, seus próprios pacotes e seu próprio
executável Python, sem interferir em outros projetos ou no sistema.

### "Que problemas os ambientes virtuais resolvem?"
- Conflito de versões: projeto A precisa do pandas 1.x, projeto B precisa do 2.x
- Poluição do sistema: pacotes instalados globalmente ficam para sempre
- Reprodutibilidade: com venv + requirements.txt, qualquer pessoa recria o ambiente exato

### "Como o seu programa detecta se está dentro de um venv?"
```python
import sys

# sys.prefix      → caminho do Python em uso agora
# sys.base_prefix → caminho do Python original do sistema

if sys.prefix != sys.base_prefix:
    # está dentro de um venv — os caminhos são diferentes
else:
    # está no Python global — os caminhos são iguais
```
Quando o venv está ativo, o `sys.prefix` aponta para a pasta do venv.
Fora do venv, os dois são iguais (ambos apontam para o Python do sistema).

---

## O que o programa mostra em cada cenário

**Fora do venv:**
```
MATRIX STATUS: You're still plugged in

Current Python: /usr/bin/python3
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\Scripts\activate # On Windows

Then run this program again.
```

**Dentro do venv:**
```
MATRIX STATUS: Welcome to the construct

Current Python: /path/to/matrix_env/bin/python
Virtual Environment: matrix_env
Environment Path: /path/to/matrix_env

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
/path/to/matrix_env/lib/python3.x/site-packages
```

---

## Como o programa detecta o nome e caminho do venv

```python
import os

v_path = os.environ.get("VIRTUAL_ENV")
# VIRTUAL_ENV é uma variável de ambiente definida automaticamente
# pelo sistema quando você ativa um venv com source .../activate

v_name = os.path.basename(v_path) if v_path else 'None detected'
# basename pega só o nome da pasta final do caminho
# ex: "/Users/gabi/projeto/matrix_env" → "matrix_env"
```

## Como o programa mostra onde os pacotes são instalados

```python
import site

package_path = site.getsitepackages()
# retorna uma lista de diretórios onde o Python instala pacotes
# dentro do venv, aponta para a pasta do venv
# fora do venv, aponta para o Python do sistema

print(package_path[0])   # mostra o principal
```

---

## Pontos de atenção na avaliação

- A pasta `matrix_env/` **não deve estar no repositório** — está no `.gitignore`
- O programa deve funcionar nos **dois cenários** (dentro e fora do venv)
- Você deve ser capaz de criar o venv do zero durante a avaliação
