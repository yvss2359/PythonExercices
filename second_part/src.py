import inspect
import random

def random_gen():
    while True:
        number = random.randint(10, 20)
        if number == 15:
            return None
        yield number


def decorator_to_str(func):
    def wapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wapper


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']


def ignore_exception(exception):
      def wrapper(func):
            def wrapped(*args,**kwargs):
                try:
                    return func(*args,**kwargs)
                except exception :
                    return None
            return wrapped
      return wrapper


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList(type):
    # todo exercise 5
    def __init__(cls, name, bases, attrs):
        bases = (list,) + bases
        super().__init__(name, bases, attrs)



class Ex:
    x = 4

class ForceToList(Ex, metaclass=MetaInherList):
    pass

"""
Metaclass that checks if classes have an attribute named 'process' which must be a method taking 3 arguments
"""
class ProcessChecker(type):
    def __init__(cls, name, bases, attrs):
        #Chechs if the class contains attribut 'process'
        if 'process' not in attrs:
            raise TypeError("ProcessChecker must have a 'process' method.")
        #Checks if 'process' is a method
        if not callable(attrs['process']):
            raise TypeError("The 'process' attribute must be a method.")
        #Checks if method takes 3 arguments
        if len(inspect.signature(attrs['process']).parameters) != 3:
            raise TypeError("The 'process' method must take 3 arguments.")
        super().__init__(name, bases, attrs)


class ProcessClass(metaclass=ProcessChecker):
    def process(self, arg1, arg2, arg3):
        pass

