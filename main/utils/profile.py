import time
from functools import wraps


def print_elapsed_time(elapsed_time):
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
    print(f'Time spent: {formatted_time}')


def profile(fn):
    @wraps(fn)
    def with_profiling(*args, **kwargs):
        start_time = time.time()
        ret = fn(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print_elapsed_time(elapsed_time)
        return ret, elapsed_time

    return with_profiling


def profile_async(fn):
    @wraps(fn)
    async def with_profiling(*args, **kwargs):
        start_time = time.time()
        ret = await fn(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print_elapsed_time(elapsed_time)
        return ret, elapsed_time

    return with_profiling
