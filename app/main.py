import sys
import os

builtin_commands = ["exit", "echo", "type"]
PATH = os.environ.get("PATH")

def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        tokens = command.split()
        
        command_name = tokens[0]

        if command_name == "exit":
            return 0
        
        elif command_name == "echo":
            sys.stdout.write(" ".join(tokens[1:]))

        elif command_name == "type":
            query_command = tokens[1]
            paths = PATH.split(":")
            command_path = ""

            for path in paths:
                if os.path.isfile(f"{path}/{query_command}"):
                    command_path = path 
                    #We can not put a break here as it may be defined elsewhere too

            if query_command in builtin_commands:
                sys.stdout.write(f"{query_command} is a shell builtin")

            elif command_path:
                sys.stdout.write(f"{query_command} is {command_path}")
            
            else:
                sys.stdout.write(f"{query_command}: not found")

        else:
            sys.stdout.write(f"{command_name}: command not found")

        sys.stdout.write('\n')
        sys.stdout.flush()

if __name__ == "__main__":
    main()
