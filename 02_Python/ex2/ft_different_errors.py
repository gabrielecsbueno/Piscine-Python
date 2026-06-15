def garden_operations(operation_number):
    if operation_number == 0:
        print(int("abc"))
        # raise ValueError
    elif operation_number == 1:
        print(10 / 0)
        # raise ZeroDivisorError
    elif operation_number == 2:
        open("/non/existent/file", "r")
        # raise FileNotFoundError
    elif operation_number == 3:
        print(f"{"hello" + 15}")
        # raise TypeError
    else:
        return operation_number


def test_error_types():
    print("=== Garden Error Types Demo ===")

    count = 0
    while count <= 4:
        try:
            print(f"Testing operation {count}...")
            garden_operations(count)
        except ValueError as err:
            print(f"Caught ValueError: {err}")
        except ZeroDivisionError as err:
            print(f"Caught ZeroDivisionError: {err}")
        except FileNotFoundError as err:
            print(f"Caught FileNotFoundError: {err}")
        except TypeError as err:
            print(f"Caught TypeError: {err}")
        else:
            print("Operation completed successfully")
        finally:
            count += 1
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
