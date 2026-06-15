# Plano de Estudo — FuncMage (9 horas)

---

## Exercício 0 — Lambda Sanctum

### Perguntas de reflexão

- O que é uma expressão lambda?
`lambda args: expressão`

- Diferença entre lambda e `def`?
lambda é anônima, de uma linha, sem `return` explícito

- Quando usar lambda?
transformações simples passadas como argumento (callbacks)

- Quando **não** usar lambda?
lógica complexa, reuso, legibilidade exige nome

- Como `map()`, `filter()` e `sorted()` aceitam funções como argumento?
Em Python funções são objetos de primeira classe — podem ser passadas como valores. Esses builtins recebem um parâmetro `key`/`function` e chamam internamente `f(item)` para cada elemento.

- Quando uma lambda se torna difícil de ler? Qual é o limite?
Quando tem lógica condicional, múltiplas operações ou precisa de nome para comunicar intenção. Limite prático: se não cabe confortavelmente em uma linha e precisa de explicação, use `def`.

- Por que `sorted()` retorna uma nova lista em vez de modificar a original?
Por design funcional — evita efeitos colaterais. A original pode ser uma tuple ou outro iterável imutável. Se quiser modificar in-place, use `lista.sort()`.

### Exemplos:
```python
# sorted com lambda
sorted(lista, key=lambda x: x['power'], reverse=True)

# filter com lambda
list(filter(lambda x: x['power'] >= 50, mages))

# map com lambda
list(map(lambda s: f"* {s} *", spells))
```
---

## Exercício 1 — Higher Realm

### Perguntas de reflexão

- Funções como valores: podem ser atribuídas a variáveis, passadas como argumentos, retornadas

- O que é uma higher-order function?
recebe ou retorna outra função

- Como retornar uma função dentro de outra (factory pattern)?
A função externa define e retorna uma função interna. Cada chamada cria uma nova função especializada:
```python
def multiplier(n):
    return lambda x: x * n

dobro = multiplier(2)
dobro(5)  # → 10
```

- QUal a diferença entre `Callable` de `typing` vs `collections.abc`?
São a mesma coisa em runtime. `typing.Callable` era o caminho antes do Python 3.9; a partir do 3.9, `collections.abc.Callable` é o preferido. `typing.Callable` vira um alias para o outro.

- O que `callable(obj)` faz?
verifica se um objeto pode ser chamado como função

- Por que importar `Callable` de `collections.abc` e não de `typing`?
`typing.Callable` está deprecated desde 3.9. `collections.abc.Callable` é a fonte canônica — `typing` só re-exportava.

- Qual a diferença entre `callable(f)` e checar `isinstance(f, Callable)`?
`callable(f)` verifica se o objeto tem `__call__` (mais direto, sem import). `isinstance(f, Callable)` é mais explícito para type checkers e funciona melhor com anotações de tipo.

---

## Exercício 2 — Memory Depths

- **Lexical scoping:** uma função enxerga as variáveis do escopo onde foi **definida**, não onde foi **chamada**

- **Closure:** função interna que captura variáveis do escopo externo e as mantém vivas após o retorno da função externa

- **`nonlocal`:** permite modificar uma variável do escopo externo (não global) dentro da função interna. Sem `nonlocal`, você só pode ler a variável, não reatribuí-la

### Perguntas de reflexão

- Por que `global` é proibido?
variáveis globais criam estado compartilhado invisível, dificultam testes e composição


- O que acontece com o estado de uma closure se você chamar a função externa novamente?
Cria um estado independente. Cada chamada da função externa gera uma nova closure com seu próprio conjunto de variáveis capturadas — não compartilham estado entre si.

- Por que mutar um dict dentro de uma closure não precisa de `nonlocal`?
`nonlocal` é necessário para reatribuir a variável (mudar a referência). Mutar um dict (`d['key'] = val`) não reatribui — a referência ao dict continua a mesma. Você está modificando o objeto, não a variável que aponta para ele.

---

## Exercício 3 — Ancient Library

- **`functools.reduce(func, iterable)`**: aplica `func` acumulativamente — `reduce(add, [1,2,3])` → `(1+2)+3 = 6`

- **`functools.partial(func, *args, **kwargs)`**: congela argumentos de uma função, criando uma versão especializada

- **`functools.lru_cache`**: decorator que memoriza resultados de chamadas anteriores, evitando recálculo. Exige que os argumentos sejam hasháveis

- **`functools.singledispatch`**: permite criar uma função com comportamentos diferentes por tipo do primeiro argumento (polimorfismo funcional)

- **Módulo `operator`**: versões funcionais dos operadores Python — `operator.add` equivale a `lambda x, y: x + y`, mas mais rápido e com nome claro

### Perguntas de reflexão

- Por que `lru_cache` exige argumentos hasháveis? O que acontece se você passar uma lista?
O cache usa os argumentos como chave de um dicionário interno. Dicionários exigem chaves hasháveis. Listas não são hasháveis → lança `TypeError` na chamada.

- Qual a diferença entre `functools.singledispatch` e uma cadeia de `isinstance`?
`singledispatch` é extensível sem modificar a função original — outros módulos podem registrar novos tipos com `@func.register`. Uma cadeia de `isinstance` é fechada e cresce no mesmo lugar, violando o princípio aberto/fechado.

---

## Exercício 4 — Master's Tower

- **Decorator:** função que recebe uma função, retorna uma função modificada. O `@` é açúcar sintático: `f = decorator(f)`

- **`functools.wraps`:** preserva `__name__`, `__doc__` e outros metadados da função original — sem isso, todos os seus decorators teriam o mesmo nome (`wrapper`)

- **Decorator factory (parametrizado):** quando o decorator recebe argumentos, há três níveis de aninhamento: `factory(arg) → decorator(func) → wrapper(*args, **kwargs)`

- **`@staticmethod`:** método que não recebe `self` nem `cls` — pertence à classe logicamente, mas não depende da instância ou da classe. Útil para validações e utilitários


### Perguntas de reflexão

- O que acontece com `func.__name__` se você não usar `functools.wraps`? Por que isso importa?
Todos os decorators mostram o nome da função interna (`wrapper`). Isso quebra debugging, logs e documentação automática — você perde a identidade da função original.

- Qual a diferença entre `@staticmethod` e `@classmethod`?
`@staticmethod` não recebe `self` nem `cls` — é uma função comum dentro da classe, sem acesso ao estado da instância ou da classe.
`@classmethod` recebe `cls` (a própria classe) — tem acesso à classe e pode criar instâncias alternativas (factory methods).
