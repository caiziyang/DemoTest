import logging
import unittest

from Fxm.testCase.mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(cls):
        print("setup......")

    def tearDown(self) -> None:
        print('teardown......')
    # def test_init(self):
    #     d = Dict(a=1, b='test')
    #     self.assertEqual(d.a, 1)
    #     self.assertEqual(d.b, 'test')
    #     self.assertTrue(isinstance(d, dict))
    #     print('执行：%s', TestDict.test_init)
    #
    # def test_key(self):
    #     d = Dict()
    #     d['key'] = 'value'
    #     self.assertEqual(d.key, 'value')


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @property
    def get_grade(self):

        if 80 <= self.score <= 100:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade, 'A')
        self.assertEqual(s2.get_grade, 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade, 'B')
        self.assertEqual(s2.get_grade, 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade, 'C')
        self.assertEqual(s2.get_grade, 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(TypeError):
            s1.get_grade()
        with self.assertRaises(TypeError):
            s2.get_grade()


if __name__ == '__main__':
    unittest.main()










