import functools


def safe_execute(fn):
    """Decorator that catches exceptions and returns None on failure.
    
    Args:
        fn: The function to wrap with exception handling.
        
    Returns:
        A wrapped function that returns None if an exception occurs.
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception:
            return None
    return wrapper