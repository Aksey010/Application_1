import math
import random

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt(a=random.randint(0,100)):
    assert math.sqrt(a**2) == a

def test_pow(b=random.randint(0,100),c=random.randint(0,100)):
    assert math.pow(b,c) == b**c

def test_hypot(x=random.randint(0,100),y=random.randint(0,100)):
    assert math.hypot(x,y) == math.sqrt(x**2 + y**2)

def test_filter(numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    filtered = []
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
    assert list(filter(lambda s: s % 2 == 0, numbers)) == filtered

def test_map(numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    mapped = []
    for number in numbers:
        mapped.append(number**2)
    assert list(map(lambda s: s**2, numbers)) == mapped

def test_sorted(strings = ['1', '6789', '23', '345']):
    strings_check = strings
    strings_check.sort(key=len)
    assert sorted(strings, key=len) == strings_check
