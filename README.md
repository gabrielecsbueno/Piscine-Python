# Piscine Python

Exercise repository for the Python Piscine — a series of progressive modules covering everything from language fundamentals to advanced topics such as functional programming and data validation.

---

## Modules

### 00 — Fundamentals (Growing Code)
Introduction to the language: variables, primitive types, conditionals, loops, iterative and recursive functions, and basic type hints.

**Concepts:** `print`, `input`, arithmetic/logical operators, `if/else`, `for/while`, recursion, type hints.

---

### 01 — Object-Oriented Programming: Basics
Creating classes with attributes and methods, class vs. instance variables, encapsulation, and formatted strings.

**Concepts:** `class`, `__init__`, instance and class attributes, methods, f-strings, lists of objects.

---

### 02 — Exception Handling
Using `try/except/else/finally`, raising custom exceptions, and best practices for robust code.

**Concepts:** `try/except/else/finally`, `raise`, built-in exceptions (`ValueError`, `TypeError`), custom exceptions.

---

### 03 — Arguments and Collections
Reading command-line arguments, manipulating lists, dictionaries, tuples, and generators.

**Concepts:** `sys.argv`, `list`, `dict`, `tuple`, `set`, list comprehensions, generator expressions.

---

### 04 — File Handling
Opening, reading, writing, and managing file streams; permission control and I/O error handling.

**Concepts:** `open()`, file modes (`r`, `w`, `a`), context managers (`with`), `sys.argv` for path reading.

---

### 05 — Abstract Classes and Inheritance
Defining interfaces with `ABC`, implementing abstract methods, and polymorphism through concrete inheritance.

**Concepts:** `ABC`, `@abstractmethod`, inheritance, polymorphism, `typing` module, queues with `list.pop(0)`.

---

### 06 — Modules and Packages (Alchemy)
Organising code into packages with `__init__.py`, different import styles, and detecting circular dependencies.

**Concepts:** `import`, `from ... import`, `__init__.py`, namespaces, circular dependencies, `ImportError`.

---

### 07 — Design Patterns (Battle)
Implementing Abstract Factory, Mixin, and Strategy patterns in a creature battle system with a tournament.

**Concepts:** Abstract Factory, Multiple Inheritance (Mixins), Strategy Pattern, `@abstractmethod`, polymorphism, exception handling in game flows.

---

### 08 — Virtual Environments and External APIs
Creating and detecting virtual environments with `venv`, installing packages with `pip` and `poetry`.

**Concepts:** `venv`, `sys.prefix` vs `sys.base_prefix`, `pip`, `requirements.txt`, `pyproject.toml`, environment variables (`.env`), `requests`.

---

### 09 — Data Validation with Pydantic
Modelling and validating data with Pydantic v2: basic models, custom validators, and nested models.

**Concepts:** `BaseModel`, `Field`, `@model_validator`, `Enum`, nested models, `ValidationError`, automatic type coercion.

---

### 10 — Functional Programming (FuncMage)
Functions as first-class citizens: lambdas, higher-order functions, closures, `functools`, and decorators.

**Concepts:** `lambda`, `map/filter/sorted`, `Callable`, closures, `nonlocal`, `functools.reduce/partial/lru_cache/singledispatch`, decorators, `functools.wraps`, `@staticmethod`.

---

## How to run

### Prerequisites
- Python 3.10 or higher
- `flake8` and `mypy` for style and type checking (optional but recommended)

```bash
pip install flake8 mypy
```

### Running an exercise
Each exercise is a standalone Python file. Run it directly:

```bash
python3 00_Python/ex2/ft_plot_area.py
python3 03_Python/ex0/ft_command_quest.py arg1 arg2
python3 04_Python/ex0/ft_ancient_text.py 04_Python/ex0/ancient_fragment.txt
```

### Using the module 00 helper
Module 00 includes an interactive menu to test the exercises:

```bash
cd 00_Python
python3 main.py
```

### Modules with packages (06 and 07)
Modules with a package structure must be run from the module root:

```bash
cd 06_Python
python3 ft_alembic_0.py
python3 ft_transmutation_2.py

cd 07_Python
python3 battle.py
python3 tournament.py
```

### Module 08 — Virtual environment
```bash
cd 08_Python/ex0
python3 construct.py              # outside the venv
python3 -m venv matrix_env
source matrix_env/bin/activate
python3 construct.py              # inside the venv
deactivate
```

### Module 09 — Pydantic (requires installation)
```bash
cd 09_Python
python3 -m venv venv
source venv/bin/activate
pip install pydantic
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```
