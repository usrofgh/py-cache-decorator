def cache(func: callable) -> callable:
    calculated = {}

    def inner(*args) -> list:
        if args in calculated:
            print("Getting from cache")
            return calculated[args]

        res = func(*args)
        calculated[args] = res
        print("Calculating new result")
        return res
    return inner


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
