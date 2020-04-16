n = 123
f = 456.789

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = '''Hello,
Lisa!
'''


def trim(s):

    if s[0] == " ":
        return trim(s[1:])
    if s[-1] == " ":
        return trim(s[:-1])
    else:
        return s
s2 = "  Abc"
s3 = "   Abc   "
s4 = "    aaa  aa   a   "

s5 = " abcdefghijk "
print(trim(s4))
print(s5[:])

print(s5.strip(), '\n', s5[:3])
print(n, f, s2, s3, s4)
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print('%2d-%2d' % (311, 11))
print('%.2f' % 3.1415926)

def findMinAndMax(L):

    if not L:

        return None, None

    else:

        max_num = L[0]

        min_num = L[0]

        for i in L:

            if i > max_num:

                max_num = i

            if i < min_num:

                min_num = i

        return min_num, max_num


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 8,5]) == (1, 9):
    print(findMinAndMax([7, 1, 3, 9, 5]))
    print('测试失败!')
else:
    print('测试成功!')



L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


def normalize(name):
    str.title()

    return name.title()

# 测试:

L1 = ['adam', 'LISA', 'barT']

L2 = list(map(normalize, L1))
print(L2)

s2 = "aWEDFSEaaa"
print(s2.title())