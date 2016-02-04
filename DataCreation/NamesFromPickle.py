import random, pickle


nameload = open('NameObjectPickle.txt', 'rb')
x = pickle.load(nameload)

y = random.choice(x)

print(x[0].f)
print(str(y.f) + ' ' + str(y.l))