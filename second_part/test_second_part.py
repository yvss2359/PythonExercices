import pytest
import unittest

from second_part.src import div, raise_something, add, ForceToList, random_gen, get_info, CacheDecorator





def test_generator():
    g = random_gen()
    assert isinstance(g, type((x for x in [])))
    a = next(g)
    while a != 15:
        assert 10 <= a <= 20
        a = next(g)
    with pytest.raises(StopIteration):
        next(g)


def test_to_str():
    assert add(5, 30) == '35'
    assert get_info({'info': [1, 2, 3]}) == '[1, 2, 3]'


def test_ignore_exception():
    assert div(10, 2) == 5
    assert div(10, 0) is None
    assert raise_something(TypeError) is None
    with pytest.raises(NotImplementedError):
        raise_something(NotImplementedError)


def test_meta_list():
    test = ForceToList([1, 2])
    assert test[1] == 2
    assert test.x == 4


class TestCacheDecorator(unittest.TestCase):

    def test_caching(self):

        cache_decorator = CacheDecorator()
        @cache_decorator
        def exponent(x):
            return x ** 2

        result1 = exponent(2)
        result2 = exponent(3)
        self.assertNotEqual(result1, result2)
        self.assertEqual(result1, cache_decorator.cache[2])
        self.assertEqual(result2, cache_decorator.cache[3])

    def test_caching_with_kwargs(self):

        cache_decorator = CacheDecorator()

        @cache_decorator
        def exponent(x, y):
            return x ** y

        result1 = exponent(2, y=3)
        self.assertEqual(result1, cache_decorator.cache[2])
        result2 = exponent(2, y=5)
        self.assertNotEqual(result1, result2)
        self.assertEqual(result2, cache_decorator.cache[2])


if __name__ == '__main__':
    unittest.main()

