import time
import functools


def backoff(logger, start_sleep_time=0.1, factor=2, border_sleep_time=10):
    def func_wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            n = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    logger.error(error)
                    if border_sleep_time > start_sleep_time * factor ** n:
                        time.sleep(start_sleep_time * factor ** n)
                    else:
                        time.sleep(border_sleep_time)
                    n += 1
                    raise error
        return inner
    return func_wrapper
