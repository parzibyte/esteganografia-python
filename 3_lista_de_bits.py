caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]

def obtener_representacion_ascii(caracter):
	return ord(caracter)

def obtener_representacion_binaria(numero):
	return bin(numero)[2:].zfill(8)

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

print("Hola en bits es")
print(obtener_lista_de_bits("Hola"))