# Authorized: import sys, sys.argv, len(), open(),
#             import typing, typing.IO,
#             io.read(), io.write(), io.close(), print(), input()
'''
Ao final do script, aprimore o código para:
• Adicionar um caractere especial de arquivamento (o caractere #) ao final de
    cada linha (por exemplo, para ser compatível com o Windows 2087)
• Exibir o novo conteúdo
• Solicitar ao usuário o nome do file para salvar ou deixar o campo em
    branco para evitar salvar qualquer coisa
• Salvar o novo conteúdo se um nome de arquivo for fornecido e exibir uma
    nova mensagem final

Criar o arquivo ou substituí-lo se ele já existir

'''

import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")

        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(sys.argv[1], "r")
            # Retorna um TextIOWrapper[_WrappedBuffer]
            print("---\n")
            text = file.read()
            print(text)
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")

            print()
            print("Transform data:\n---\n")

            # o .replace é um metodo assiciado (funções que "pertencem" a um
            # tipo e são chamadas com . (ponto)) do tipo str
            # isso é autorizado no subject
            new_text = text.replace("\n", "#\n")

            print(new_text)

            name = input("Enter new file name (or empty):")

            if not name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{name}'")
                new_file = open(name, "w")
                new_file.write(new_text)
                print(f"Data saved in file '{name}'.")
                new_file.close()

        except Exception as err:
            print(f"Error opening file '{sys.argv[1]}': {err}")


if __name__ == "__main__":
    main()
