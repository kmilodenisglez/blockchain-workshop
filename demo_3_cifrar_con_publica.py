# cifrar_con_publica.py
# Este script lo ejecuta quien quiere enviar un mensaje cifrado.
# Solo necesita la CLAVE PÚBLICA del destinatario.

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64

# Mensaje secreto que quieres enviar
mensaje_original = b"Hola, este es un mensaje cifrado con tu clave publica. Solo tu puedes leerlo!"
print("✉️  Mensaje original:", mensaje_original.decode())

# Cargar la clave pública del destinatario (alumno.pub.pem)
try:
    with open("alumno.pub.pem", "rb") as f:
        clave_publica = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo 'alumno.pub.pem'.")
    exit(1)

# Cifrar el mensaje con la clave pública
try:
    mensaje_cifrado = clave_publica.encrypt(
        mensaje_original,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
except Exception as e:
    print("❌ Error al cifrar:", e)
    exit(1)

# Guardar el mensaje cifrado en un archivo (en formato base64 para que sea legible/portable)
with open("mensaje_cifrado.bin", "wb") as f:
    f.write(mensaje_cifrado)

# Opcional: también guardar una versión en Base64 para inspección o envío por texto
mensaje_cifrado_b64 = base64.b64encode(mensaje_cifrado).decode('utf-8')
with open("mensaje_cifrado.b64", "w") as f:
    f.write(mensaje_cifrado_b64)

print("\n🔒 Mensaje cifrado guardado en:")
print("   - 'mensaje_cifrado.bin' (formato binario)")
print("   - 'mensaje_cifrado.b64' (formato texto Base64)")
print(f"\n📏 Longitud del mensaje cifrado: {len(mensaje_cifrado)} bytes")
print("\n✅ ¡Listo! Envía los archivos 'mensaje_cifrado.bin' (o .b64) al destinatario.")