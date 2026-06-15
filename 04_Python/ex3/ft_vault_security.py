'''
Resumo da missão: O arquivista-chefe percebeu o seu potencial e está promovendo
você para as operações de segurança do cofre.
É aqui que os verdadeiros arquivistas provam seu valor.

Este exercício requer o uso da instrução `with` (gerenciador de contexto) para
garantir o manuseio adequado dos arquivos.
A instrução `with` fecha automaticamente os arquivos mesmo que ocorram erros,
evitando vazamentos de recursos.

Crie uma função secure_archive() que :
- forneça acesso seguro a qualquer arquivo para leitura ou gravação.
- Ela retorna uma tupla (True|False, str) que indica se a operação foi
bem-sucedida (o booleano) e fornece o conteúdo associado (seja o conteúdo do
arquivo ou uma mensagem de erro).

A função recebe os seguintes parâmetros:
um nome de arquivo obrigatório, um int ou str opcional (à sua escolha) que
indica a ação a ser realizada (leitura ou gravação) e outra string opcional
que contém o conteúdo a ser gravado no arquivo.

Durante a defesa, a estrutura do código será analisada para verificar se atende
a esses requisitos.
'''


def secure_archive(name: str, action: str, text: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(name, "r") as file:
                return (True, file.read())
        elif action == "w":
            with open(name, "w") as file:
                file.write(text)
            with open(name, "r") as file:
                return (True, file.read())
        else:
            return (False, "Error")
    except Exception as err:
        return (False, f"{err}")


def main():
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "r"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w",
                         "Content successfully written to file"))


if __name__ == "__main__":
    main()
