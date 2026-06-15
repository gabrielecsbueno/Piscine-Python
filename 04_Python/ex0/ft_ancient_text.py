import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")

        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file = open(sys.argv[1], "r")
            # Retorna um TextIOWrapper[_WrappedBuffer]
            print("---\n")
            print(file.read())
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")

        except Exception as err:
            print(f"Error opening file '{sys.argv[1]}': {err}")


if __name__ == "__main__":
    main()
