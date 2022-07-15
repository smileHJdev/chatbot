# number = [1, 2, 3, 4, 5]
# for i in number:
#     print(i)


# numbers = range(1, 10)
# for i in numbers:
#     print(i)

# coord = [(0, 0), (10, 15), (20, 25)]
# for x, y in coord:
#     print(x, y)

# user = {'ame': 'Kei', 'age': 35, 'nationality': 'Korea'}
# print(user)
# for i in user.keys():
#     print(i)
# for i in user.values():
#     print(i)
# for k, v in user.items():
#     print(k, v)

class SimpleObj:
    def __init__(self):
        print('call __init__()')

    def __del__(self):
        print('call __del__()')


obj = SimpleObj()
print('obj instance alive...')
del obj
