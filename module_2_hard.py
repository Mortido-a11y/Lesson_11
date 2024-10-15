import random
result = list()
def get_number():
    number = random.randint(3, 20)
    return number
c = get_number()
print(c)
for a in range(1, c):
    for b in range(1, c):
        if c % (a + b) == 0 and a < b:
            result.append(a)
            result.append(b)
print(result)
