from colorama import Back
from pathlib import Path
import sys

def log_file():
    print(f"{Back.BLUE} [FILE]  This a file")

def log_dir():
    print(f"{Back.YELLOW} [DIRECTORY] This a directory")


def proccesing_path(path):
    
    if path.exists():
        for item in path.iterdir():    
            if item.is_dir():
                new_path = path / f"{item}"
                log_dir()
                proccesing_path(new_path)
            elif item.is_file():
                log_file()
    else:
        print("Not such file or directory")

user_path = Path(sys.argv[1])

if __name__ == "__main__":
    proccesing_path(user_path)