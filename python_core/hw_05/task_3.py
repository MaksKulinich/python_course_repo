from pathlib import Path
from collections import Counter
import sys


# розбиття логів на окремі частини 
def parse_log_line(line : str) -> dict:
    date, time, log_level, *message = line.split()
    return {
        "date" : date,
        "time" : time,
        "log" : log_level,
        "message" : message
    }


# створення списку усіх логів за частинами
def load_logs(file_path: str) -> list:
    new_file_path = Path(file_path)
    try:
        with open(new_file_path, "r", encoding="utf-8") as log_file:
           line_list =  [parse_log_line(line) for line in log_file]
                
    except FileNotFoundError:
        print("File not found")
    return line_list


# створення списку усіх вказаних логів
def filter_logs_by_level(logs: list , level: str = None) -> list:
    logs_list = []
    if level:
        for sl in logs:
            if sl["log"].lower() == level.lower():
                log_message = ""
                for word in sl["message"]:
                    log_message += word + " "
                logs_list.append(f"{sl["date"]} {sl["time"]} - {log_message}")
        
    return logs_list


# підрахунок кількості логів кожного виду
def count_logs_by_level(logs: list) -> dict:
    if not logs:
        return {}
    list_logs_items = []
    for item in logs:
        list_logs_items.append(item["log"])
    # list_logs_items = [item['log'] for item in logs]
    
    return dict(Counter(list_logs_items))


# виведення інформації
def display_log_counts(counts: dict):
    print("Рівень логування    |     Кількість")
    for key, value in counts.items():
        print(f"{key.center(20)}| {str(value).center(20)}")

def display_log_filter(filter: list):
    for element in filter:
        print(element)

logs = load_logs(sys.argv[1])

filtered_logs = logs

log_counts = count_logs_by_level(filtered_logs)

display_log_counts(log_counts)

# перевірка чи існує другий аргумент і чи є він вірною назвою логу 
if len(sys.argv) > 2 and sys.argv[2].upper() in list(log_counts.keys()):
    print_level_log = filter_logs_by_level(logs, sys.argv[2])
    print(f"\nУсі логи для {sys.argv[2].upper()}:")
    display_log_filter(print_level_log)