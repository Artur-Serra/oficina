import serial
from time import sleep


class Comandos():
    ler_led = b'1'
    ler_botao = b'2'
    not_led = b'3'
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

    def envia_comando(self, conexao, comando):
        conexao.write(comando)

    def comunicacao(self, route):
        conexao = self.abre_conexao(baudrate=115200, com='COM5')
        # self.envia_comando(conexao=conexao, comando=route)
        conexao.write(route)
        resposta = conexao.read()
        self.fecha_conexao(ser=conexao)
        resposta = str(resposta)
        print(resposta.split("'")[1])
        return resposta
