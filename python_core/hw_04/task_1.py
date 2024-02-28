def total_salary(path) -> tuple:
    try:
        with open(path, "r", encoding="utf-8") as file_about_workers:
            read_file_about_workers = file_about_workers.readlines()
    except FileNotFoundError:
        print("File is not found")
    
    general_salary = 0 

    for worker in read_file_about_workers:
        data_about_workers = worker.strip('\n').split(",")
        general_salary += int(data_about_workers[1])

    average_salary = general_salary / len(read_file_about_workers)
    
    # перевірка числа після коми, якщо 0 то виводимо як ціле число, інакше з округленням до 3 чисел
    if (average_salary%1) == 0:
        return general_salary, int(average_salary)
    else: 
        return  general_salary, average_salary.__round__(3)
    

