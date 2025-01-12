import sys


def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")
        builtin_commands = ["exit", "echo", "type"]

        command = input()

        tokens = command.split()
        
        command_name = tokens[0]

        if command_name == "exit":
            return 0
        if command_name == "echo":
            sys.stdout.write(" ".join(tokens[1:]))
        if command_name == "type":
            if tokens[1] in builtin_commands:
                sys.stdout.write(f"{tokens[1]} is a shell builtin")
            else:
                sys.stdout.write(f"{tokens[1]}: not found")
        else:
            sys.stdout.write(f"{command_name}: command not found")
        sys.stdout.write('\n')

if __name__ == "__main__":
    main()
