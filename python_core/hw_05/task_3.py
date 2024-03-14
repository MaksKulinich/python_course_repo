from pathlib import Path


def parse_log_line(line : str) -> dict:
    date, time, log_level, *message = line.split()
    return {
        "date" : date,
        "time" : time,
        "log" : log_level,
        "message" : message
    }


def load_logs(file_path: str) -> list:
    new_file_path = Path(file_path)
    try:
        with open(new_file_path, "r", encoding="utf-8") as log_file:
           line_list =  [parse_log_line(line) for line in log_file]
                
    except FileNotFoundError:
        print("File not found")
    return line_list


def filter_logs_by_level(logs: list, level: str) -> list:
    pass


# for i in load_logs(r"C:\REPOSITORY\python_course_repo\python_core\hw_05\file.log"):
#     print(i)