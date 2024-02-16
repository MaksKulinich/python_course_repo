import random as rd

def get_numbers_ticket(min : int, max : int, quantity : int) -> list:
    random_number_set = set()
    if min >= 1 and max <= 1000:
        while(len(random_number_set) < quantity):
            random_number_set.add(rd.randint(min, max))
    
    return sorted(list(random_number_set))

print(f"Random numbers : {get_numbers_ticket(1, 49, 7)}")