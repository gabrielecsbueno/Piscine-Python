# PROJETO 09 - Cosmic Data: Pydantic Models & Validation


# 1. APRENDENDO PYDANTIC

## 1.1. O que e Pydantic

Pydantic e uma biblioteca Python para **validacao de dados em tempo de execucao** usando anotacoes de tipo. Quando voce cria uma instancia de um modelo Pydantic, ele automaticamente:

1. Valida os tipos dos dados passados
2. Converte tipos compativeis (ex: string `"2024-01-01"` vira `datetime`)
3. Lanca `ValidationError` com mensagens claras se algum dado for invalido

## 1.2. Como usar

### BaseModel

Herdar de `BaseModel` e o ponto de entrada. Todos os campos sao anotados como atributos da classe.

```python
from pydantic import BaseModel

class MeuModelo(BaseModel):
    campo_obrigatorio: str
    campo_opcional: str | None = None   # Optional com default None
    campo_com_padrao: bool = True
```

### Field - Restricoes de validacao

`Field(...)` permite adicionar restricoes alem do tipo:

```python
from pydantic import BaseModel, Field
from typing import Optional

class Exemplo(BaseModel):
    # Strings: min_length e max_length
    nome: str = Field(min_length=2, max_length=50)

    # Numeros: ge (>=), le (<=), gt (>), lt (<)
    idade: int = Field(ge=18, le=80)
    percentual: float = Field(ge=0.0, le=100.0)

    # Campo opcional com max
    notas: Optional[str] = Field(default=None, max_length=200)

    # Com valor padrao
    ativo: bool = Field(default=True)
```

Parametros mais usados no Field:
- `min_length` / `max_length` - para strings
- `ge` (greater or equal) / `le` (less or equal) - para numeros
- `gt` (greater than) / `lt` (less than) - para numeros (exclusivo)
- `default` - valor padrao


### Enum - Tipos enumerados

```python
from enum import Enum

class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"

# Uso no modelo
class AlienContact(BaseModel):
    contact_type: ContactType  # so aceita os valores definidos no Enum
```

Herdar de `str` alem de `Enum` facilita a serializacao e comparacao.


### @model_validator - Validacao personalizada

Usado para regras que dependem de **multiplos campos ao mesmo tempo**. Roda apos todos os campos terem sido validados individualmente.

```python
from pydantic import BaseModel, Field, model_validator

class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    ...

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        ...
        return self  # OBRIGATORIO retornar self
```

**Pontos importantes do @model_validator:**
- Sempre usar `mode='after'` (roda depois de validar os campos individualmente)
- Sempre retornar `self` no final
- Levantar `ValueError` (nao Exception) para erros de validacao


### Modelos Aninhados (Nested Models)

Pydantic valida modelos dentro de modelos automaticamente:

```python
from pydantic import BaseModel, Field
from typing import List

class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    ...

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    # Lista de modelos aninhados: min_length e max_length funcionam em listas tambem
    crew: List[CrewMember] = Field(min_length=1, max_length=12)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':
        # Acessar membros da lista
        ranks = [member.rank for member in self.crew]
        if Rank.captain not in ranks and Rank.commander not in ranks:
            raise ValueError('Mission must have at least one Commander or Captain')
        return self
```

Quando um `CrewMember` invalido e passado dentro de `SpaceMission`, Pydantic lanca um `ValidationError` apontando exatamente qual membro e qual campo falhou.

## Perguntas para responder :

### 1. Como funciona a conversao automatica de tipos do `Pydantic`?
Pydantic tenta converter o valor recebido para o tipo declarado no campo. Ex: campo int recebe "42" (string) → converte para 42 automaticamente. Se não conseguir converter, lança ValidationError.

### 2. O que acontece quando voce passa uma string `timestamp` para um campo `datetime`?
Pydantic parseia a string automaticamente usando o formato ISO 8601. Ex: "2024-01-15T10:30:00" vira um objeto datetime do Python. Strings em outros formatos podem falhar.


### 3. Como o Pydantic trata a validacao de modelos aninhados?
Valida recursivamente. Se um campo é do tipo OutroModel, o Pydantic valida os dados desse sub-modelo também. Um dicionário passado no lugar é convertido automaticamente para a instância do modelo aninhado.


### 4. O que acontece quando um CrewMember falha na validacao dentro de uma SpaceMission?
O erro é propagado para cima — o SpaceMission também falha, e o ValidationError mostra o caminho completo do erro, ex: crew[2].age → value is not a valid integer. Nenhum objeto parcial é criado.



# REFEREENCIAS

DOcumentacao do Pydantic[https://pydantic.dev/docs]