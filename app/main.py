import sys


def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")

        command = input()

        tokens = command.split()
        
        command_name = tokens[0]

        if command_name == "exit":
            return 0
        if command_name == "echo":
            sys.stdout.write(" ".join(tokens[1:]))

        print(f"{command_name}: command not found")


if __name__ == "__main__":
    main()
