'''
Agora você precisa tratar a parte de saída do pipeline.
Isso será feito usando um sistema de plugins para classes de
exportação, tornadas compatíveis com exportação por meio de
duck typing.

Implemente o seguinte:

• Uma nova classe ExportPlugin que herda da classe especial Protocol.

• Esta classe definirá o seguinte método, que atuará como restrição para cada
plugin de exportação:

def process_output(self, data: list[tuple[int, str]]) -> None:

O tipo do parâmetro data é uma lista de tuplas que corresponde ao valor de
retorno do método output da classe DataProcessor.

• A classe DataStream implementará o método :

def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:

a ser usado após chamar process_stream, que consumirá nb elementos de todos os
processadores registrados e os exportará usando o plugin compatível fornecido.

• Crie ao menos um plugin de exportação CSV e um plugin de exportação JSON.
Não é necessário usar uma importação específica para esses plugins
— crie manualmente strings CSV e JSON válidas.
'''


from abc import ABC, abstractmethod
from typing import Any, Protocol


# Classe feita no ex0, nao modificada
class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
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


# Classe feita no ex0, nao modificada
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


# Classe feita no ex0, nao modificada
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


# Nova classe: ExportPlugin herda da classe especial Protocol
# Protocol define tipagem estrutural (ou structural subtyping), permitindo
# estabelecer contratos de comportamento baseados nos métodos e atributos
# que um objeto possui, em vez de sua herança
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('CSV Output:')
        print(','.join(item[1] for item in data))


class JsonPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print('JSON Output:')
        out = ', '.join(f'"item_{item[0]}": "{item[1]}"' for item in data)
        print('{' + out + '}')


# Classe feita no ex1, novo metodo (output_pipeline)
class DataStream():
    def __init__(self):
        self._processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            registered = False
            for process in self._processors:
                if process.validate(item) is True:
                    process.ingest(item)
                    registered = True
                    break
            if not registered:
                print("DataStream error - Can't process element in stream:",
                      item)

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for process in self._processors:
            name = type(process).__name__.replace("Processor", " Processor")
            remaining = len(process._data)
            amount = len(process._data) + process._count
            print(f"{name}: total {amount} items processed,"
                  f" remaining {remaining} on processor")

    # Novo metodo: consume 'nb' elementos de todos os processadores
    # registrados e os exporta usando o plugin compatível fornecido em plugin
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        data_output = []
        for processor in self._processors:
            for _ in range(nb):
                if len(processor._data):
                    data_output.append(processor.output())
            plugin.process_output(data_output)
            data_output.clear()


def main():
    print("=== Code Nexus - Data Pipeline ===")
    print()

    print("Initialize Data Stream...")
    data_logs = DataStream()
    print()

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
    data2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    # Registrando Processadores
    print("Registering Processors")
    # Registrando o Processador Numérico
    data_logs.register_processor(NumericProcessor())
    # Registrando o Processador Texto
    data_logs.register_processor(TextProcessor())
    # Registrando o Processador Log
    data_logs.register_processor(LogProcessor())
    print()

    # Enviar o primeiro lote de dados em tempo real:
    print("Send first batch of data on stream:", data)
    data_logs.process_stream(data)
    print()

    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # Enviar os dados processados de cada processador para um plugin CSV:
    print("Send 3 processed data from each processor to a CSV plugin:")
    data_logs.output_pipeline(3, CsvPlugin())

    print()
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # Enviar outro lote de dados:
    print("Send another batch of data:", data2)
    data_logs.process_stream(data2)

    print()
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()

    # Enviar 5 conjuntos de dados processados ​​de cada
    # processador para um plugin JSON:
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_logs.output_pipeline(5, JsonPlugin())

    print()
    print("== DataStream statistics ==")
    data_logs.print_processors_stats()
    print()


if __name__ == "__main__":
    main()
