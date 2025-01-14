import sys
import os
import subprocess

builtin_commands = ["exit", "echo", "type", "pwd", "cd", "cat"]
PATH = os.environ.get("PATH")

def find_executable(query_command):
    paths = PATH.split(":")

    for path in paths:
        if os.path.isfile(f"{path}/{query_command}") and os.access(f"{path}/{query_command}", os.X_OK):
            return f"{path}/{query_command}"
    return ""

def handle_cd(tokens):
    current_working_folder = os.getcwd()

    if tokens[1]=='~':
        os.chdir(os.environ.get("HOME"))

    elif tokens[1].startswith('.'):
        if len(tokens[1])>=2 and tokens[1][1]=='/':
            folders = tokens[1][2:].split('/')
        else:
            folders = tokens[1].split('/')

        for index in range(len(folders)):
            if folders[index]=='..':
                os.chdir(os.pardir)
            else:
                if os.path.isdir(f"{os.getcwd()}/{'/'.join(folders[index:])}"):
                    os.chdir(f"{os.getcwd()}/{'/'.join(folders[index:])}")
                else:
                    os.chdir(current_working_folder)
                    sys.stdout.write(f"cd: {tokens[1]}: No such file or directory\n")
                return

    else:
        path_folder = tokens[1]

        if os.path.isdir(path_folder):
            os.chdir(path_folder)
        else:
            os.chdir(current_working_folder)
            sys.stdout.write(f"cd: {tokens[1]}: No such file or directory\n")

def handle_single_ticks(command):
    start = command.find('\'')
    result = ""
    for index in range(start, len(command)):
        if command[index]!='\'':
            result += command[index]
    return result
        
def handle_echo(command):
    tokens = command.split()

    if tokens[1].startswith('\''):
        sys.stdout.write(f"{handle_single_ticks(command)}\n")

    else:            
        sys.stdout.write(f"{' '.join(tokens[1:])}\n")

def handle_cat(command):
    tokens  = command.split('\'')

    for filename in tokens[1:]:
        if not filename.strip() and os.path.isfile(filename):
            with open(filename) as file:
                sys.stdout.write(f"{file.read()}\n")

def handle_pwd():
    sys.stdout.write(f"{os.getcwd()}\n")

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

        command = input().strip()

        tokens = command.split()
        
        command_name = tokens[0]

        if command_name == "exit":
            break
        
        elif command_name == "echo":
            handle_echo(command)

        elif command_name == "type":
            handle_type(tokens)

        elif command_name == "pwd":
            handle_pwd()

        elif command_name == "cd":
            handle_cd(tokens)

        elif command_name == "cat":
            handle_cat(command)
                
        else:
            executable = find_executable(tokens[0])

            if executable:
                subprocess.run(tokens)
            else:
                sys.stdout.write(f"{command_name}: command not found\n")

        sys.stdout.flush()
if __name__ == "__main__":
    main()
