#!/bin/python3 
import click
from random import randint

#Autor@Josue Lopez

"""
Desarrolla un programa que permita generar una n cantidad de IP de forma aleatoria.

El programa debe cumplir con los siguientes requerimientos.

El programa deberá pedir al usuario la cantidad de IPs a generar.
En caso el número ingresado sea menor igual a 0 el programa debe finalizar.
El programa debe mostrar en consola la n cantidad de IPs solicitadas.
Para este ejemplo trabajaremos con IPs v4.
Ejemplo 192.168.0.1
Por default el programa debe generar el archivo: ips.txt de forma local.
El archivo debe almacenar todas las IPs generadas. Una dirección IP por línea.
En caso el usuario no desee generar dicho archivo, al momento de ejecutar el programa deberá expresarlo mediante la bandera --notfile
Ejemplo.

>>> python main.py save
Cantidad de IPs a generar: 4

187.183.22.1
199.123.12.12
12.13.15.15
186.200.200.1

Archivo generado exitosamente.
Ejemplo.

>>> python main.py save --notfile
Cantidad de IPs a generar: 2

187.183.22.1
199.123.12.12
    """



def generar_ipvs4(n : int):
    return [
        str(randint(0,255))+"."+
        str(randint(0,255))+"."+
        str(randint(0,255))+"."+
        str(randint(0,255)) for i in range(1,n)]

@click.command()
@click.option('--save', '-s', is_flag=True,default=False)
@click.option('--notfile', '-s', is_flag=True,default=False)
def main(save,notfile):
    try:
        n = int(input("Cantidad de IPs a generar:"))
        if n >= 0 and n <= 0:
            print("Programa finalizado")
        else:
            if save:
                ipv4 =  generar_ipvs4(n)
                file = open('ips.txt','w')
                print("")
                for ip in ipv4:
                    file.write(ip+"\n")
                    print(ip)
                print("")
                print("Archivo generado exitosamente.")
                file.close
            if notfile:
                ipv4 = generar_ipvs4(n)
                print("")
                for ip in ipv4:
                    print(ip)
    except ValueError as e:
        pass
if __name__ == '__main__':
    main()
