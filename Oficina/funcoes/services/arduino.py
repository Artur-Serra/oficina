from typing import Optional

import serial
from time import sleep


class Comandos():
    ler_led = b'a'
    ler_botao = b'b'
    not_led = b'c'
    blink_x = b'4'


class Arduino:

    def abre_conexao(self, baudrate, com):
        ser = serial.Serial()
        ser.baudrate = baudrate
        ser.port = com
        ser.open()
        # Inicializacao da comunicacao
        ser.write(b'\r\n\r\n')
        sleep(2)
        # Limpeza do buffer
        ser.flushInput()
        return ser

    def fecha_conexao(self, ser):
        ser.close()

    def envia_comando(self, comando, numero):
        if comando == Comandos.blink_x:
            self.conexao.write(bytes(numero, 'utf-8'))
        else:
            self.conexao.write(comando)

    def comunicacao(self, route, numero):
        # conexao = self.abre_conexao(baudrate=115200, com='COM5')
        self.envia_comando(comando=route, numero=numero)
        # conexao.write(route)
        resposta = self.conexao.readline()
        # self.fecha_conexao(ser=conexao)
        resposta = str(resposta)
        print(resposta.split("'")[1][:-4])
        return resposta

    def __init__(self):
        self.conexao = self.abre_conexao(baudrate=9600, com='COM7')