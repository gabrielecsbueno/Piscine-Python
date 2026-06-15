# Authorized: builtins, standard types, import typing, import abc


from abc import ABC, abstractmethod
import typing


# Classe feita no ex0, nao modificada
class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._count = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self._data:
            index = self._count
            self._count += 1
            return (index, self._data.pop(0))
        else:
            raise Exception("No data available")


# Classe feita no ex0, nao modificada
class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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


# Classe feita no ex0, nao modificada
class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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


# Classe feita no ex0, nao modificada
class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
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


# Classe nova: recebe um fluxo de dados contendo diferentes tipos e encaminha
#              cada elemento ao processador de dados apropriado usando
#              comportamento polimórfico
class DataStream():
    def __init__(self):
        self._processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        # para cada elemento no stream
        for item in stream:
            # comeco com meu item nao registrado
            registered = False
            # para cada processador registrado
            for process in self._processors:
                # se o item for igual ao processo
                # → guarda no processador, muda o registro e para
                if process.validate(item) is True:
                    process.ingest(item)
                    registered = True
                    break
            # se nenhum processador aceitou → imprime erro
            if not registered:
                print("DataStream error - Can't process element in stream:",
                      item)

    def print_processors_stats(self) -> None:
        # imprime estatísticas do fluxo
        if not self._processors:
            print("No processor found, no data")
            return
        for process in self._processors:
            # "NumericProcessor" → "Numeric Processor"
            name = type(process).__name__.replace("Processor", " Processor")
            remaining = len(process._data)
            amount = len(process._data) + process._count
            # Processador Numérico: total de {value} itens processados,
            # {value} restantes no processador
            print(f"{name}: total {amount} items processed,"
                  f" remaining {remaining} on processor")


def main():
    print("=== Code Nexus - Data Stream ===")
    print()

    # Inicializando o Fluxo de Dados...
    print("Initialize Data Stream...")
    data_logs = DataStream()

    # Imprimindo as Estatisticas
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # A informacao que precisa ser registrada
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    # Registrando o Processador Numérico
    print("Registering Numeric Processor")
    data_logs.register_processor(NumericProcessor())
    print()

    # Enviando o primeiro lote de dados no fluxo
    print(f"Send first batch of data on stream: {data}")
    data_logs.process_stream(data)

    # Imprimindo as Estatisticas
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # Registrando outros processadores de dados
    print("Registering other data processors")

    # Registrando o Processador Texto
    data_logs.register_processor(TextProcessor())
    # Registrando o Processador Log
    data_logs.register_processor(LogProcessor())

    # Enviando o mesmo lote novamente
    print("Send the same batch again")
    data_logs.process_stream(data)

    # Imprimindo as Estatisticas
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # Consumindo alguns elementos dos processadores de dados:
    # Numérico 3, Texto 2, Log 1
    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for processor in data_logs._processors:
        processor_name = type(processor).__name__
        if processor_name == 'NumericProcessor':
            for _ in range(3):
                processor.output()
        elif processor_name == 'TextProcessor':
            for _ in range(2):
                processor.output()
        else:
            processor.output()
    # Imprimindo as Estatisticas
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()


if __name__ == "__main__":
    main()
