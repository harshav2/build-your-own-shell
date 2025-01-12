import sys


def main():
    sys.stdout.write("$ ")

    inp = input()

    tokens = inp().split()

    valid_commands = []

    if tokens[0] not in valid_commands:
        sys.stdout.write(f"{tokens[0]}: command not found")


if __name__ == "__main__":
    main()
