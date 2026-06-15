# Autorizados: `os`, `sys`, `python-dotenv`, operações de arquivo
# pip install python-dotenv

# load_dotenv carrega o arquivo .env e transforma cada linha em variavel
# de ambiente, como se tivesse sido definida manualmente no terminal
from dotenv import load_dotenv  # type: ignore

# getenv le o valor de uma variavel de ambiente pelo nome
from os import getenv
from sys import stderr


def oracle() -> None:
    # load_dotenv() le o arquivo .env e carrega as variaveis no ambiente
    # importante: nao sobrescreve variaveis que ja existem no sistema
    # isso permite que variaveis definidas no terminal tenham prioridade
    load_dotenv()

    keys_env = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    # getenv retorna None se a variavel nao existir
    validation = [x for x in keys_env if not getenv(x)]

    if validation:
        for var in validation:
            stderr.write(f"Error: Required variable missing: {var}\n")
        return

    # todas as variaveis estao presentes, entao exibe a configuracao carregada
    print("Configuration loaded:")
    print("Mode:", getenv('MATRIX_MODE'))
    print("Database:", getenv('DATABASE_URL'))
    print("API Access:", getenv('API_KEY'))
    print("Log Level:", getenv('LOG_LEVEL'))
    print("Zion Network:", getenv('ZION_ENDPOINT'))
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()

    # le o modo atual para decidir o comportamento do programa
    # nao esta no exemplo de saida, mas diz que tem que fazer
    # norequisito do projeto
    mode = getenv('MATRIX_MODE')

    # development: ambiente local, logs detalhados, debug ativo
    if mode == "development":
        print("[DEV] Debug mode active - verbose logging enabled")
        print("[DEV] Using local database instance")
        print("[DEV] All config values visible for debugging")
    elif mode == "production":
        # production: ambiente remoto, logs minimos, dados sensiveis protegidos
        print("[PROD] Production mode - minimal logging active")
        print("[PROD] Remote database - secure connection required")
        print("[PROD] Use env vars directly, not .env files in production")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()


# ---------------------------------------------------------------------------
# CONCEITOS USADOS NESTE EXERCICIO
# ---------------------------------------------------------------------------
#
# VARIAVEL DE AMBIENTE
#   E um valor armazenado no sistema operacional, fora do codigo.
#   Qualquer programa rodando naquele ambiente pode le-la com os.getenv().
#   Usamos para guardar informacoes que mudam entre maquinas (senhas, URLs,
#   chaves de API) sem precisar alterar o codigo-fonte.
#   Exemplo no terminal:
#     export API_KEY=minha_chave
#     python3 oracle.py
#
# ARQUIVO .env
#   E um arquivo de texto simples com variaveis de ambiente no formato:
#     NOME=valor
#   A biblioteca python-dotenv le esse arquivo e carrega as variaveis
#   automaticamente com load_dotenv(). E uma convencao para facilitar o
#   desenvolvimento local sem precisar exportar cada variavel no terminal.
#   IMPORTANTE: o .env nunca deve ser commitado no repositorio — ele fica
#   no .gitignore porque pode conter senhas e chaves reais.
#   O .env.example e um modelo seguro (sem valores reais) que pode ser
#   commitado para que outros saibam quais variaveis precisam configurar.
#
# DEVELOPMENT vs PRODUCTION
#   Development (desenvolvimento): ambiente local do programador.
#     - Logs detalhados para facilitar o debug
#     - Banco de dados local
#     - Erros aparecem completos na tela
#   Production (producao): ambiente real, acessado pelos usuarios finais.
#     - Logs minimos para nao expor informacoes sensiveis
#     - Banco de dados remoto e seguro
#     - Erros sao registrados em logs, nao exibidos ao usuario
#   A variavel MATRIX_MODE controla qual comportamento o programa adota.
#
# PIP E POETRY NESTE PROJETO
#   pip: gerenciador de pacotes padrao do Python.
#     - As dependencias sao listadas em requirements.txt
#     - Instalacao: pip install -r requirements.txt
#   Poetry: gerenciador mais moderno, usado no ex1.
#     - As dependencias ficam em pyproject.toml
#     - Gera um arquivo poetry.lock com as versoes exatas de tudo
#     - Instalacao: poetry install
#   Neste exercicio (ex2) a unica dependencia externa e python-dotenv,
#   instalada com: pip install python-dotenv
# ---------------------------------------------------------------------------
