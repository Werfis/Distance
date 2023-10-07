import random
def char_from_int(n):
return unichr(n)
random_string = "".join([char_from_int(random.randint(0, 0x10ffff)) for _ in range(1000)])
print(random_string)