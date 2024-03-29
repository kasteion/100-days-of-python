import time


def speed_calc_decorator(function):
    def speed_calc():
        start_time = time.time()
        function()
        run_time = time.time() - start_time
        print(f"{function.__name__} run speed: {run_time}s")

    return speed_calc


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
