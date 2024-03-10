

def caching_fibonacci():
    fibonacci_dict_cache = {}

    def fibonacci(numb):        
        if numb in fibonacci_dict_cache:
            return fibonacci_dict_cache[numb]
        elif numb <= 0:
            return 0
        elif numb == 1:
            return 1

        
        fibonacci_dict_cache[numb] = fibonacci(numb - 1) + fibonacci(numb - 2)
        return fibonacci_dict_cache[numb]

    return fibonacci
