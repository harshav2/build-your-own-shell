import sys


def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")

        command = input()

        tokens = command.split()
        
        if tokens[0]=="exit":
            return 0

        print(f"{tokens[0]}: command not found")


if __name__ == "__main__":
    main()
