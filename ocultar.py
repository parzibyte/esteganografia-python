"""
	Ocultar mensaje en una imagen utilizando esteganografía, ocultando un bit en cada nivel de color

	Nota: recuerda instalar Pillow:
		pip install Pillow

	@author parzibyte
	@date 06-04-2018
	@web parzibyte.me/blog
"""
from PIL import Image
import math #Utilizado sólo para redondear hacia abajo

caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]


def obtener_representacion_ascii(caracter):
	return ord(caracter)

def obtener_representacion_binaria(numero):
	return bin(numero)[2:].zfill(8)

def cambiar_ultimo_bit(byte, nuevo_bit):
	return byte[:-1] + str(nuevo_bit)

def binario_a_decimal(binario):
	return int(binario, 2)

def modificar_color(color_original, bit):
	color_binario = obtener_representacion_binaria(color_original)
	color_modificado = cambiar_ultimo_bit(color_binario, bit)
	return binario_a_decimal(color_modificado)

def obtener_lista_de_bits(texto):
	lista = []
	for letra in texto:
		representacion_ascii = obtener_representacion_ascii(letra)
		representacion_binaria = obtener_representacion_binaria(representacion_ascii)
		for bit in representacion_binaria:
			lista.append(bit)
	for bit in caracter_terminacion:
		lista.append(bit)
	return lista

def ocultar_texto(mensaje, ruta_imagen_original, ruta_imagen_salida="salida.png"):
	print("Ocultando mensaje...".format(mensaje))
	imagen = Image.open(ruta_imagen_original)
	pixeles = imagen.load()

	tamaño = imagen.size
	anchura = tamaño[0]
	altura = tamaño[1]

	lista = obtener_lista_de_bits(mensaje)
	contador = 0
	longitud = len(lista)
	for x in range(anchura):
		for y in range(altura):
			if contador < longitud:
				pixel = pixeles[x, y]


				rojo = pixel[0]
				verde = pixel[1]
				azul = pixel[2]

				if contador < longitud:
					rojo_modificado = modificar_color(rojo, lista[contador])
					contador += 1
				else:
					rojo_modificado = rojo

				if contador < longitud:
					verde_modificado = modificar_color(verde, lista[contador])
					contador += 1
				else:
					verde_modificado = verde

				if contador < longitud:
					azul_modificado = modificar_color(azul, lista[contador])
					contador += 1
				else:
					azul_modificado = azul

				pixeles[x, y] = (rojo_modificado, verde_modificado, azul_modificado)
			else:
				break
		else:
			continue
		break

	if contador >= longitud:
		print("Mensaje escrito correctamente")
	else:
		print("Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres".format( math.floor((longitud - contador) / 8) ))

	imagen.save(ruta_imagen_salida)


ocultar_texto("Hola, mundo. Esto es un mensaje oculto desde parzibyte.me/blog", "oveja.png")