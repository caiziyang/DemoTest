from enum import Enum,unique


class Student(object):
    pass

def set_age(self, age):
    self.age = age


s =Student()
s.name = 'Michel'
print(s.name)
from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

class Screen(object):
    width = 0
    height = 0
    @property
    def resolution(self):
        return self.width * self.height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

print(Chain().users.repos)

@unique
class Gender(Enum):
    Male = 0
    Female = 1
    Gender = Enum('Gender', ('Male', 'Female'))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)

print(Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')





