import functools


def safe_execute(fn):
    """Decorator that wraps function execution to suppress exceptions.
    
    If the decorated function raises any exception, returns None instead
    of propagating the error. Useful for fault-tolerant task execution.
    
    Args:
        fn: Callable to wrap with exception handling
        
    Returns:
        Wrapped function that returns None on exception
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return None
    return wrapper