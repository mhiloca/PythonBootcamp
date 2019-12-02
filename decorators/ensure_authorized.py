from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin':
        # if 'role' in kwargs.keys():
        #     if kwargs['role'] == 'admin':
            return "Shhh! Don't tell anyone!"
        return "Unauthorized"
    return wrapper

@ensure_authorized
def show_secrets(**kwargs):
    pass


print(show_secrets(role='nobody'))