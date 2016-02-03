import random, string

company = ['red car', 'blue wagon', 'orange', 'green engine']
domain = ['school.edu', 'business.com', 'organization.org', 'government.gov', 'network.net']
letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def randomstr(i):
    return ''.join(random.choice(letters) for _ in range(i))
    
def randomnum(i):
    return ''.join(random.choice(digits) for _ in range(i))

class Person:
    def __init__(self):
        # first name
        self.f = randomstr(random.randrange(3,10)).capitalize()
        # last name
        self.l = randomstr(random.randrange(3,10)).capitalize()
        # email address
        if len(self.l) <= 6:
            trunclast = self.l
        else:
            trunclast = self.l[0:6]
        self.a = (self.f[0] + trunclast + '@' + random.choice(domain)).lower()
        # company name
        self.c = string.capwords(random.choice(company))
        # random number
        self.n = randomnum(random.randrange(4,8))

PersonList = []       
for i in range(20):
    i = Person()
    PersonList.append(i)


x = random.choice(PersonList)


"""
print(x.f)
"""


for i in PersonList:
    print('===================================')
    print('First Name is: ' + i.f)
    print('Last Name is: ' + i.l)
    print('Email Address is: ' + i.a)
    print('Company is: ' + i.c)
    print('Number is: ' + i.n)
    print('===================================')
