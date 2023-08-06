from functools import wraps;

def faultHandler(func):
    """
        Handles functions with no return.
        Decorated function returns True if function executed successfully, False if something went wrong.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            func(*args, **kwargs);
            return True;

        except Exception as error_message:
            print("Something went wrong: {}".format(error_message));
            return False;

    return wrapper;

def faultReturnHandler(func):
    """
        Handles functions with return.
        Decorated function returns erro message if something went wrong.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs);

        except Exception as error_message:
            return "Fault: {}".format(error_message);

    return wrapper;