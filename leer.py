"""
	Leer mensaje en una imagen utilizando esteganografía, leyendo un bit en cada nivel de color

	Nota: recuerda instalar Pillow:
		pip install Pillow

	@author parzibyte
	@date 06-04-2018
	@web parzibyte.me/blog
"""
from PIL import Image

caracter_terminacion = "11111111"
def obtener_lsb(byte):
	return byte[-1]

def obtener_representacion_binaria(numero):
	return bin(numero)[2:].zfill(8)

def binario_a_decimal(binario):
	return int(binario, 2)

def caracter_desde_codigo_ascii(numero):
	return chr(numero)

def leer(ruta_imagen):
	imagen = Image.open(ruta_imagen)
	pixeles = imagen.load()

	tamaño = imagen.size
	anchura = tamaño[0]
	altura = tamaño[1]

	byte = ""
	mensaje = ""

	for x in range(anchura):
		for y in range(altura):
			pixel = pixeles[x, y]

			rojo = pixel[0]
			verde = pixel[1]
			azul = pixel[2]


			byte += obtener_lsb(obtener_representacion_binaria(rojo))
			if len(byte) >= 8:
				if byte == caracter_terminacion:
					break
				mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
				byte = ""

			byte += obtener_lsb(obtener_representacion_binaria(verde))
			if len(byte) >= 8:
				if byte == caracter_terminacion:
					break
				mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
				byte = ""

			byte += obtener_lsb(obtener_representacion_binaria(azul))
			if len(byte) >= 8:
				if byte == caracter_terminacion:
					break
				mensaje += caracter_desde_codigo_ascii(binario_a_decimal(byte))
				byte = ""

		else:
			continue
		break
	return mensaje

mensaje = leer("salida.png")
print("El mensaje oculto es:")
print(mensaje)