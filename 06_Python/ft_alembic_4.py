# 'import alchemy' carrega o pacote executando alchemy/__init__.py.
# Apenas o que estiver exportado no __init__ fica acessivel via alchemy.<nome>.
import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print("Testing create_air:", alchemy.create_air())

print("Now show that not all functions can be reached")

# create_earth nao foi exportado em alchemy/__init__.py.
# Mesmo existindo em alchemy/elements.py, o acesso via alchemy.create_earth()
# lanca AttributeError: module 'alchemy' has no attribute 'create_earth'
print("This will raise an exception!")

print(f"{alchemy.create_earth()}")  # type: ignore
