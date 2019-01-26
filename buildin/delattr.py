class User:
    name = 'admin'
    pwd = '123'

    def __repr__(self):
        return 'repr, name:{},pwd:{}'.format(self.name, self.pwd)

    def __str__(self):
        return 'str, name:{},pwd:{}'.format(self.name, self.pwd)


u = User()
print(u)

delattr(User, 'name')

# print(u)
