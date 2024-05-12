import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def get_files(directory):
    files_list = []
    for file_path in Path(directory).rglob("*"):
        if file_path.is_file():
            files_list.append(file_path)
    return files_list


def copy_files(src_dir, dst_dir):
    files = get_files(src_dir)
    with ThreadPoolExecutor() as executor:
        for file in files:
            executor.submit(copy_file, file, src_dir, dst_dir)


def copy_file(file, src_dir, dst_dir):
    rel_path = file.relative_to(src_dir)
    dst_subdir = Path(dst_dir) / rel_path.suffix[1:]
    dst_subdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(file, dst_subdir)


if __name__ == "__main__":
    src_directory = input("Введіть шлях до директорії з файлами для обробки: ")
    dst_directory = input("Введіть шлях до цільової директорії: ") or "dist"
    copy_files(src_directory, dst_directory)
