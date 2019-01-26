"""
转成一个json字典
"""


class User:
    name = 'admin'
    pwd = '123'


u=User()
print(vars(u))
u.name='A'
u.pwd='1'
print(vars(u))
