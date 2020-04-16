import datetime
import functools
import time
from functools import reduce


def f(x):
    return x*x

def add(x, y):
    return x*10 + y


print(reduce(add, [1, 3, 5, 7, 9]))

L = [1, 3, 5, 7, 9]

print(list(map(f, L)))


def normalize(name: str):
    return name.title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    Mia = 1
    for i in range(len(L)):
        Mia *= L[i]

    return Mia

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x*10+y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, '13579'))

print(str2int(DIGITS))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'



def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divs(n):
    return lambda x: x % n > 0


def paimes():
    it = _odd_iter()
    yield 2
    while True:
        n = next(it)
        yield n
        it = filter(_not_divs(n), it)


for n in paimes():
    if n < 1000:
        print(n)
    else:
        break


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(info):

    return info[0]

def by_grade(info):

    return info[1]

L1 = sorted(L, key = by_name)

L2 = sorted(L, key = by_grade , reverse=True)

print(L1)

print(L2)

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))

print(L)
print(L2)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator




@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试cg')


