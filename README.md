
# Esteganografía con Python 3 y PIL

Esteganografía con Python 3. Ejemplo para ocultar texto en imágenes

  

# Modo de uso

  

Los archivos importantes son **ocultar.py** y **leer.py**, dentro de ellos está el código necesario y las funciones para la esteganografía

Recuerda tener instalado Python y pip.  

## Ocultar

Para ocultar simplemente invoca a la función `ocultar_texto` así:

```python

ocultar_texto("Hola, mundo. Esto es un mensaje oculto desde parzibyte.me/blog",  "oveja.png")

```

  

Como primer argumento pasa el texto a ocultar, y como segundo argumento la imagen en donde se guardará el mensaje. Recuerda que opcionalmente puedes indicar un tercer argumento para indicar la imagen de salida, si no lo haces, se guardará en **salida.png**

  

## Mostrar

Para mostrar invoca a la función `leer` así:

```python

mensaje = leer("salida.png")

```

Esta función únicamente toma el nombre de la imagen que tiene el texto oculto

  

# Tutorial

Si quieres ver un ejemplo o cómo fue hecho todo esto, mira el tutorial:

https://parzibyte.me/blog/2018/04/06/esteganografia-python-imagenes-lsb-introduccion/