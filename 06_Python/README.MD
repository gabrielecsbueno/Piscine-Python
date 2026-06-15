#### esse readme nao sera entregue no repo42

# ESTRUTURA BASICA DO PROJETO

```
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── grimoire/
│   │   ├── __init__.py
│   │   ├── dark_spellbook.py
│   │   ├── dark_validator.py
│   │   ├── light_spellbook.py
│   │   └── light_validator.py
│   ├── potions.py
│   └── transmutation/
│       ├── __init__.py
│       └── recipes.py
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_alembic_2.py
├── ft_alembic_3.py
├── ft_alembic_4.py
├── ft_alembic_5.py
├── ft_distillation_0.py
├── ft_distillation_1.py
├── ft_kaboom_0.py
├── ft_kaboom_1.py
├── ft_transmutation_0.py
├── ft_transmutation_1.py
└── ft_transmutation_2.py
```

# FUNCOES

## Componentes : O Alambique

### elements.py
- create_fire(): retorna a string `“Fire element created”`
- create_water(): retorna a string `“Water element created”`

### alchemy/elements.py
- create_earth(): retorna a string `“Earth element created”`
- create_air(): retorna a string `“Air element created”`

### alchemy/__init__.py
- Qualquer coisa util para importar parcialmente o modulo alchemy

### alchemy/potions.py
- healing_potion(): retorna a string `"Healing potion brewed with '[Created earth
element]' and '[Created air element]"`
- strength_potion(): retorna a string `"Strength potion brewed with '[Created fire element]' and '[Created water element]"`
- Qualquer outra coisa util para acessar os quatro elementos fundamentais.

### alchemy/transmutation/recipes.py
- lead_to_gold(): retorna a string `"Recipe transmuting Lead to Gold: brew ’[created air]’ and ’[created strength potion]’ mixed with ’[created fire]’"`

### alchemy/grimoire/light_spellbook.py
- light_spell_allowed_ingredients(): retorna uma lista de ingredientes permitidos para a magia da luz: `earth`, `air`, `fire`, `water`

- light_spell_record(spell_name: str, ingredients: str): retorna uma string indicando se o feitico foi registrado ou rejeitado.

A decisao vem da funcao de validacao (descrita em `alchemy/grimoire/light_validator.py`)

### alchemy/grimoire/light_validator.py
- validate_ingredients(ingredients: str): retorna uma string com os ingredientes e a palavra-chave `VALID` ou `INVALID`.
Os ingredientes sao validos se incluirem pelo menos um dos ingredientes permitidos do grimorio (sem distinacao entre maiusculas e minusculas).

### alchemy/grimoire/dark_spellbook.py
- dark_spell_allowed_ingredients(): retorna uma lista de ingredientes permitidos para a magia das trevas: `bats`, `frogs`, `arsenic`, and `eyeball`

- dark_spell_record(spell_name: str, ingredients: str): retorna uma string indicando se o feitico foi registrado ou rejeitado.

A decisao vem da funcao de validacao (descrita em `alchemy/grimoire/dark_validator.py`)

### alchemy/grimoire/dark_validator.py
- validate_ingredients(ingredients: str): retorna uma string com os ingredientes e a palavra-chave `VALID` ou `INVALID`.
Os ingredientes sao validos se incluirem pelo menos um dos ingredientes permitidos do grimorio (sem distinacao entre maiusculas e minusculas).

### Scripts:

### ft_alembic_0.py
- Usa a estrutura `import ...` para acessar `elements.py` diretamente e entao criar fogo.

```bash
$> python3 ft_alembic_0.py
=== Alembic 0 ===
Using: 'import ...' structure to access elements.py
Testing create_fire: Fire element created
```

### ft_alembic_1.py
Usa a estrutura `from ... import ...` para acessar `elements.py` diretamente e entao criar agua.

```bash
$> python3 ft_alembic_1.py
=== Alembic 1 ===
Using: 'from ... import ...' structure to access elements.py
Testing create_water: Water element created
```

### ft_alembic_2.py
- Usa a estrutura `import ...` para acessar `alchemy/elements.py` diretamente e entao criar terra.

```bash
$> python3 ft_alembic_2.py
=== Alembic 2 ===
Accessing alchemy/elements.py using 'import ...' structure
Testing create_earth: Earth element created
```

### ft_alembic_3.py
- Usa a estrutura `from ... import ...` para acessar `alchemy/elements.py` diretamente e entao criar ar.

```bash
$> python3 ft_alembic_3.py
=== Alembic 3 ===
Accessing alchemy/elements.py using 'from ... import ...' structure
Testing create_air: Air element created
```

### ft_alembic_4.py
- Usa `import alchemy` para acessar o modulo `alchemy` e entao criar ar. A funcao `create_earth()` nao é exposta pela interface do modulo e lanca uma excecao quando chamada (se pode capturar a excecao ou nao, isso serve apenas para fins pedagogicos). Um erro de mypy tambem sera gerado, novamente, intencionalmente.

```bash
$> python3 ft_alembic_4.py
=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: Air element created
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth: Traceback (most recent call last):
  File "/tmp/Python/module-06/ft_alembic_4.py", line 12, in <module>
print(f"{alchemy.create_earth()}")
        ^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'alchemy' has no attribute 'create_earth'. Did you mean: 'create_air'?
```

### ft_alembic_5.py
- Usa a estrutura `from alchemy import ...` para acessar o modulo `alchemy` e entao criar ar.

```bash
$> python3 ft_alembic_5.py
=== Alembic 5 ===
Accessing the alchemy module using 'from alchemy import ...'
Testing create_air: Air element created
```

### ft_distillation_0.py
- Usa a estrutura `from ... import ...` para acessar `alchemy/potions.py` diretamente e entao preparar ambas as pocoes de cura e forca.

```bash
$> python3 ft_distillation_0.py
=== Distillation 0 ===
Direct access to alchemy/potions.py
Testing strength_potion: Strength potion brewed with 'Fire element created' and 'Water element created'
Testing healing_potion: Healing potion brewed with 'Earth element created' and 'Air element created'
```

### ft_distillation_1.py
- Usa a estrutura `import alchemy` para acessar o modulo `alchemy`, e entao preparar a pocao de forca original e a pocao especial `heal()`, que e um alias do pacote para a pocao de cura.

```bash
$> python3 ft_distillation_1.py
=== Distillation 1 ===
Using: 'import alchemy' structure to access potions
Testing strength_potion: Strength potion brewed with 'Fire element created' and 'Water element created'
Testing heal alias: Healing potion brewed with 'Earth element created' and 'Air element created'
```

### ft_transmutation_0.py
- Usa a estrutura `import ...` para acessar `alchemy/transmutation/recipes.py` diretamente e entao realizar a transformacao de chumbo em ouro

```bash
$> python3 ft_transmutation_0.py
=== Transmutation 0 ===
Using file alchemy/transmutation/recipes.py directly
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion
     brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

### ft_transmutation_1.py
- Usa a estrutura `import ...` para importar o modulo `transmutation` diretamente e entao realizar a transformacao de chumbo em ouro

```bash
$> python3 ft_transmutation_1.py
=== Transmutation 1 ===
Import transmutation module directly
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion
brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

### ft_transmutation_2.py
- Usa a estrutura `import ...` para importar o modulo `alchemy` diretamente e entao realizar a transformacao de chumbo em ouro

```bash
$> python3 ft_transmutation_2.py
=== Transmutation 2 ===
Import alchemy module only
Testing lead to gold: Recipe transmuting Lead to Gold: brew 'Air element created' and 'Strength potion
brewed with 'Fire element created' and 'Water element created'' mixed with 'Fire element created'
```

Os scripts abaixo demonstram como evitar dependencias circulares:

### ft_kaboom_0.py
- Acessa o modulo `grimoire` diretamente e entao registra um feitico de luz, sem problemas. Demonstra a maneira que utiliza para evitar dependencias circulares. Explicar as diferentes abordagens.

```bash
$> python3 ft_kaboom_0.py
=== Kaboom 0 ===
Using grimoire module directly
Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)
```

### ft_kaboom_1.py
- Acessa secretamente `dark_spellbook.py` diretamente e tenta registrar um feitico negro. Se isso falhar e lanca uma excecao (pode captura-la ou nao; e apenas para fins pedagogicos), indicando que seu laboratorio alquimico acabou de explodir.

```bash
$> python3 ft_kaboom_1.py
=== Kaboom 1 ===
Access to alchemy/grimoire/dark_spellbook.py directly
Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION
Traceback (most recent call last):
File "/tmp/Python/module-06/ft_kaboom_1.py", line 7, in <module>
  from alchemy.grimoire.dark_spellbook import dark_spell_record
File "/tmp/Python/module-06/alchemy/grimoire/dark_spellbook.py", line 2, in <module>
  from .dark_validator import validate_ingredients
File "/tmp/Python/module-06/alchemy/grimoire/dark_validator.py", line 2, in <module>
  from .dark_spellbook import dark_spell_allowed_ingredients
ImportError: cannot import name 'dark_spell_allowed_ingredients' from partially initialized module '
     alchemy.grimoire.dark_spellbook' (most likely due to a circular import) (/tmp/Python/module-06/
alchemy/grimoire/dark_spellbook.py)
```


***OBSERVACOES***
You may face flake8 / mypy errors over your __init__.py file. Follow usual conventions in this situation.