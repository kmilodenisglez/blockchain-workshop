### Archivos generados (puedes descargarlos)

* `pdf_base_grade_10.pdf` con el texto grande **"GRADE: 10/20"**.
* `pdf_overlay_grade_20.pdf` con **"GRADE: 20/20"**.
* `attacked_incremental_concat.pdf` concatenando los bytes de ambos PDFs (simulando un append / incremental).

    * Esto deja **dos** `startxref` y `%%EOF` en el archivo final, que es exactamente el tipo de firma/append que suele activar alertas.

* `detection_commands.txt` (instrucciones y comandos)

---

### Herramientas Linux (binarios) para detectar este tipo de manipulación

Te dejo comandos concretos que puedes correr en una máquina Linux para detectar/inspeccionar incrementales y otros indicios:

1. Contar los marcadores `startxref` / `%%EOF` (rápido, siempre funciona):

```bash
grep -a -o 'startxref' attacked_incremental_concat.pdf | wc -l
grep -a -o '%%EOF' attacked_incremental_concat.pdf | wc -l
```

2. `qpdf` — chequear estructura:

```bash
# instala en Debian/Ubuntu: sudo apt install qpdf
qpdf --check attacked_incremental_concat.pdf
qpdf --show-object=trailer attacked_incremental_concat.pdf
```

3. `mutool` (mupdf tools) — información y diagnóstico:

```bash
# instala: sudo apt install mupdf-tools
mutool info attacked_incremental_concat.pdf
mutool clean -gg attacked_incremental_concat.pdf cleaned.pdf   # intentará recomponer/limpiar (no incremental)
```

4. `pdfid.py` / `pdf-parser.py` (Didier Stevens) — análisis profundo y búsqueda de objetos:

```bash
# pdfid.py te da un rápido fingerprint de amenazas (ej. /OpenAction, /JS, etc.)
python pdfid.py attacked_incremental_concat.pdf

# pdf-parser.py permite buscar 'startxref' y ver objetos
python pdf-parser.py --search startxref attacked_incremental_concat.pdf
```

5. Inspección con `strings` / `hexdump` / `xxd`:

```bash
strings pdf_attacked_incremental_concat.pdf | grep -E 'startxref|%%EOF' -n
xxd pdf_attacked_incremental_concat.pdf | less
```

6. `pikepdf` (Python) — programático, te permite abrir y analizar objetos:

```python
import pikepdf
pdf = pikepdf.Pdf.open('pdf_attacked_incremental_concat.pdf')
len(pdf.pages)   # etc.
```

---

### Resultado del análisis rápido (lo que mostró el script)

* `pdf_base_grade_10.pdf` → `startxref: 1`, `%%EOF: 1` ✅
* `pdf_overlay_grade_20.pdf` → `startxref: 1`, `%%EOF: 1` ✅
* `attacked_incremental_concat.pdf` → `startxref: 2`, `%%EOF: 2`  — **incremental append detectado**. 🚨

También incluyo los SHA256 de cada archivo en el script (impreso en la ejecución).

---

### ¿Se verá distinto en distintos lectores?

* En muchos lectores modernos verás la **primera página** o la **última** según cómo el lector resuelva las tablas xref y los incrementales; esto produce el tipo de confusión que quieres demostrar en clase.
* Algunos lectores (o versiones viejas) pueden mostrar la **primera** instancia y otros la **segunda**. Esa diferencia es precisamente la que aprovechan ciertos ataques de visualización.

---

### Cómo usar este demo en clase (sugerencia práctica)

1. Abre `pdf_base_grade_10.pdf` con Reader A — muestra **10/20**.
2. Abre `pdf_attacked_incremental_concat.pdf` con Reader A — (puede mostrar 10/20).
3. Abre `pdf_attacked_incremental_concat.pdf` con Reader B — (algunos lectores pueden mostrar 20/20).
4. Ejecuta en la terminal:

   ```bash
   grep -a -o 'startxref' pdf_attacked_incremental_concat.pdf | wc -l
   ```

   — y muestra que hay **2** ocurrencias: indicio claro de append/incremental.
5. Explica la diferencia entre **verificación criptográfica (firmas, hashes)** vs **inspección estructural** (startxref/%%EOF, objetos XRef).

---

### Nota importante para la parte legal/pedagógica

* Concéntrate en que el `incremental` no siempre es malicioso (firmas legítimas usan append), pero un **incremental extra** después de una firma válida es sospechoso.
* Como aprendiste antes: combina **hashes/signature checks** con **estructural inspection** para distinguir expected vs unexpected increments.

---
