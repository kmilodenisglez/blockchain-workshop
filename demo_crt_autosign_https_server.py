# https_server.py
import http.server
import ssl
import sys

# Configuración
PORT = 8443
KEYFILE = "alumno.key"     # Tu clave privada
CERTFILE = "alumno.crt"    # ¡Tu certificado autofirmado (NO la clave pública .pub.pem)!

# Verificar que los archivos existen
try:
    with open(KEYFILE) as f: pass
    with open(CERTFILE) as f: pass
except FileNotFoundError as e:
    print(f"Error: No se encontró el archivo {e.filename}")
    sys.exit(1)

# Crear servidor
httpd = http.server.HTTPServer(('127.0.0.1', PORT), http.server.SimpleHTTPRequestHandler)

# Envolver el socket con SSL
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile=KEYFILE,
    certfile=CERTFILE,
    server_side=True
)

print(f"Servidor HTTPS corriendo en https://127.0.0.1:{PORT}")
print("⚠️  Advertencia: Certificado autofirmado. El navegador mostrará advertencia de seguridad.")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServidor detenido.")
