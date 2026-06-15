import sys

# Ver los argumentos pasados al script
# print("Argumentos:", sys.argv)


def main():
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if len(sys.argv) >= 2:
        print("Arguments received:", len(sys.argv[1:]))
        count = 1
        for args in sys.argv[1:]:
            print(f"Argument {count}: {args}")
            count += 1
    else:
        print("No arguments provided!")
    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    main()
