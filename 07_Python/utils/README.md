## INSTRUCOES DO PROJETO
- O projeto é escrito em `Python 3.10` ou superior;
- O projeto segue o padrao de codificacao `flake8`;
- Todo o codigo inclui anotacoes de tipo abrangentes. Verificados usando mypy;
- Todas as classes e colecoes padrao sao autorizadas, junto com seus metodos (`int`, `str`, `list`, `dict`, etc.);
- Todas as funcoes embutidas sao autorizadas, exceto `eval()` e `exec()`;
- As funcoes tratam excecoes adequadamente para evitar falhas;
- Bibliotecas externas sao proibidas;

Essa atividade requer dominio de heranca Python, classes abstratas, polimorfismo e imports.
Um arquivo `__init__.py` e OBRIGATORIO para cada pasta de exercicio.
Todo o codigo de teste esta na raiz do repositorio git.

## ESTRUTURA DO PROJETO

```bash
.
├── ex0/
│   ├── __init__.py
│   └── battle.py
├── ex1/
│   ├── __init__.py
│   └── capacitor.py
├── ex2/
│   ├── __init__.py
│   └── tournament.py
├── battle.py
```

## PROJETO

## Parte 1

### ex0/battle.py
Esse arquivo comeca o jogo com a criacao de cartas basicas de Criaturas (Creature).
As Criaturas sao classificadas em diversas familias e podem evoluir.
Esse arquivo foca no padrao de projeto fabrica abstrata.
Foi implemendo os seguintes elementos na pasta ex0/:

- A classe abstrata `Creature` possui atributos para o nome e o tipo da Criatura, um metodo abstrato `attack` e um metodo concreto generico `describe`.

    - O metodo `describe` que retorna a mensagem padrao (`{name_creature} is a {type_creature} type Creature`) usando o nome e o tipo da Criatura

    - O metodo `attack` retorna a mensagem de string (`{name_creature} uses {power_creature}!`)

- As seguintes classes concretas que herdam de Creature:
    - `Flameling`, `Pyrodon`, `Aquabub` e `Torragon`.

- A classe abstrata `CreatureFactory` permite criar a Criatura base e a Criatura evoluida para a mesma familia, usando os metodos abstratos `create_base` e `create_evolved`.

- As classes concretas `FlameFactory` e `AquaFactory`, herdando de `CreatureFactory`, tratam a criacao das Criaturas base e evoluida para cada familia (respectivamente `Flameling` e `Pyrodon` para `FlameFactory`, e `Aquabub` e `Torragon` para `AquaFactory`).

- O pacote `ex0/` e `ex1/` nao expoe Creature (Criaturas) concretas diretamente, expoe apenas as fabricas

## SCRIPT

### battle.py
Testa o pacote `ex0/battle.py`.
O seguinte cenario foi implementado:
- Instancia as fabricas de `Flameling` e `Aquabub`.
- Usa uma unica funcao que recebe um objeto de fabrica e verifica se pode criar a Criatura base e a evoluida, e entao se cada Criatura pode ser descrita e pode atacar.
- Outra funcao que recebe ambas as fabricas e faz as Criaturas base lutarem.
(pode usar Criaturas diferentes, mas deve manter os conceitos envolvidos (familias e fabricas abstratas))

```bash
$> python3 battle.py
Testing factory
Flameling is a Fire type Creature
Flameling uses Ember!
Pyrodon is a Fire/Flying type Creature
Pyrodon uses Flamethrower!

Testing factory
Aquabub is a Water type Creature
Aquabub uses Water Gun!
Torragon is a Water type Creature
Torragon uses Hydro Pump!

Testing battle
Flameling is a Fire type Creature
 vs.
Aquabub is a Water type Creature
 fight!
Flameling uses Ember!
Aquabub uses Water Gun!
```

## Parte 2

### ex1/capacitor.py
- `HealCapability` - classe abstrata independente (nao herda de `Creature`)
    - Contem o metodo abstrato `heal`, que pode receber um parametro `target` (opcional).
    - Retorna a string descrevendo a cura

- `TransformCapability` - classe abstrata independente (nao herda de `Creature`)
    - Define os metodos abstratos `transform` e `revert`
    - Um atributo de estado - a ideia e que a criatura "lembrar" se esta transformada ou nao
    - Impacta a implementacao do `attack` das `Creature`(Criaturas)

- `Sproutling` - herda de `Creature` e `HealCapability`

- `Bloomelle` - herda de `Creature` e `HealCapability`

- `Shiftling` - herda de `Creature` e `TransformCapability`
    - usa `attack()` antes de `transform()`
    - usa `attack()` depois de `revert()`

- `Morphagon` - herda de `Creature` e `TransformCapability`


obs: formam uma unica familia e estao disponiveis pela
- `HealingCreatureFactory` - herda de `CreatureFactory`
    - cria `Sproutling` e `Bloomelle`

- `TransformCreatureFactory` - herda de `CreatureFactory`
    - cria `Shiftling` e `Morphagon`


## SCRIPT

### capacitor.py

- Cria uma fabrica de Criaturas com cura

- Cria a Criatura base e depois a evoluida e faze-las:
    1) ser descritas;
    2) atacar;
    3) curar.

- Cria uma fabrica de Criaturas com transformacao.

- Cria a Criatura base e depois a evoluida e faze-las:
    1) ser descritas;
    2) atacar;
    3) transformar;
    4) atacar novamente;
    5) reverter.

```bash
$> python3 capacitor.py
Testing Creature with healing capability
 base:
Sproutling is a Grass type Creature
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount
 evolved:
Bloomelle is a Grass/Fairy type Creature
Bloomelle uses Petal Dance!
Bloomelle heals itself and others for a large amount

Testing Creature with transform capability
 base:
Shiftling is a Normal type Creature
Shiftling attacks normally.
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.

 evolved:
Morphagon is a Normal/Dragon type Creature
Morphagon attacks normally.
Morphagon morphs into a dragonic battle form!
Morphagon unleashes a devastating morph strike!
Morphagon stabilizes its form.
```

## Parte 3

Como acabamos de experimentar no exercicio anterior, Criaturas com capacidades diferentes agiram de forma diferente. No nosso caso, a familia de cura ira curar apos o attack, enquanto a familia de transformacao ira transform, depois attack, depois revert. No dia em que quisermos comprar multiplas cartas de Criaturas de diversas familias e faze-las lutar juntas em um torneio, precisamos de codigo de batalha que conheca cada capacidade. Ou talvez nao? Vamos explorar o padrao de estrategia abstrata! E sim, o dia do torneio chegou.

Na pasta/pacote ex2/, voce implementara o seguinte:

- A classe abstrata `BattleStrategy` define os metodos abstratos `act` e `is_valid`.
    - O metodo `is_valid` retorna um `bool` indicando que uma Criatura (`Creature`) é adequada para a estrategia
    - o metodo `act` é chamado pelo script do torneio (`tournament`)

Classes concretas (que herdam de `BattleStrategy`):

- `NormalStrategy` - herda de `BattleStrategy`
    - adequada para qualquer Criatura (`Creature`), que simplesmente usa o metodo `attack` durante o torneio.
- `AggressiveStrategy` - herda de `BattleStrategy`
    - adequada para Criatura (`Creature`) com capacidades de transformacao, que ira tranformar(`transform`), atacar (`attack`) e reverter (`revert`) durante o torneio.
- `DefensiveStrategy` - herda de `BattleStrategy`
    - adequada para Criatura (`Creature`) com capacidades de cura, que ira atacar (`attack`) e depois curar (`heal`) durante o torneio.


- Em caso de combinacao invalida `strategy-Creature`, o metodo `is_valid` retorna `False`. Se o metodo `act` for chamado com uma combinacao invalida, uma excecao (`exception`) dedicada e lancada com uma mensagem clara.

## SCRIPT

Finalmente podemos criar nosso torneio. O script tournament.py, localizado na raiz do repositorio Git, procedera da seguinte forma:

- Criar diversas fabricas de Criaturas (de ex0 e ex1).
- Criar as tres estrategias.
- Definir uma unica funcao `battle` que:
- Recebe uma lista de oponentes no torneio; cada oponente e definido como uma `tupla` composta por um `CreatureFactory` e um `BattleStrategy`.
- Faz cada oponente lutar uma vez contra todos os outros oponentes.
- Organiza cada luta usando a estrategia associada a cada Criatura.
- Trata corretamente tuplas invalidas de Criatura-estrategia.

```bash
$> python3 tournament.py
Tournament 0 (basic)
 [ (Flameling+Normal), (Healing+Defensive) ]
*** Tournament ***
2 opponents involved

* Battle *
Flameling is a Fire type Creature
vs.
Sproutling is a Grass type Creature
now fight!
Flameling uses Ember!
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount

Tournament 1 (error)
[ (Flameling+Aggressive), (Healing+Defensive) ]
*** Tournament ***
2 opponents involved

* Battle *
Flameling is a Fire type Creature
vs.
Sproutling is a Grass type Creature
now fight!
Battle error, aborting tournament: Invalid Creature 'Flameling' for this aggressive strategy

Tournament 2 (multiple)
[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
*** Tournament ***
3 opponents involved

* Battle *
Aquabub is a Water type Creature
vs.
Sproutling is a Grass type Creature
now fight!
Aquabub uses Water Gun!
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount

* Battle *
Aquabub is a Water type Creature
 vs.
Shiftling is a Normal type Creature
 now fight!
Aquabub uses Water Gun!
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.

* Battle *
Sproutling is a Grass type Creature
 vs.
Shiftling is a Normal type Creature
 now fight!
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.
```

## ex2

Resumo das Classes:

Ex0: battle

FlameFactory:
    Flameling (fire) - basic
    Pyrodon (fire/Flying) - evol
    --- pode: describe, attack
AquaFactory
    Aquabub (water) - basic
    Torragon (water) - evol
    --- pode: describe, attack

Ex1: capacitor

HealingCreatureFactory:
    Sproutling (Grass) - cura
    Bloomelle (Grass/Fairy) - cura evol
    --- pode : describe, attack, heal

TransformCreatureFactory:
    Shiftling (normal) - transform
    Morphagon (normal/Dragon) - transform evol
    --- pode : describe, attack, transform, revert

---

## Como pensar o tournament.py (da raiz)

Cada participante do torneio e uma CARTA com duas informacoes:
- De qual familia ele vem (a fabrica)
- Qual estilo de luta ele usa (a estrategia)

Entao cada participante e: (fabrica, estrategia)

### Fluxo da funcao battle

```
Entrada: [(FlameFactory, NormalStrategy), (HealFactory, DefensiveStrategy)]

Para cada participante:
    1. A fabrica CRIA a criatura  ->  creature = factory.create_base()
    2. A estrategia RECEBE essa criatura  ->  strategy = NormalStrategy(creature)

Para cada PAR de participantes (0 vs 1, 0 vs 2, 1 vs 2 ...):
    - imprime "* Battle *"
    - imprime describe() de cada criatura
    - imprime "vs." e "now fight!"
    - chama act() de cada estrategia
    - se der BattleException, imprime o erro e passa para o proximo par
```

### O que a lista de oponentes deve conter

A lista deve ser de tuplas (factory_instance, StrategyClass):
- factory_instance: objeto da fabrica ja instanciado, ex: FlameFactory()
- StrategyClass: a CLASSE da estrategia, nao instanciada ainda

A funcao battle instancia a estrategia internamente, depois de criar a criatura pela fabrica.

### Loop de pares (cada um luta contra todos os outros)

Com 3 oponentes [A, B, C], as batalhas sao: A x B, A x C, B x C.
Pensa em dois loops aninhados onde o segundo comeca sempre um passo a frente do primeiro.

### BattleException

Lancada dentro de act() quando is_valid() retorna False.
Deve incluir o nome da criatura na mensagem:
    "Invalid Creature 'Flameling' for this aggressive strategy"

O tournament.py captura essa excecao com try/except e imprime:
    "Battle error, aborting tournament: <mensagem da excecao>"
