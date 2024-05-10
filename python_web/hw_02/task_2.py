import logging
from time import time, sleep


def factorize(list_number: list) -> list:
    del_list = []
    for item in list_number:
        for el in range(1, int(max(list_number) / 2)):
            if item % el == 0:
                del_list.append(el)

    return del_list


if __name__ == "__main__":
    rand_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    logging.INFO(f"Список дільників : {factorize(rand_list)}")
