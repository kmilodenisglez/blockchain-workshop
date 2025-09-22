# descifrar_con_privada.py
# Este script lo ejecuta el destinatario, usando su CLAVE PRIVADA.

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64

# Cargar la clave privada (alumno.key)
try:
    with open("alumno.key", "rb") as f:
        clave_privada = serialization.load_pem_private_key(
            f.read(),
            password=None,  # Asumimos que no tiene contraseña
            backend=default_backend()
        )
except FileNotFoundError:
    print("❌ Error: No se encontró el archivo 'alumno.key'.")
    exit(1)
except ValueError:
    print("❌ Error: La clave privada está protegida con contraseña o está dañada.")
    exit(1)

# Intentar cargar el mensaje cifrado (primero intenta .bin, luego .b64)
mensaje_cifrado = None

try:
    with open("mensaje_cifrado.bin", "rb") as f:
        mensaje_cifrado = f.read()
    print("📂 Leyendo mensaje cifrado desde 'mensaje_cifrado.bin'...")
except FileNotFoundError:
    try:
        with open("mensaje_cifrado.b64", "r") as f:
            contenido_b64 = f.read()
            mensaje_cifrado = base64.b64decode(contenido_b64)
        print("📂 Leyendo mensaje cifrado desde 'mensaje_cifrado.b64'...")
    except FileNotFoundError:
        print("❌ Error: No se encontró ni 'mensaje_cifrado.bin' ni 'mensaje_cifrado.b64'.")
        exit(1)
    except Exception as e:
        print("❌ Error al decodificar Base64:", e)
        exit(1)

# Descifrar el mensaje con la clave privada
try:
    mensaje_descifrado = clave_privada.decrypt(
        mensaje_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("\n🔓 Mensaje descifrado exitosamente:")
    print(">>>", mensaje_descifrado.decode(), "<<<")
    print("\n✅ ¡Éxito! Solo tú, con tu clave privada, puedes leer este mensaje.")
except Exception as e:
    print("\n❌ Error al descifrar:", e)
    print("🔍 Posibles causas: clave privada incorrecta, mensaje alterado, o no corresponde a esta clave.")