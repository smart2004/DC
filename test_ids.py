import random
import string


for t in range(20):

    letters = string.ascii_uppercase
    digits = string.digits
    key = ''.join(random.choices(digits, k=9))

    with open("test_ids.txt", "a") as myfile:
        myfile.write(f'{key} \n')

    t += 1

myfile.close()
