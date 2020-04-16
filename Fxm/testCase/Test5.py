import logging
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value ： %s' %s)
    return 10 / n

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print('finally...')

class FooError(ValueError):

    pass


from functools import reduce

def str2num(s):
   try:
        return int(s)
   except ValueError as e:
        return eval(s)



def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main2():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main2()