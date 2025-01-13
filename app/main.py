import sys
import os
import subprocess

builtin_commands = ["exit", "echo", "type"]
PATH = os.environ.get("PATH")

def find_executable(query_command):
    paths = PATH.split(":")

    for path in paths:
        if os.path.isfile(f"{path}/{query_command}") and os.access(f"{path}/{query_command}", os.X_OK):
            return f"{path}/{query_command}"
        
    return ""

def handle_echo(tokens):
    sys.stdout.write(f"{" ".join(tokens[1:])}\n")

def handle_type(tokens):
    command_path = find_executable(tokens[1])

    if tokens[1] in builtin_commands:
        sys.stdout.write(f"{tokens[1]} is a shell builtin\n")

    elif command_path:
        sys.stdout.write(f"{tokens[1]} is {command_path}\n")
    
    else:
        sys.stdout.write(f"{tokens[1]}: not found\n")

def main():
    while True:
        #REPL: Read-Evaluate-Print Loop
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        tokens = command.split()
        
        command_name = tokens[0]

        if command_name == "exit":
            return tokens[1]
        
        elif command_name == "echo":
            handle_echo(tokens)

        elif command_name == "type":
            handle_type(tokens)
                
        else:
            executable = find_executable(tokens[0])

            if executable:
                subprocess.run(tokens)
            else:
                sys.stdout.write(f"{command_name}: command not found\n")

        sys.stdout.flush()
if __name__ == "__main__":
    main()
