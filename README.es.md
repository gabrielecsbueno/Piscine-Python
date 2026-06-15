# Piscine Python

Repositorio de ejercicios de la Piscine Python — una serie de módulos progresivos que cubren desde los fundamentos del lenguaje hasta temas avanzados como la programación funcional y la validación de datos.

---

## Módulos

### 00 — Fundamentos (Growing Code)
Introducción al lenguaje: variables, tipos primitivos, condicionales, bucles, funciones iterativas y recursivas, y anotaciones de tipo básicas.

**Conceptos:** `print`, `input`, operadores aritméticos/lógicos, `if/else`, `for/while`, recursión, type hints.

---

### 01 — Programación Orientada a Objetos: Básico
Creación de clases con atributos y métodos, variables de clase vs. de instancia, encapsulamiento y cadenas formateadas.

**Conceptos:** `class`, `__init__`, atributos de instancia y de clase, métodos, f-strings, listas de objetos.

---

### 02 — Manejo de Excepciones
Uso de `try/except/else/finally`, lanzamiento de excepciones personalizadas y buenas prácticas para código robusto.

**Conceptos:** `try/except/else/finally`, `raise`, excepciones integradas (`ValueError`, `TypeError`), excepciones personalizadas.

---

### 03 — Argumentos y Colecciones
Lectura de argumentos de línea de comandos, manipulación de listas, diccionarios, tuplas y generadores.

**Conceptos:** `sys.argv`, `list`, `dict`, `tuple`, `set`, comprensiones de listas, expresiones generadoras.

---

### 04 — Manipulación de Archivos
Apertura, lectura, escritura y gestión de flujos de archivos; control de permisos y manejo de errores de E/S.

**Conceptos:** `open()`, modos de archivo (`r`, `w`, `a`), gestores de contexto (`with`), `sys.argv` para lectura de rutas.

---

### 05 — Clases Abstractas y Herencia
Definición de interfaces con `ABC`, implementación de métodos abstractos y polimorfismo mediante herencia concreta.

**Conceptos:** `ABC`, `@abstractmethod`, herencia, polimorfismo, módulo `typing`, colas con `list.pop(0)`.

---

### 06 — Módulos y Paquetes (Alchemy)
Organización del código en paquetes con `__init__.py`, distintas formas de importación y detección de dependencias circulares.

**Conceptos:** `import`, `from ... import`, `__init__.py`, espacios de nombres, dependencias circulares, `ImportError`.

---

### 07 — Patrones de Diseño (Battle)
Implementación de los patrones Abstract Factory, Mixin y Strategy en un sistema de batalla de criaturas con torneo.

**Conceptos:** Abstract Factory, herencia múltiple (Mixins), patrón Strategy, `@abstractmethod`, polimorfismo, manejo de excepciones en flujos de juego.

---

### 08 — Entornos Virtuales y APIs Externas
Creación y detección de entornos virtuales con `venv`, instalación de paquetes con `pip` y `poetry`.

**Conceptos:** `venv`, `sys.prefix` vs `sys.base_prefix`, `pip`, `requirements.txt`, `pyproject.toml`, variables de entorno (`.env`), `requests`.

---

### 09 — Validación de Datos con Pydantic
Modelado y validación de datos con Pydantic v2: modelos básicos, validadores personalizados y modelos anidados.

**Conceptos:** `BaseModel`, `Field`, `@model_validator`, `Enum`, modelos anidados, `ValidationError`, coerción de tipos automática.

---

### 10 — Programación Funcional (FuncMage)
Funciones como ciudadanos de primera clase: lambdas, funciones de orden superior, cierres, `functools` y decoradores.

**Conceptos:** `lambda`, `map/filter/sorted`, `Callable`, cierres (closures), `nonlocal`, `functools.reduce/partial/lru_cache/singledispatch`, decoradores, `functools.wraps`, `@staticmethod`.

---

## Cómo ejecutar

### Requisitos previos
- Python 3.10 o superior
- `flake8` y `mypy` para verificación de estilo y tipos (opcionales, pero recomendados)

```bash
pip install flake8 mypy
```

### Ejecutar un ejercicio
Cada ejercicio es un archivo Python independiente. Ejecútalo directamente:

```bash
python3 00_Python/ex2/ft_plot_area.py
python3 03_Python/ex0/ft_command_quest.py argumento1 argumento2
python3 04_Python/ex0/ft_ancient_text.py 04_Python/ex0/ancient_fragment.txt
```

### Usar el helper del módulo 00
El módulo 00 incluye un menú interactivo para probar los ejercicios:

```bash
cd 00_Python
python3 main.py
```

### Módulos con paquetes (06 y 07)
Los módulos con estructura de paquete deben ejecutarse desde la raíz del módulo:

```bash
cd 06_Python
python3 ft_alembic_0.py
python3 ft_transmutation_2.py

cd 07_Python
python3 battle.py
python3 tournament.py
```

### Módulo 08 — Entorno virtual
```bash
cd 08_Python/ex0
python3 construct.py              # fuera del venv
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py              # dentro del venv
deactivate
```

### Módulo 09 — Pydantic (requiere instalación)
```bash
cd 09_Python
python3 -m venv venv
source venv/bin/activate
pip install pydantic
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```
