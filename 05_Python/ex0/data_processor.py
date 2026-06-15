# Authorized imports: abc and typing
# All standard classes and collections are authorized, along with their
# methods (int, str, list, dict, etc.).
# All built-in functions are authorized.

# Authorized: builtins, standard types, import typing, import abc


from abc import ABC, abstractmethod
from typing import Any


# essa classe tem apenas definicoes, entao todos que herdam DataProcessor,
# obrigatoriamente tem que ter essa estrutura
# ABC = Abstract Basic Class
class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        # deve verificar se os dados de entrada são adequados
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        # deve processar os dados de entrada
        pass

    def output(self) -> tuple[int, str]:
        # deve extrair o dado mais antigo e retornar
        if self._data:
            index = self._count
            self._count += 1
            return (index, self._data.pop(0))
        else:
            raise Exception("No data available")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for item in data:
                if type(item) not in (int, float):
                    return False
            return True
        if type(data) in (int, float):
            return True
        return False

    def ingest(self, data: int | float | list) -> None:
        if self.validate(data) is False:
            raise Exception("Improper numeric data")
        if type(data) is list:
            for value in data:
                self._data.append(str(value))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for item in data:
                if type(item) is not str:
                    return False
            return True
        if type(data) is str:
            return True
        return False

    def ingest(self, data: str | list) -> None:
        if self.validate(data) is False:
            raise Exception("Improper data")
        if type(data) is list:
            for value in data:
                self._data.append(str(value))
        else:
            self._data.append(str(data))


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for item in data:
                if type(item) is not dict:
                    return False
            return True
        if type(data) is dict:
            return True
        return False

    def ingest(self, data: dict | list) -> None:
        if self.validate(data) is False:
            raise Exception("Improper data")
        if type(data) is list:
            for value in data:
                self._data.append(f"{value['log_level']}: "
                                  f"{value['log_message']}")
        elif type(data) is dict:
            self._data.append(f"{data['log_level']}: {data['log_message']}")


def main():
    print("=== Code Nexus - Data Processor ===")
    print()

    #  Testando o Processador Numérico...
    print("Testing Numeric Processor...")

    proc_num = NumericProcessor()

    val_1 = proc_num.validate(42)
    # Tentando validar a entrada '42': Verdadeiro
    print(f"Trying to validate input '42': {val_1}")

    val_2 = proc_num.validate('Hello')
    # Tentando validar a entrada 'Olá': Falso
    print(f"Trying to validate input 'Hello': {val_2}")

    # Teste de ingestão inválida da string 'foo' sem validação prévia:
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        proc_num.ingest('foo')
    except Exception as err:
        # Exceção recebida: Dados numéricos incorretos
        print("Got exception:", err)

    data_list_num = [1, 2, 3, 4, 5]
    # Processando dados: [1, 2, 3, 4, 5]
    print(f"Processing data: {data_list_num}")
    proc_num.ingest(data_list_num)
    # Extraindo 3 valores...
    print("Extracting 3 values...")
    # Valor numérico count: data
    for _ in range(3):
        out_proc = proc_num.output()
        print(f"Numeric value {out_proc[0]}: {out_proc[1]}")

    print()

    # Testando o Processador de Texto...
    print("Testing Text Processor...")

    proc_text = TextProcessor()

    val_3 = proc_text.validate(42)
    # Tentando validar a entrada '42': Falso
    print(f"Trying to validate input '42': {val_3}")

    data_list_txt = ['Hello', 'Nexus', 'World']
    # Processando dados: ['Olá', 'Nexus', 'Mundo']
    print(f"Processing data: {data_list_txt}")
    proc_text.ingest(data_list_txt)

    # Extraindo 1 valor...
    print("Extracting 1 value...")
    out_txt = proc_text.output()
    # Valor de texto 0: Olá
    print(f"Text value {out_txt[0]}: {out_txt[1]}")

    print()

    # Testando o Processador de Log...
    print("Testing Log Processor...")

    proc_log = LogProcessor()
    val_4 = proc_log.validate('Hello')
    # Tentando validar a entrada 'Olá': Falso
    print(f"Trying to validate input 'Hello': {val_4}")

    data_list_dic = [
        {
            'log_level': 'NOTICE',
            'log_message': 'Connection to server'
        },
        {
            'log_level': 'ERROR',
            'log_message': 'Unauthorized access!!'
        }
        ]

    # Processando dados: [{'log_level': 'NOTICE', 'log_message': 'Conexão com
    # o servidor'}, {'log_level': 'ERROR'
    # ', 'log_message': 'Acesso não autorizado!!'}]

    print(f"Processing data: {data_list_dic}")
    proc_log.ingest(data_list_dic)
    # Extraindo 2 valores...
    print("Extracting 2 values...")
    for _ in range(2):
        out_log = proc_log.output()
        # Entrada de log 0: AVISO: Conexão com o servidor
        # Entrada de log 1: ERRO: Acesso não autorizado!!
        print(f"Log entry {out_log[0]}: {out_log[1]}")


if __name__ == "__main__":
    main()
