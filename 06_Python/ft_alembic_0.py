# 'import elements' carrega o modulo inteiro no namespace com o nome 'elements'
# As funcoes sao acessadas como atributos do modulo: elements.create_fire()
import elements


print("=== Alembic 0 ===")
print("Using: 'import ...' structure to access elements.py")
print("Testing create_fire:", elements.create_fire())
