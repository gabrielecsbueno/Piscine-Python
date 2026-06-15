# Autorizados `pandas`, `requestss`, `matplotlib`, `numpy`, `sys`, `importlib`

''''
Modulo nativo : importlib
Sua principal função é permitir importações dinâmicas de módulos (ou seja,
importar bibliotecas usando strings em tempo de execução), recarregar módulos
já carregados e criar carregadores customizados
'''


from importlib import util, metadata
try:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
except ModuleNotFoundError:
    pass


def check_dependencies() -> bool:
    '''
    Essa funcao verifica se uma lista de dependencias estao instaladas.
    Se sim, imprime as informacoes das dependencias, e retorna True
    Se nao, imprime erro com uma instrucao de como instalar com pip,
    e retorna False
    '''
    def check_spec(name: str) -> str | None:
        '''
        Essa funcao verifica se a dependencia esta instalada atraves do modulo
        importlib.
        Se sim retorna a versao instalada, se nao retorna None
        - A funcao util.find_spec(), busca o módulo que deseja verificar e
        retorna suas especificações se ele estiver disponível, ou None caso
        não esteja instalado.
        '''
        check = util.find_spec(name)
        if check:
            return metadata.version(name)
        else:
            return None

    dependencies_list = [
        ('pandas', 'Data manipulation ready'),
        ('numpy', 'Numerical computation ready'),
        ('matplotlib', 'Visualization ready')
    ]

    for dependency, description in dependencies_list:
        version = check_spec(dependency)
        if not version:
            # 2. se alguma faltar - mostrar como instalar (pip e Poetry)
            print(f"[KO] {dependency} - {description}")
            print(f"Error: '{dependency}' not installed. Try installing with: "
                  f"'pip install {dependency}'")
            return False
        else:
            print(f"[OK] {dependency} ({version}) - {description}")
    return True


def show_pip_poetry() -> None:
    # Mostra a diferença entre pip e Poetry para gerenciar dependências
    # Nao tem demosntrado na saida, mas tem solicitano nos requisitos,
    # entao achei melhor colocar isso
    print("Package Manager Comparison:")
    print()
    print("pip (requirements.txt):")
    print(" Install:    pip install -r requirements.txt")
    print(" Manage:     versions defined manually, no automatic lock file")
    print()
    print("Poetry (pyproject.toml):")
    print(" Install:    poetry install")
    print(" Run:        poetry run python loading.py")
    print(" Manage:     generates poetry.lock automatically (exact versions)")
    print()
    print("Main difference:")
    print(" pip:    you control versions manually")
    print(" Poetry: generates a lock file, ensuring reproducibility")
    print()


def loading_data() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()

    # 1. devemos verificar quais dependências estão disponíveis
    print("Checking dependencies:")
    if not check_dependencies():
        print()
        print("To install with pip:     pip install -r requirements.txt")
        print("To install with Poetry:  poetry install")
        return
    print()

    # printa a comparacao entre pip e Poetry
    show_pip_poetry()

    # 3. se todas presentes - gerar dados com numpy
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    # numpy.linspace(inicio, fim, quantidade) - cria 1000 números igualmente
    # espaçados entre 0 e 10 (0.01, 0.02 ...), algo basico para representar
    # o eixo de tempo de leitura de dados
    timestamps = np.linspace(0, 10, 1000)

    # random.uniform(min, max, quantidade) - cria 1000 números aleatórios
    # simulando sinall de sinal e ruído da Matrix
    signal = np.random.uniform(0, 100, 1000)
    noise = np.random.uniform(0, 100, 1000)

    # pandas.DataFrame, to colocando como dicionario, aqui organiza os arrays
    # em uma tabela com colunas nomeadas cada chave do dicionário vira o
    # nome de uma coluna
    data_frame = pd.DataFrame({
        "timestamp": timestamps,
        "signal": signal,
        "noise": noise,
    })

    # 5. Gerar visualização com matplotlib - tem que salvar
    # como matrix_analysis.png
    print("Generating visualization...")
    print()

    # aqui cria uma figura (fig) e um eixo (axis)
    fig, axis = plt.subplots()
    # .plot(x, y)
    axis.plot(data_frame["timestamp"], data_frame["signal"])
    axis.set_title("Matrix Analysis")
    fig.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    # libera a memoria
    plt.close(fig)


if __name__ == "__main__":
    loading_data()
