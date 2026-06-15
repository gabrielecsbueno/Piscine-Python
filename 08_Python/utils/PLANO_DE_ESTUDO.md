# Python 08: The Matrix

Projeto de Engenharia de Dados com 3 exercícios focados em:
ambientes virtuais, gerenciamento de pacotes e configuração segura de ambiente.

---

## Requisitos técnicos obrigatórios (todos os exercícios)

| Ferramenta | O que precisa saber |
|---|---|
| Python 3.10+ | Sintaxe atual, type hints com `match`, `|` union types |
| flake8 | Verificar estilo: `flake8 arquivo.py` |
| mypy | Verificar tipos: `mypy arquivo.py` |
| Anotações de tipo | `def func(x: int) -> str:`, `Optional`, `Union`, `list[str]` |
| Tratamento de exceções | `try/except`, exceções customizadas, não deixar dados corrompidos |

---

## O que é Venv?

O Venv é uma ferramenta integrada ao Python que permite criar ambientes virtuais isolados.
Esses ambientes são importantes porque permitem que cada projeto tenha suas próprias dependências, sem interferir em outros projetos.
Isso é crucial para evitar conflitos de versão e garantir que o software funcione de maneira consistente em diferentes máquinas e configurações.
Em um mundo onde os projetos podem exigir diferentes versões de bibliotecas, o Venv torna-se uma solução simples e eficaz para gerenciar essas dependências.

---

## Estrutura de diretórios esperada

```
ex0/
└── construct.py

ex1/
├── loading.py
├── requirements.txt
└── pyproject.toml

ex2/
├── oracle.py
├── .env.example
└── .gitignore
```

---

## Checklist antes da entrega

### Ex0
- [ ] Detecta corretamente quando está dentro/fora do venv
- [ ] Mostra caminho do Python atual (`sys.executable`)
- [ ] Mostra caminho de instalação de pacotes (`site`)
- [ ] Mostra instruções de criação do venv quando fora
- [ ] Sem `matrix_env/` no repositório
- [ ] `mypy` sem erros, `flake8` sem erros

### Ex1
- [ ] `requirements.txt` com versões corretas
- [ ] `pyproject.toml` válido para Poetry
- [ ] Dados gerados com `numpy` (não listas/range)
- [ ] `pandas` para manipulação do DataFrame
- [ ] `matplotlib` salva imagem `.png`
- [ ] Detecta dependências ausentes e mostra como instalar
- [ ] Mostra versões dos pacotes instalados
- [ ] Mostra diferença pip vs Poetry

### Ex2
- [ ] `.env` listado no `.gitignore`
- [ ] `.env.example` commitado (sem valores reais)
- [ ] Usa `python-dotenv`, não parser manual
- [ ] Trata variáveis ausentes com mensagem clara
- [ ] Comportamento diferente dev vs prod visível na saída
- [ ] Variáveis do sistema têm prioridade sobre `.env`
- [ ] `mypy` sem erros, `flake8` sem erros

---

## Comandos de referência rápida

```bash
# Ambiente virtual para pip
python3.10 -m venv matrix_env_pip
source matrix_env/bin/activate.fish # se estiver usando o fish
deactivate

# pip
pip list
pip install -r requirements.txt
pip freeze > requirements.txt
pip list

# aqui testar o exercicio 1

# Poetry
pip install poetry
poetry init
poetry add pandas numpy matplotlib
poetry install
poetry run python loading.py

# Verificação de qualidade
flake8 arquivo.py
mypy arquivo.py

# python-dotenv
pip install python-dotenv
```

### REFERENCIAS

Python: Venv e Poetry para criar ambientes virtuais - [https://www.alura.com.br/artigos/ven-poetry-no-python?srsltid=AfmBOoolTLtKUCn0k1fTqPPIOdQc6oUqyygAJC9mslwdzj_BqwhSV4we]