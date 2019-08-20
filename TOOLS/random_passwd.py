import random
import string

all_infos = string.ascii_letters+r"""!#$%&*+?@"""+string.digits
password = ""
for _ in range(15):
    password += random.choices(all_infos)[0]
print(password)
# print(all_infos)
