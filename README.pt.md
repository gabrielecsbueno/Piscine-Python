# Piscine Python

Repositório de exercícios da Piscine Python — uma série de módulos progressivos cobrindo desde os fundamentos da linguagem até tópicos avançados como programação funcional e validação de dados.

---

## Módulos

### 00 — Fundamentos (Growing Code)
Introdução à linguagem: variáveis, tipos primitivos, condicionais, loops, funções iterativas e recursivas, e type hints básicos.

**Conceitos:** `print`, `input`, operadores aritméticos/lógicos, `if/else`, `for/while`, recursão, type hints.

---

### 01 — Orientação a Objetos: Básico
Criação de classes com atributos e métodos, variáveis de classe vs. de instância, encapsulamento e strings formatadas.

**Conceitos:** `class`, `__init__`, atributos de instância e de classe, métodos, f-strings, listas de objetos.

---

### 02 — Tratamento de Exceções
Uso de `try/except/else/finally`, lançamento de exceções customizadas e boas práticas para código robusto.

**Conceitos:** `try/except/else/finally`, `raise`, exceções built-in (`ValueError`, `TypeError`), exceções customizadas.

---

### 03 — Argumentos e Coleções
Leitura de argumentos de linha de comando, manipulação de listas, dicionários, tuplas e geradores.

**Conceitos:** `sys.argv`, `list`, `dict`, `tuple`, `set`, list comprehensions, generator expressions.

---

### 04 — Manipulação de Arquivos
Abertura, leitura, escrita e gerenciamento de streams de arquivos; controle de permissões e tratamento de erros de I/O.

**Conceitos:** `open()`, modos de arquivo (`r`, `w`, `a`), context managers (`with`), `sys.argv` para leitura de paths.

---

### 05 — Classes Abstratas e Herança
Definição de interfaces com `ABC`, implementação de métodos abstratos e polimorfismo via herança concreta.

**Conceitos:** `ABC`, `@abstractmethod`, herança, polimorfismo, módulo `typing`, filas com `list.pop(0)`.

---

### 06 — Módulos e Pacotes (Alchemy)
Organização de código em pacotes com `__init__.py`, diferentes formas de import e detecção de dependências circulares.

**Conceitos:** `import`, `from ... import`, `__init__.py`, namespaces, dependências circulares, `ImportError`.

---

### 07 — Padrões de Projeto (Battle)
Implementação dos padrões Abstract Factory, Mixin e Strategy em um sistema de batalha de criaturas com torneio.

**Conceitos:** Abstract Factory, Multiple Inheritance (Mixins), Strategy Pattern, `@abstractmethod`, polimorfismo, tratamento de exceções em fluxos de jogo.

---

### 08 — Ambientes Virtuais e APIs Externas
Criação e detecção de ambientes virtuais com `venv`, uso de instalações de pacotes com `pip` e `poetry`

**Conceitos:** `venv`, `sys.prefix` vs `sys.base_prefix`, `pip`, `requirements.txt`, `pyproject.toml`, variáveis de ambiente (`.env`), `requests`.

---

### 09 — Validação de Dados com Pydantic
Modelagem e validação de dados com Pydantic v2: modelos básicos, validadores customizados e modelos aninhados.

**Conceitos:** `BaseModel`, `Field`, `@model_validator`, `Enum`, modelos aninhados, `ValidationError`, type coercion automático.

---

### 10 — Programação Funcional (FuncMage)
Funções como cidadãos de primeira classe: lambdas, higher-order functions, closures, `functools` e decorators.

**Conceitos:** `lambda`, `map/filter/sorted`, `Callable`, closures, `nonlocal`, `functools.reduce/partial/lru_cache/singledispatch`, decorators, `functools.wraps`, `@staticmethod`.

---

## Como executar

### Pré-requisitos
- Python 3.10 ou superior
- `flake8` e `mypy` para verificação de estilo e tipos (opcionais, mas recomendados)

```bash
pip install flake8 mypy
```

### Executando um exercício
Cada exercício é um arquivo Python independente. Execute diretamente:

```bash
python3 00_Python/ex2/ft_plot_area.py
python3 03_Python/ex0/ft_command_quest.py argumento1 argumento2
python3 04_Python/ex0/ft_ancient_text.py 04_Python/ex0/ancient_fragment.txt
```

### Usando o helper do módulo 00
O módulo 00 inclui um menu interativo para testar os exercícios:

```bash
cd 00_Python
python3 main.py
```

### Módulos com pacotes (06 e 07)
Os módulos com estrutura de pacote devem ser executados a partir da raiz do módulo:

```bash
cd 06_Python
python3 ft_alembic_0.py
python3 ft_transmutation_2.py

cd 07_Python
python3 battle.py
python3 tournament.py
```

### Módulo 08 — Ambiente virtual
```bash
cd 08_Python/ex0
python3 construct.py              # fora do venv
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py              # dentro do venv
deactivate
```

### Módulo 09 — Pydantic (requer instalação)
```bash
cd 09_Python
python3 -m venv venv
source venv/bin/activate
pip install pydantic
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```
