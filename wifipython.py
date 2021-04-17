#!/usr/bin/env python3 
import random
import os
import subprocess
import sys
from wifi import Cell
import time

caracteres = "abcdefghijklmnñopqrstuvwxyz0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
lista_redes=[]
ssid=""
contador=0
n=0
interfaz=""

def escaneo_redes():
    for cell in Cell.all(interfaz):
        lista_redes.append(cell)
    


def error():
    print("Opcion no valida")

def generador_claves():
    print("Su informacion: \n ssid={} \n interfaz={}".format(ssid,interfaz))
    time.sleep(1)
    while True:
        passwd=""

    

        for i in range(n):
            passwd += caracteres[random.randrange(len(caracteres))]

        print(passwd)


        print(subprocess.call("wpa_passphrase {} {} > red.conf".format(ssid,passwd),shell=True))
        print(subprocess.call("sudo wpa_supplicant -B -i {}  -c red.conf ".format(interfaz),shell=True))

interfaz=input("Ingrese su interfaz inalambrica: ")

respuesta=input("Desea escanear las redes cercanas?? (S/n): ")
respuesta.lower()
print(respuesta)

if(respuesta != "s" and respuesta != "n"):
    error()
elif respuesta=="s":
    escaneo_redes()
    print("Seleccione la red")

    for red in lista_redes:
        print("{}: {}".format(contador,red.ssid))
        contador += 1

    red_seleccionada=input("\n")
    ssid=lista_redes[int(red_seleccionada)].ssid
    interfaz=input("Ingrese su interfaz inalambrica: ")
    n=int(input("Ingrese el numero de caracteres de su clave: "))
    generador_claves()
else:
    ssid=input("Ingrese su ssid: ")
    
    n=int(input("Ingrese el numero de caracteres de su clave: "))
    generador_claves()




