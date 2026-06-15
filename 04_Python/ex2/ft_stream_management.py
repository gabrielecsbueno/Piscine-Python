'''
Use o código criado para o exercício anterior. Atualize-o para:
• Imprimir mensagens de erro resultantes de exceções no fluxo de saída de
erros, em vez de na saída padrão, com um prefixo claro (veja o exemplo)
• Obter entradas do usuário sem usar a função embutida input().

 ============================================================
 Os tres fluxos padrao sao objetos de arquivo abertos automaticamente:

 sys.stdin   -> entrada padrao (normalmente o teclado)
 sys.stdout  -> saida padrao  (normalmente o terminal)
 sys.stderr  -> saida de erros (aparece no terminal, mas separado do stdout)

 print() usa sys.stdout por padrao.
 Para escrever no stderr (erros, logs de debug):
   print("mensagem de erro", file=sys.stderr)
   sys.stderr.write("erro\n")  -> sem o \n nao pula linha

 Util para separar saida normal de mensagens de erro
 quando o usuario redireciona stdout para arquivo:
   python script.py > saida.txt  2> erros.txt
 ============================================================
'''
import sys


def main():
    if len(sys.argv) != 2:
        # saida de erros (aparece no terminal, mas separado do stdout)
        sys.stderr.write(f"Usage: {sys.argv[0]} <file>\n")
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

            new_text = text.replace("\n", "#\n")

            print(new_text)
            print("---\nEnter new file name (or empty): ", end="")
            # entrada padrao (normalmente o teclado), utilizado como imput
            name = sys.stdin.readline().rstrip("\n")

            if not name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{name}'")

                try:
                    new_file = open(name, "w")
                    new_file.write(new_text)
                    print(f"Data saved in file '{name}'.")
                    new_file.close()

                except PermissionError as err:
                    sys.stderr.write("[STDERR] Error opening file"
                                     f" '{name}': {err}\n")
                    print("Data not saved.")

        except Exception as err:
            sys.stderr.write("[STDERR] Error opening file"
                             f" '{sys.argv[1]}': {err}")


if __name__ == "__main__":
    main()
