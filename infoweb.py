import requests
#instalar el paquete requests

# Realizar la solicitud GET al servidor web
url = "https://www.ejemplo.com"  # Reemplaza con la URL del servidor web que desees
response = requests.get(url)

# Verificar el código de respuesta HTTP
if response.status_code == 200:
    # Obtener el contenido de la respuesta
    contenido = response.text

    # Guardar el contenido en un archivo de texto
    with open("informacion.txt", "w") as archivo:
        archivo.write(contenido)

    print("La información se ha guardado correctamente en el archivo informacion.txt.")
else:
    print("Error al obtener la información del servidor. Código de respuesta:", response.status_code)
