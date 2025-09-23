## Taller práctico:

---

### 1. Juego de “firma y verificación de mensajes”

Dinámica:

1. Cada estudiante genera su par de claves (pública y privada) con OpenSSL.


2. Firma un mensaje corto usando su clave privada.


3. Otro estudiante verifica la firma usando la clave pública.



Aprendizaje clave: Entender la relación clave pública/privada y la verificación de integridad.

Tip dinámico: Hacerlo con mensajes divertidos o “mensajes secretos” para gamificar.


---

### 2. Mini laboratorio de HTTPS local

Dinámica:

1. Crear un certificado autofirmado con OpenSSL.


2. Configurar un servidor web local (Python http.server o Nginx) para usar ese certificado.


3. Acceder desde un navegador y analizar el certificado.



Aprendizaje clave: Comprender cómo HTTPS usa certificados para cifrar y autenticar.



---

### 3. “Caza de errores” en certificados

Dinámica:

Prepara varios certificados con errores comunes (fecha vencida, CN incorrecto, autofirmado).

Los estudiantes deben detectarlos usando GUI y OpenSSL (openssl x509 -in cert.pem -text -noout).


Aprendizaje clave: Entender validaciones y confianza en certificados.



---

### 4. Cadena de confianza en acción

Dinámica:

Crear un mini CA (autoridad certificadora) con OpenSSL.

Firmar certificados de estudiantes con esa CA.

Ver cómo se construye y verifica la cadena de confianza en GUI o navegador.


Aprendizaje clave: Concepto de CA y cómo los certificados se validan.



---

💡 Tip general: Combinar GUI + línea de comandos para ver visualmente la información y además se entienda cómo funciona realmente debajo del capó.


---