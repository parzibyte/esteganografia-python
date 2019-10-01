def cambiar_ultimo_bit(byte, nuevo_bit):
	return byte[:-1] + str(nuevo_bit)

def binario_a_decimal(binario):
	return int(binario, 2)

def obtener_representacion_binaria(numero):
	return bin(numero)[2:].zfill(8)

def modificar_color(color_original, bit):
	color_binario = obtener_representacion_binaria(color_original)
	color_modificado = cambiar_ultimo_bit(color_binario, bit)
	return binario_a_decimal(color_modificado)

color_original = 200
color_modificado = modificar_color(color_original, 1) # Cambiar el LSB de 200 por un 1
print("Original: {}".format(color_original))
print("Modificado: {}".format(color_modificado))