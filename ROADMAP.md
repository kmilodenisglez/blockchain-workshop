# 📑 Estructura Detallada – 10 Talleres (3h c/u)

---

## **Taller 1 – Introducción y vulnerabilidades en certificados tradicionales**

* **Objetivo:** Entender por qué la educación necesita reforzar sus sistemas de certificación y qué riesgos existen en el modelo actual basado en PDFs.
* **Teoría (1h15m):**

  * Breve introducción al curso y expectativas.
  * Certificados digitales en la actualidad (PDF, firma digital vs firma electrónica).
  * Vulnerabilidades: edición con Adobe/Word, falsificación, uso indebido.
  * Concepto de “confianza” en entornos centralizados.
* **Práctica en equipos (1h30m):**

  * Cada equipo recibe un **PDF de “certificado universitario” firmado electrónicamente (FEA)**.
  * Tarea: intentar **alterar nombre, fecha o calificación** → demostrar lo fácil que es manipularlo.
  * Comparación con un **PDF firmado con FEC** (firma cualificada).
* **Producto esperado:** Reporte corto en pizarra (qué tan fácil fue alterar, qué software usaron, qué implicaciones tiene).

---

## **Taller 2 – Criptografía aplicada a la educación**

* **Objetivo:** Comprender cómo los conceptos básicos de criptografía protegen la integridad y autenticidad de los certificados.
* **Teoría (1h):**

  * Hash, firma digital, clave pública / privada.
  * Diferencia entre cifrado y firma.
  * Ejemplo práctico: “huella digital” de un documento.
* **Práctica en equipos (1h40m):**

  * Uso de **Cryptool Online** para:

    * Generar hash de un certificado.
    * Firmar/verificar con clave privada/pública.
  * Simulación: cambiar 1 byte en el PDF → hash cambia completamente.
  * Cada equipo firma y verifica un archivo de otro equipo.
* **Producto esperado:** Capturas y breve explicación del flujo de firma/verificación.

---

## **Taller 3 – Fraudes en EVAs y análisis de casos**

* **Objetivo:** Analizar vulnerabilidades reales en entornos educativos digitales.
* **Teoría (1h15m):**

  * Estudio de casos: ResearchGate + papers sobre fraudes en institutos.
  * Riesgos de Moodle/Canvas con certificados simples.
  * Vectores de ataque: phishing, PDF editado, cuentas robadas.
* **Práctica (1h30m):**

  * Cada equipo recibe un “caso ficticio” (ej: certificado alterado en Moodle, PDF falsificado, credenciales hackeadas).
  * Deben identificar vulnerabilidades y proponer contramedidas.
* **Producto esperado:** Exposición breve (5 min por equipo).

---

## **Taller 4 – Fundamentos de Blockchain**

* **Objetivo:** Entender los principios básicos de blockchain como solución al fraude.
* **Teoría (1h20m):**

  * Descentralización, consenso, inmutabilidad.
  * PoW vs PoS (solo conceptual, no técnico profundo).
  * ¿Por qué un bloque es “a prueba de edición”?
* **Práctica (1h30m):**

  * Uso de **Anders Brownworth Blockchain Demo** (hash, bloques, ataques).
  * Equipos experimentan cambiando transacciones y viendo ruptura de cadena.
* **Producto esperado:** Mapa conceptual comparando PDF firmado vs documento registrado en blockchain.

---

## **Taller 5 – Verifiable Credentials (VCs)**

* **Objetivo:** Introducir el estándar W3C y su aplicación en educación.
* **Teoría (1h20m):**

  * Qué son las **VCs**.
  * Identificadores descentralizados (DID).
  * Ecosistema: universidades → estudiantes → empleadores.
* **Práctica (1h30m):**

  * Uso de **Blockcerts Playground**:

    * Crear un VC.
    * Emitirlo y verificarlo.
  * Comparación entre un VC válido y uno manipulado.
* **Producto esperado:** Captura del proceso de emisión/verificación de credenciales.

---

## **Taller 6 – Blockcerts en la práctica**

* **Objetivo:** Realizar un ejercicio completo de emisión y validación de certificados académicos en blockchain.
* **Teoría (30m):**

  * Arquitectura Blockcerts (cert-issuer, cert-verifier).
* **Práctica extendida (2h30m):**

  * Cada equipo configura el **Blockcerts Playground** o repositorio simplificado.
  * Emiten un diploma “demo” y lo envían a otro equipo.
  * El segundo equipo debe **verificar la validez**.
* **Producto esperado:** Evidencia de emisión + validación en blockchain.

---

## **Taller 7 – Plataformas y arquitecturas**

* **Objetivo:** Comparar plataformas open source y privadas para certificados educativos.
* **Teoría (1h20m):**

  * OpenCerts, OpenAttestation, Hyperledger, Ethereum/Polygon.
  * Pros/cons de blockchain público vs privado.
  * Patrones de ataque y mitigación.
* **Práctica (1h30m):**

  * Demostración en equipos con **OpenAttestation Toolkit**: crear/verificar un certificado JSON.
  * Comparar con emisión previa en Blockcerts.
* **Producto esperado:** Informe en mural digital: ventajas/desventajas de cada arquitectura.

---

## **Taller 8 – Contratos inteligentes en educación**

* **Objetivo:** Entender cómo la automatización con smart contracts impacta en los EVAs.
* **Teoría (1h20m):**

  * Qué es un contrato inteligente.
  * Casos de uso: matrícula, registro de notas, emisión automática.
* **Práctica (1h30m):**

  * Cada equipo despliega con **HardHat (local)** un contrato simple que emite un “certificado NFT” (ERC-721 simplificado).
  * Simulación de validación por otra cuenta.
* **Producto esperado:** Hash de transacción en red local + NFT emitido.

---

## **Taller 9 – Auditoría y seguridad con Blockchain**

* **Objetivo:** Explorar blockchain como herramienta de auditoría.
* **Teoría (1h15m):**

  * Logs inmutables.
  * Cómo blockchain ayuda contra ataques comunes (OWASP Top 10).
* **Práctica (1h30m):**

  * Uso de explorador blockchain (ej: Polygonscan testnet).
  * Emitir una credencial como NFT en testnet → rastrear transacción.
  * Cada equipo debe auditar un certificado emitido por otro.
* **Producto esperado:** Evidencia de rastreo con dirección hash.

---

## **Taller 10 – Cierre y visión futura**

* **Objetivo:** Integrar todo lo aprendido y proyectar aplicaciones futuras.
* **Teoría (1h):**

  * Regulaciones (GDPR, derecho al olvido).
  * Tendencias: wallets de credenciales, interoperabilidad global.
* **Práctica (1h30m):**

  * Debate en equipos: diseñar un flujo completo de certificación blockchain para una universidad.
  * Presentación final (cada equipo expone 5 min).
* **Producto esperado:** Propuesta de arquitectura educativa con blockchain.

---

# 🚀 Beneficios de esta estructura en 10 talleres

* Ritmo equilibrado (3h por sesión, sin saturar).
* Teoría siempre conectada con práctica en equipos.
* Casos reales + simulaciones → **impacto pedagógico fuerte**.
* Cierra con visión crítica (no solo hype, sino pros/limitaciones).
