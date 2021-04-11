import random

caracteres = "abcdefghijklmnñopqrstuvwxyz0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


passwd=""

for i in range(10):
    passwd += caracteres[random.randrange(len(caracteres))]

print(passwd)
