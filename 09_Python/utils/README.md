# 2. INSTRUCOES GERAIS

## 2.1 Requisitos Python
- Deve ser escrito em `Python 3.10` ou superior
- Deve seguir o padrao de codificacao `flake8`
- Todo o codigo deve incluir anotacoes de tipo abrangentes. Verifique usando `mypy`.
- O tratamento de excecoes deve proteger os fluxos de dados de corrupcao.
- Todas as classes e colecoes padrao sao autorizadas, junto com seus metodos (`int`, `str`, `list`, `dict`, etc.).
- Todas as funcoes embutidas sao autorizadas.
- Use `pip` como gerenciador de pacotes.
- Voce deve usar Ambientes Virtuais (recomendado: `venv`, `virtualenv` ou `conda`).
- Voce deve usar `Pydantic 2.x` em todos os exercicios. (Deve ser instalado via `pip`). Apenas outros modulos serao listados na secao Autorizado de cada exercicio.


## 2.2. Estrutura do Projeto
- Cada exercicio deve ser concluido em seu proprio diretorio: ex0/, ex1/, ex2/
- Seu codigo deve demonstrar compreensao dos conceitos, nao apenas copiar e colar solucoes
- Todos os exercicios se baseiam uns nos outros; complete-os em ordem
- Documente seu processo de aprendizado por meio de comentarios claros no codigo e nomes de variaveis significativos


## 2.3. Ferramentas Disponiveis
Esta atividade inclui ferramentas de geracao de dados para ajudar voce a testar seus modelos `Pydantic` (`utils/data_generator/`):
- `data_generator.py` - Gera dados de teste realistas para todos os exercicios
- `data_exporter.py` - Exporta dados nos formatos JSON, CSV e Python
- `generated_data/` - Conjuntos de dados pre-gerados prontos para uso

***observacao***
1. Imports autorizados: pode importar dados JSON e CSV do diretorio tools. Modulos da biblioteca padrao (json, csv, datetime, etc.) sao permitidos.
2. Importante: Esta atividade foca na sintaxe do Pydantic v2. Evite decoradores depreciados como @validator - use @model_validator para validacao personalizada.


## 2.4. Conceitos Chave do Pydantic

### BaseModel
A base de todos os modelos `Pydantic`. Herde de `BaseModel` para criar classes de dados validadas.

### Field
Use `Field(...)` para adicionar restricoes de validacao, descricoes e valores padrao aos atributos do modelo.

### model_validator
Use o decorador `@model_validator(mode='after')` para logica de validacao personalizada que e executada apos a validacao embutida do `Pydantic`. Isso substitui o decorador `@validator` depreciado do `Pydantic v1`.


## 2.5. ARQUIVOS

```
09_Python
├── ex0/
│   └── space_station.py
├── ex1/
│   └── alien_contact.py
└── ex2/
    └── space_crew.py
```


---


# 3. Exercicio 0: Dados da Estacao Espacial

- Arquivo: `ex0/space_station.py`
- Funcoes autorizadas: Nenhum
- Projeto: criar um sistema de validacao para esses dados criticos

***observacao***
Objetivo: Aprender a criacao basica de modelos Pydantic com BaseModel e validacao com Field.

## Contexto
O Observatorio de Dados Cosmicos monitora centenas de estacoes espaciais pela galaxia. Cada estacao reporta estatisticas vitais incluindo tamanho da tripulacao, niveis de energia e status operacional.

## Modelo SpaceStation
Criar um modelo Pydantic com estes campos validados:

- `station_id`: String, 3-10 caracteres
- `name`: String, 1-50 caracteres
- `crew_size`: Inteiro, 1-20 pessoas
- `power_level`: Float, 0.0-100.0 por cento
- `oxygen_level`: Float, 0.0-100.0 por cento
- `last_maintenance`: Campo DateTime
- `is_operational`: Booleano, padrao True
- `notes`: String opcional, max 200 caracteres

## Funcao de Demonstracao
Inclua uma funcao `main()` que:

- Crie uma instancia valida de estacao espacial
- Exiba as informacoes da estacao claramente
- Tente criar uma estacao invalida (ex.: `crew_size > 20`)
- Mostre a mensagem de erro de validacao


### Saida esperada

```bash
Space Station Data Validation
========================================
Valid station created:
ID: ISS001
Name: International Space Station
Crew: 6 people
Power: 85.5%
Oxygen: 92.3%
Status: Operational
========================================
Expected validation error:
Input should be less than or equal to 20
```


## Perguntas para refletir:
1. Como funciona a conversao automatica de tipos do `Pydantic`?
2. O que acontece quando voce passa uma string `timestamp` para um campo `datetime`?


---


# 4. Exercicio 1: Logs de Contato Alien

- Arquivo: `ex1/alien_contact.py`
- Funcoes autorizadas: Nenhum
- Projeto: receber relatorios de contato alien de toda a galaxia

***observacao***
Objetivo: Dominar a validacao personalizada usando `@model_validator` para regras de negocio complexas.

## Contexto
O Observatorio recebe relatorios de contato alien de toda a galaxia. Esses relatorios sensiveis requerem regras de validacao sofisticadas que vao alem de simples restricoes de campos. Diferentes tipos de contato tem diferentes requisitos, e certas combinacoes de dados indicam relatorios potencialmente fraudulentos.


## `Enum` ContactType
Defina os tipos de contato: `radio`, `visual`, `physical`, `telepathic`


## Modelo `AlienContact`
Crie um modelo `Pydantic` com estes campos:
- `contact_id`: String, 5-15 caracteres
- `timestamp`: DateTime do contato
- `location`: String, 3-100 caracteres
- `contact_type`: Enum ContactType
- `signal_strength`: Float, escala 0.0-10.0
- `duration_minutes`: Inteiro, 1-1440 (max 24 horas)
- `witness_count`: Inteiro, 1-100 pessoas
- `message_received`: String opcional, max 500 caracteres
- `is_verified`: Booleano, padrao False


## Regras de Validacao Personalizada
Implemente `@model_validator(mode='after')` com estas regras de negocio:
- O `ID` de contato deve comecar com `"AC"` (Alien Contact)
- Relatorios de contato fisico devem ser verificados
- Contato telepatico requer pelo menos 3 testemunhas
- Sinais fortes (> 7.0) devem incluir mensagens recebidas

## Funcao de Demonstracao
Inclua uma funcao `main()` que mostre relatorios de contato validos e invalidos com mensagens de erro claras.

### Saida esperada

```
Alien Contact Log Validation
======================================
Valid contact report:
ID: AC_2024_001
Type: radio
Location: Area 51, Nevada
Signal: 8.5/10
Duration: 45 minutes
Witnesses: 5
Message: 'Greetings from Zeta Reticuli'
======================================
Expected validation error:
Telepathic contact requires at least 3 witnesses
```


*** Dica Avancada ***
O decorador @model_validator permite validar o modelo inteiro apos todos os campos terem sido validados. Lembre-se de retornar self ao final da funcao validadora.


---


# 5. Exercicio 2: Gestao de Tripulacao

- Arquivo: `ex2/space_crew.py`
- Funcoes autorizadas: Nenhum
- Projeto: gerenciamento cuidadoso da tripulacao

***observacao***
Objetivo: Dominar modelos Pydantic aninhados e relacionamentos complexos de dados.

## Contexto
Missoes espaciais requerem gerenciamento cuidadoso da tripulacao. Cada missao tem multiplos membros com diferentes patentes, especializacoes e niveis de experiencia. O Observatorio precisa validar que as tripulacoes atendem aos requisitos de seguranca e operacionais antes da aprovacao de lancamento.


## Enum Rank

Defina as patentes da tripulacao: cadet, officer, lieutenant, captain, commander


## Modelo CrewMember

Membro individual da tripulacao com estes campos:
- member_id: String, 3-10 caracteres
- name: String, 2-50 caracteres
- rank: Enum Rank
- age: Inteiro, 18-80 anos
- specialization: String, 3-30 caracteres
- years_experience: Inteiro, 0-50 anos
- is_active: Booleano, padrao True


## Modelo SpaceMission

Missao com lista de tripulacao e estes campos:
- mission_id: String, 5-15 caracteres
- mission_name: String, 3-100 caracteres
- destination: String, 3-50 caracteres
- launch_date: DateTime
- duration_days: Inteiro, 1-3650 dias (max 10 anos)
- crew: Lista de CrewMember, 1-12 membros
- mission_status: String, padrao "planned"
- budget_millions: Float, 1.0-10000.0 milhoes de dolares


## Regras de Validacao da Missao

Implemente @model_validator(mode='after') com estes requisitos de seguranca:
- O ID da missao deve comecar com "M"
- Deve ter pelo menos um Comandante ou Capitao
- Missoes longas (> 365 dias) precisam de 50% de tripulacao experiente (5+ anos)
- Todos os membros da tripulacao devem estar ativos

## Funcao de Demonstracao
Mostre uma missao valida com detalhes da tripulacao e uma missao invalida que falha na validacao.


### Saida esperada

```
Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: M2024_MARS
Destination: Mars
Duration: 900 days
Budget: $2500.0M
Crew size: 3
Crew members:
- Sarah Connor (commander) - Mission Command
- John Smith (lieutenant) - Navigation
- Alice Johnson (officer) - Engineering
=========================================
Expected validation error:
Mission must have at least one Commander or Captain
```


## Perguntas para refletir:
1. Como o Pydantic trata a validacao de modelos aninhados?
2. O que acontece quando um CrewMember falha na validacao dentro de uma SpaceMission?


---


# 6. ENTREGA E REVISAO

- Submeter no repositorio Git da atividade
- Apenas os arquivos solicitados pelo subject serao avaliados:
  - `ex0/space_station.py`
  - `ex1/alien_contact.py`
  - `ex2/space_crew.py`
- Nao incluir o venv ou arquivos gerados pelo data_generator na entrega
- Verificar nomes dos arquivos antes de submeter

---

# REFEREENCIAS

DOcumentacao do Pydantic[https://pydantic.dev/docs]