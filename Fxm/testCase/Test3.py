class Student(object):
    name1 = 'Student'
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


    def get_name(self):
        return self.name

    def print_score(self):
        print('%s' % (self.name))


class Animal(object):
    def run(self):
        print('Animal is running...')

    def run_twice(aa):
        aa.run()
        aa.run()
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
class Husky(Dog):
    def run(self):
        print('Husky is running...')

def run_twice(animal):
    animal.run()
    animal.run()



if __name__ == '__main__':
    a = Animal()
    d = Dog()
    c = Cat()
    b = Husky()
    z = Animal()
    print(isinstance(a, Animal))

    print(a.run_twice())
    print(d.run_twice())
    print(c.run_twice())
    print(run_twice(Animal()))
    print(dir(Animal))

    print(getattr(a, 'x', 404))
    setattr(a, 'x', 19)
    print(getattr(a, 'x', 404))
    print(hasattr(a, 'x'))



    if Student.count != 0:
        print('测试失败!1')
    else:
        bart = Student('Bart')
        if Student.count != 1:
            print('测试失败!2')
        else:
            lisa = Student('Bart')
            if Student.count != 2:
                print('测试失败!3')
            else:
                print('Students:', Student.count)
                print('测试通过!')
