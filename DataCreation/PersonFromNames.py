import random, string, names, pickle, time

# Initial values for semi-random portions
company = ['red car', 'blue wagon', 'orange', 'green engine']
domain = ['school.edu', 'business.com', 'organization.org', 'government.gov', 'network.net']
digits = '0123456789'

# Generate a random string of 'i' digits
def randomnum(i):
    return ''.join(random.choice(digits) for _ in range(i))

# Creates a Person object with first and last names, email address, company, and a random number
class Person:
    def __init__(self):
        # first name
        self.f = names.get_first_name()
        # last name
        self.l = names.get_last_name()
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

# Log the process start time and alert the user
starttime = time.time()
print('Creating people...')

# Loop to generate people and add them to the list
PersonList = []       
for i in range(50000):
    i = Person()
    PersonList.append(i)

# Alert the user that people creation finished and the process duration.    
print('People created. Time elapsed: ' + str(time.time() - starttime))

# Open a new binary file to store the people.
namedump = open('Soylent.green', 'wb')
pickle.dump(PersonList, namedump)

# Alert the user that the people are binned, and how long this process took.
print('Soylent.green is people. Total time elapsed: ' + str(time.time() - starttime))