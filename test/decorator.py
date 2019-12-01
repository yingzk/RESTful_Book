from functools import wraps


def logged():
    def decorator(f):
        print('logged')
        return f

    return decorator


def logged2(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        print('logged2')
        return f(*args, **kwargs)

    return decorator


@logged()
def hello(): print('hello')


@logged2
def hello2(): print('hello2')


if __name__ == '__main__':
    hello()
    print('-' * 20)
    hello2()
