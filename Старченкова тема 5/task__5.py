import string
#string.ascii_uppercase
#string.ascii_lowercase
#string.ascii_letters
#string.digits
aplphabet = string.ascii_letters + string.digits

from random import sample
def create_key(n) -> list[int]:
    key = sample(aplphabet, k=n)
    key_1 = "".join(key)
    return key_1

password = create_key(8)

print(password)