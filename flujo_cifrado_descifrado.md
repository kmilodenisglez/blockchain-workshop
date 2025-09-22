# 🔐 Flujo de Cifrado/Descifrado entre Dos Alumnos (RSA + Python)

> ✅ **Objetivo**: Que dos estudiantes intercambien un mensaje secreto cifrado, usando la clave pública del destinatario. Solo el destinatario podrá descifrarlo con su clave privada.

---

## 🎯 Requisitos previos (ambos alumnos deben hacerlo)

Cada alumno debe **generar su propio par de claves** siguiendo los pasos 1-3 de la guía OpenSSL:

```bash
# 1. Generar clave privada
openssl genpkey -algorithm RSA -out alumno.key -pkeyopt rsa_keygen_bits:2048

# 2. Generar CSR (con sus datos)
openssl req -new -key alumno.key -out alumno.csr -subj "/CN=NombreAlumno"

# 3. Autofirmar certificado y extraer clave pública
openssl x509 -req -in alumno.csr -signkey alumno.key -out alumno.crt -days 365 -sha256
openssl x509 -in alumno.crt -pubkey -noout > alumno.pub.pem
```

✅ Cada alumno tendrá:
- `alumno.key` → **CLAVE PRIVADA (¡NUNCA COMPARTIR!)**
- `alumno.pub.pem` → clave pública (para que otros cifren mensajes para ti)

---

## 🔄 Flujo de Interacción entre Alumno A y Alumno B

### Paso 1: Alumno A quiere enviar un mensaje secreto a Alumno B

1. **Alumno A recibe la clave pública de Alumno B** → archivo `alumnoB.pub.pem`.
2. **Alumno A coloca ese archivo en su carpeta de trabajo** y lo renombra a `alumno.pub.pem` (o modifica el script para usar otro nombre).
3. **Alumno A ejecuta el script de cifrado**:

```bash
python3 cifrar_con_publica.py
```

📌 Este script:
- Lee `alumno.pub.pem` (la clave pública de Alumno B).
- Cifra un mensaje secreto predefinido.
- Genera dos archivos:
  - `mensaje_cifrado.bin` → versión binaria.
  - `mensaje_cifrado.b64` → versión en texto (fácil de enviar por correo o chat).

4. **Alumno A envía `mensaje_cifrado.b64` a Alumno B**.

---

### Paso 2: Alumno B recibe y descifra el mensaje

1. **Alumno B recibe el archivo `mensaje_cifrado.b64`** de Alumno A.
2. **Alumno B coloca ese archivo en su carpeta de trabajo** (junto a su `alumno.key`).
3. **Alumno B ejecuta el script de descifrado**:

```bash
python3 descifrar_con_privada.py
```

📌 Este script:
- Lee su clave privada (`alumno.key`).
- Lee `mensaje_cifrado.b64` (o `.bin` si lo tiene).
- **Descifra y muestra el mensaje original en pantalla**.

✅ ¡Solo Alumno B puede leerlo! Ni siquiera Alumno A podría descifrarlo sin la clave privada de B.

---

## 📦 Archivos involucrados en el intercambio

| Archivo                 | ¿Quién lo genera? | ¿Quién lo usa?     | ¿Se comparte? |
|-------------------------|-------------------|--------------------|---------------|
| `alumno.key`            | Cada alumno       | Solo su dueño      | ❌ ¡NUNCA!    |
| `alumno.pub.pem`        | Cada alumno       | Otros para cifrar  | ✅ Sí         |
| `mensaje_cifrado.b64`   | Remitente (A)     | Destinatario (B)   | ✅ Sí         |

---

## 💡 Consejos para la clase

- **Prueben modificando el mensaje** en `cifrar_con_publica.py` para personalizarlo.
- **Intenten usar la clave pública equivocada** → el descifrado fallará.
- **Discutan**: ¿Por qué es seguro compartir `alumno.pub.pem`? ¿Qué pasaría si alguien intercepta `mensaje_cifrado.b64`?

---

## ⚙️ Scripts Python (resumen)

### `cifrar_con_publica.py`
```python
# Usa: alumno.pub.pem
# Genera: mensaje_cifrado.bin, mensaje_cifrado.b64
```

### `descifrar_con_privada.py`
```python
# Usa: alumno.key + mensaje_cifrado.*
# Muestra: mensaje original descifrado
```

---

> Este flujo complementa perfectamente la firma/verificación de PDFs y enseña el otro pilar de la criptografía asimétrica: **la confidencialidad**.
```
