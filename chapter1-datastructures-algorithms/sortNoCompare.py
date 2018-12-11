'''
  if the object's type is common, but they can not compare, if compare, FYI below
'''

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(12),User(3), User(36), User(18), User(45), User(25)]
    print(users)
    
    # way 1
    print(sorted(users, key=lambda u: u.user_id))

    # way 2
    print(sorted(users, key=attrgetter('user_id')))

sort_notcompare()
