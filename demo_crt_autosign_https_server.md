# **Taller Práctico: Certificados Digitales y Firmas**

**Duración:** 1 hora
**Objetivo:** Que los estudiantes comprendan y experimenten la creación, uso y verificación de certificados digitales.
**Herramientas:**

* Linux: OpenSSL, Seahorse (GNOME) o XCA
* Windows: OpenSSL (opcional GUI como XCA)

---

## **1️⃣ Introducción rápida (5 min)**

* Conceptos clave:

  * Clave pública / clave privada
  * Certificados X.509
  * Firma digital y verificación
* Mostrar visualmente con un ejemplo de **firma de un mensaje**.

---

## **2️⃣ Generar un par de claves (10 min)**

**Linux / Windows (OpenSSL CLI):**

```bash
# Generar clave privada
openssl genpkey -algorithm RSA -out mi_clave_privada.pem -aes256

# Generar certificado autofirmado
openssl req -new -x509 -key mi_clave_privada.pem -out mi_certificado.pem -days 365
```

**GUI:**

* **Seahorse (Linux GNOME)**

  * Abrir → “Certificados” → Importar `.pem` → Ver detalles
* **XCA (Linux/Windows)**

  * Crear un proyecto → Importar clave → Crear certificado → Ver cadena de confianza

💡 Tip: Cada estudiante puede agregar su nombre y correo en el certificado para personalizarlo.

---

## **3️⃣ Firmar un mensaje y enviarlo a un compañero (15 min)**

**OpenSSL CLI:**

```bash
# Crear mensaje
echo "Hola, esto es secreto" > mensaje.txt

# Firmar
openssl dgst -sha256 -sign mi_clave_privada.pem -out mensaje.sig mensaje.txt

# Verificar con la clave pública
openssl dgst -sha256 -verify mi_certificado.pem -signature mensaje.sig mensaje.txt
```

**Actividad dinámica:**

* Cada estudiante firma un mensaje y se lo envía a otro compañero.
* El compañero verifica la firma con la clave pública.
* Resultado esperado: verificación “OK”.

---

## **4️⃣ Explorar certificados con GUI (10 min)**

* Abrir los certificados `.pem` o `.p12` en **Seahorse** o **XCA**.
* Observar:

  * Propietario (CN, email)
  * Periodo de validez
  * Algoritmo de firma

**Extra:** Si usan navegador:

* Firefox → `Preferences → Privacy & Security → Certificates → View Certificates`

---

## **5️⃣ Mini laboratorio: HTTPS local (10 min)** 

### ✅ Opción 1: Usa un [script Python](./demo_crt_autosign_https_server.py) personalizado con SSL

#### 📌 Requisitos:
- Necesitas tener el certificado **`alumno.crt`** (generado en el Paso 3 de la guía [guia_firma_verificacion_openssl.md](./guia_firma_verificacion_openssl.md)).
- Ejecuta:
  ```bash
  python3 https_server.py
  ```
- Abre en tu navegador: `https://127.0.0.1:8443`

> ⚠️ El navegador mostrará una advertencia de seguridad porque el certificado es autofirmado. Haz clic en "Avanzado" > "Aceptar riesgo" (solo para pruebas locales).

---

### ✅ Opción 2: Usa `openssl s_server` (para pruebas rápidas)

Si solo quieres servir un archivo o directorio con HTTPS rápidamente, puedes usar OpenSSL directamente:

```bash
# En el directorio que quieres servir
openssl s_server -key alumno.key -cert alumno.crt -port 8443 -www
```

Luego abre: `https://localhost:8443`

> Nota: `-www` hace que OpenSSL sirva archivos estáticos del directorio actual. Es muy básico, pero útil para pruebas.

---

### ✅ Opción 3: Usa herramientas como `mkcert` + servidor (recomendado para desarrollo)

Si quieres evitar advertencias del navegador:

1. Instala [`mkcert`](https://github.com/FiloSottile/mkcert) (crea certificados locales de confianza).
2. Genera un certificado local:
   ```bash
   mkcert 127.0.0.1 localhost
   ```
3. Usa ese certificado con el script Python de la Opción 1.

---

## 🚫 ¿Por qué no usar `alumno.pub.pem`?

- `alumno.pub.pem` contiene solo:
  ```
  -----BEGIN PUBLIC KEY-----
  ... (clave pública en formato PKCS#8)
  -----END PUBLIC KEY-----
  ```

- Un certificado SSL (`.crt`) contiene:
  ```
  -----BEGIN CERTIFICATE-----
  ... (datos del titular, emisor, vigencia, firma, Y la clave pública)
  -----END CERTIFICATE-----
  ```

El protocolo HTTPS **requiere el certificado completo**, no solo la clave pública.

---

## ✅ Resumen de lo que debes hacer:

1. **Usa `alumno.crt`**, no `alumno.pub.pem`.
2. **Usa el script personalizado o `openssl s_server`.
3. **Acepta la advertencia del navegador** si usas certificado autofirmado (es normal en pruebas).

---

## **6️⃣ Detectar errores comunes (5 min)**

* Prepara 2-3 certificados con errores:

  * Fecha vencida
  * CN incorrecto
  * Autofirmado vs CA real
* Actividad: Identificar el error usando **GUI y OpenSSL CLI**.

---

## **7️⃣ Cierre y discusión (5 min)**

* ¿Qué aprendimos?

  * Claves públicas y privadas
  * Firmas digitales y verificación
  * Cómo inspeccionar certificados visualmente
  * Errores comunes y advertencias en navegadores

* **Bonus:** Mostrar cómo crear mini CA y firmar certificados de compañeros para reforzar la cadena de confianza.
