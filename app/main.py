import sys


def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")

        command = input()
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
