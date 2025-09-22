# Guía Práctica: Demo de Firma y Verificación con OpenSSL

**Para estudiantes — paso a paso (Linux / macOS / Windows)**  
**Autor:** Camilo Denis  
**Fecha:** Septiembre 2025  

---

## 🎯 Objetivo

Proveer un flujo práctico y reproducible para que los estudiantes:

- Generen su par de claves (privada/pública).
- Creen un certificado digital.
- Firmen un archivo PDF.
- Permitan que otros verifiquen la firma usando **OpenSSL**.

> ⚠️ **IMPORTANTE**: Nunca compartir la clave privada (`*.key`).  
> Solo compartir: `documento.pdf`, firma (`*.sig` o `*.sig.b64`) y certificado público (`*.crt` o `*.pub.pem`).

---

## 📋 Requisitos

- ✅ **OpenSSL instalado**:
  - En Linux/macOS normalmente ya está disponible.
  - En Windows: usar **WSL (recomendado)**, Git Bash/Cygwin o instalar OpenSSL nativo.
- ✅ Archivo PDF base: `documento.pdf` (puede ser cualquier PDF de ejemplo).
- ✅ Editor de texto para ver archivos PEM (como VS Code, Notepad++, etc.).

---

## 🔍 Comprobación Inicial

Verifica que OpenSSL esté disponible y su versión:

```bash
# Linux / macOS / WSL / Git Bash
openssl version
```

```powershell
# Windows (PowerShell) - si instalaste OpenSSL en esta ruta:
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" version
```

✅ **Salida esperada**: Nombre y versión de OpenSSL (p. ej. `OpenSSL 3.0.x`).

---

## 🔑 Paso 1 — Generar clave privada

Genera una clave RSA de 2048 bits (recomendado):

```bash
# Forma moderna (recomendada)
openssl genpkey -algorithm RSA -out alumno.key -pkeyopt rsa_keygen_bits:2048
```

```bash
# Forma alternativa (compatible con versiones antiguas)
openssl genrsa -out alumno.key 2048
```

> 📝 **Notas**:
> - Guarda `alumno.key` en un lugar seguro.
> - **Nunca** compartas `alumno.key` con nadie.

---

## 📄 Paso 2 — Generar CSR (Solicitud de Certificado)

Crea una CSR con tus datos personales. Usa `-subj` para evitar el prompt interactivo:

```bash
openssl req -new -key alumno.key -out alumno.csr -subj "/C=EC/ST=Pichincha/L=Quito/O=Universidad/OU=Curso/CN=Nombre Apellido/emailAddress=correo@ejemplo.com"
```

> 📝 **Notas**:
> - Reemplaza los valores por los tuyos.
> - En PowerShell, usa comillas simples `'` para `-subj` si hay caracteres problemáticos.
> - Opcional: Ejecuta `openssl req -new -key alumno.key -out alumno.csr` y completa el formulario interactivo.

---

## 🧾 Paso 3 — Autofirmar el certificado (opcional, simple)

Para el demo, usaremos certificados autofirmados:

```bash
openssl x509 -req -in alumno.csr -signkey alumno.key -out alumno.crt -days 365 -sha256
```

✅ **Esto genera**:
- `alumno.key` → clave privada
- `alumno.csr` → solicitud (opcional)
- `alumno.crt` → certificado público en formato X.509 PEM

Extrae la clave pública desde el certificado (necesaria para verificación):

```bash
openssl x509 -in alumno.crt -pubkey -noout > alumno.pub.pem
```

---

## 📄 Paso 4 — Preparar el PDF a firmar

Asegúrate de tener el archivo PDF:

```bash
# Linux/macOS
ls -l documento.pdf
```

```powershell
# PowerShell
Get-ChildItem documento.pdf
```

> El PDF puede ser cualquier archivo; los siguientes comandos firman su hash.

---

## ✍️ Paso 5 — Firmar el documento (crear firma digital)

Firma el PDF (sobre el hash SHA-256):

```bash
openssl dgst -sha256 -sign alumno.key -out documento.sig documento.pdf
```

> 📝 **Notas**:
> - `documento.sig` es un archivo **binario** con la firma.
> - Para enviar por correo (texto ASCII), conviértelo a Base64:

```bash
# Convertir a Base64
openssl base64 -in documento.sig -out documento.sig.b64

# Volver de Base64 a binario
openssl base64 -d -in documento.sig.b64 -out documento.sig
```

---

## 📤 Paso 6 — Compartir (qué enviar y qué NO enviar)

Cada estudiante debe enviar a su compañero:

- `documento.pdf` (el original)
- `documento.sig` o `documento.sig.b64` (la firma)
- `alumno.crt` o `alumno.pub.pem` (clave pública)

> 🚫 **Nunca enviar** `alumno.key` (clave privada).

---

## ✅ Paso 7 — Verificar la firma (receptor)

Pasos para quien recibe la firma:

1. Si recibió `documento.sig.b64`, primero decodifícalo:

```bash
openssl base64 -d -in documento.sig.b64 -out documento.sig
```

2. Asegúrate de tener la clave pública en formato PEM:

```bash
openssl x509 -in alumno.crt -pubkey -noout > alumno.pub.pem
```

3. Verifica la firma:

```bash
openssl dgst -sha256 -verify alumno.pub.pem -signature documento.sig documento.pdf
```

✅ **Salida esperada**: `Verified OK`  
❌ Si sale `'Verification Failure'`: el archivo fue modificado, o la firma/certificado no coincide.

---

## 🛠 Solución de Problemas Comunes

### 1. `"unable to load Public Key"`

- Verifica que estás usando un archivo PEM de clave pública (`alumno.pub.pem`).
- Extrae la clave pública desde el `.crt`:

```bash
openssl x509 -in alumno.crt -pubkey -noout > alumno.pub.pem
```

### 2. `"Verification Failure"`

- Asegúrate de verificar **exactamente el mismo** `documento.pdf` que se firmó.
- Confirma que la firma no fue alterada (si usaste Base64, verifica codificación/decodificación).
- Comprueba que la clave pública corresponde a la clave privada del firmante.

### 3. `"PEM routines:... no start line"`

- El archivo no tiene el encabezado PEM correcto.
- Abre el archivo y verifica que empieza con:
  ```
  -----BEGIN PUBLIC KEY-----
  ```
  o
  ```
  -----BEGIN CERTIFICATE-----
  ```

### 🔍 Comandos útiles de inspección

```bash
# Ver contenido del certificado
openssl x509 -in alumno.crt -text -noout

# Extraer clave pública directamente desde la clave privada
openssl pkey -in alumno.key -pubout -out alumno_from_key.pub.pem

# Comparar si coinciden las claves públicas
diff alumno_from_key.pub.pem alumno.pub.pem
```

---

## 💻 Windows: Recomendaciones y Ejemplos

### Opciones para Windows (recomendado para estudiantes novatos):

#### A) WSL (Recomendado)

- Instala WSL + Ubuntu desde Microsoft Store.
- En Ubuntu:

```bash
sudo apt update && sudo apt install -y openssl
```

- Usa los mismos comandos que en Linux/macOS.

#### B) OpenSSL Nativo en Windows

- Instala una distribución binaria (p. ej. OpenSSL-Win64).
- En PowerShell, usa la ruta completa:

```powershell
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" genpkey -algorithm RSA -out alumno.key -pkeyopt rsa_keygen_bits:2048
```

- Para comandos largos en PowerShell, usa comillas simples `'` para `-subj`.

#### C) Git Bash / Cygwin

- Si tienes Git Bash o Cygwin con OpenSSL, los mismos comandos deberían funcionar.

#### Ejemplo en PowerShell (ruta completa):

```powershell
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" req -new -key alumno.key -out alumno.csr -subj '/C=EC/ST=Pichincha/L=Quito/O=Universidad/CN=Nombre/emailAddress=correo@ejemplo.com'
```

> 📝 **Notas**:
> - La diferencia principal en Windows es la ubicación de `openssl.exe` y el manejo de comillas.
> - **WSL evita la mayoría de problemas** y es la opción más cercana a un entorno Linux.

---

## 🎓 Opcional (Avanzado): Crear una CA Local y Firmar CSRs de Estudiantes

Para demostrar cadena de confianza, el profesor puede crear una CA local y firmar los CSR de los estudiantes.

```bash
# 1. Crear clave y certificado de CA (solo profesor)
openssl genpkey -algorithm RSA -out ca.key -pkeyopt rsa_keygen_bits:4096
openssl req -x509 -new -nodes -key ca.key -sha256 -days 3650 -out ca.crt -subj "/C=EC/ST=Pichincha/L=Quito/O=MiUniversidad/CN=MiCA"

# 2. Firmar CSR de alumno con la CA
openssl x509 -req -in alumno.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out alumno_signed.crt -days 365 -sha256

# 3. Verificar que el certificado del alumno fue firmado por la CA
openssl verify -CAfile ca.crt alumno_signed.crt
```

---

## 🧪 Ejercicio Sugerido en Clase (Resumen Operacional)

1. El profesor distribuye `documento.pdf`.
2. Cada estudiante genera su `key`/`csr`/`crt` siguiendo los pasos.
3. Cada estudiante firma el documento y envía (`documento.pdf` + `firma` + `crt`) a otro alumno.
4. El receptor verifica la firma y reporta `'Verified OK'`.
5. Discutir fallos comunes y por qué ocurre el `'Verification Failure'`.

> 📦 **Material entregable de cada pareja**:
> - `documento.pdf`
> - `documento.sig` (o `.b64`)
> - `alumno.crt` (o `alumno.pub.pem`)
> - Breve reporte indicando si la verificación fue correcta.

---

## 📎 Anexos y Comandos Rápidos

```bash
# Generar clave
openssl genpkey -algorithm RSA -out alumno.key -pkeyopt rsa_keygen_bits:2048

# Generar CSR
openssl req -new -key alumno.key -out alumno.csr -subj "/CN=Nombre/emailAddress=correo@ejemplo.com"

# Autofirmar
openssl x509 -req -in alumno.csr -signkey alumno.key -out alumno.crt -days 365 -sha256

# Extraer pubkey
openssl x509 -in alumno.crt -pubkey -noout > alumno.pub.pem

# Firmar
openssl dgst -sha256 -sign alumno.key -out documento.sig documento.pdf

# Base64 si se necesita
openssl base64 -in documento.sig -out documento.sig.b64

# Verificar
openssl dgst -sha256 -verify alumno.pub.pem -signature documento.sig documento.pdf
```
