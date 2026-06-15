import sys
import site
import os


def main() -> None:
    # sys.prefix → caminho do Python em uso
    # sys.base_prefix → caminho do Python original (sem venv)
    # Se forem diferentes, está dentro de um venv
    if sys.prefix != sys.base_prefix:
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()
        # caminho completo do python em uso
        print("Current Python:", sys.executable)
        # Detectar o nome do ambiente. None se não estiver em venv
        v_path = os.environ.get("VIRTUAL_ENV")
        v_name = os.path.basename(v_path) if v_path else 'None detected'
        print("Virtual Environment:", v_name)
        print("Environment Path:", v_path)
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        package_path = site.getsitepackages()
        print(package_path[0])

    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()
        # caminho completo do python em uso
        print("Current Python:", sys.executable)
        # Detectar o nome do ambiente. None detected se não estiver em venv
        v_path = os.environ.get("VIRTUAL_ENV")
        v_name = os.path.basename(v_path) if v_path else 'None detected'
        print("Virtual Environment:", v_name)
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        # '-m' é para chamar um modulo do python que se chama 'venv'
        print("python -m venv matrix_env")
        # para esse nosso caso, no mac:
        # python3.10 -m venv matrix_env_pip
        # python3.10 -m venv matrix_env_poetry
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
