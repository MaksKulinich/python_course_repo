from colorama import init, Fore
from pathlib import Path
import sys


init()

def main(path):

    if path.exists():
        for item in path.iterdir():    
            if item.is_dir():
                path = path / f"{item}"
                print(f"{Fore.YELLOW}  [DIRECTORY] {Fore.RESET} {item.name}")
                main(path)
            elif item.is_file():
                print(f"{Fore.CYAN}  [FILE] {Fore.RESET} {item.name}")
    else:
        print("Not such file or directory")

user_input_path = Path(sys.argv[1])

if __name__ == "__main__":
    main(user_input_path)