# Contribuir al Seminario de Estudiantes de Matemáticas UB

¡Gracias por tu interés en contribuir! Esta guía te ayudará a añadir nuevos seminarios.

## 📂 Estructura del proyecto

```
seminario-de-estudiantes-matematicas-ub/
├── seminarios/
│   └── YYYY-semestre-tema/
│       ├── seminario.yml     # ⭐ EDITA SOLO ESTE ARCHIVO
│       ├── index.qmd         # Página del seminario (no tocar)
│       ├── sesion1_notas.pdf # PDFs de sesiones
│       └── *.tex             # LaTeX (se compila a PDF)
├── _templates/               # Plantillas
└── .github/workflows/        # CI/CD
```

## 🚀 Añadir un nuevo seminario

### 1. Crear carpeta y copiar plantilla

```bash
mkdir seminarios/2026-primavera-geometria
cp _templates/seminario-nuevo/* seminarios/2026-primavera-geometria/
```

### 2. Editar `seminario.yml`

**Este es el único archivo que necesitas editar. El seminario aparecerá automáticamente en la página de inicio y en el archivo de seminarios.**

```yaml
info:
  titulo: "Geometría Diferencial"
  subtitulo: "Seminario de Primavera 2026"
  descripcion: |
    Introducción a las variedades diferenciables.
  ponente: "Tu Nombre"
  estado: "en-curso"  # planificado | en-curso | completado

sesiones:
  - numero: 1
    titulo: "Variedades diferenciables"
    fecha: "2026-02-15"
    hora: "12:00"
    lugar: "Aula T2"
    estado: "completada"  # planificada | completada | cancelada
    notas_pdf: "sesion1_notas.pdf"  # opcional
    
  - numero: 2
    titulo: "Campos vectoriales"
    fecha: "2026-02-22"
    estado: "planificada"

materiales:
  notas_generales:
    pdf: "notas.pdf"  # cuando termine el seminario
  ejercicios: "ejercicios.pdf"

bibliografia:
  - autor: "Lee, J.M."
    titulo: "Introduction to Smooth Manifolds"
    año: 2012
```

### 3. Añadir materiales

- Pon los PDFs en la misma carpeta
- Los `.tex` se compilan automáticamente a PDF

### 4. Actualizar páginas principales

Añade el enlace en `index.qmd` y `seminarios.qmd`.

## 📝 Actualizar un seminario existente

Solo edita `seminario.yml`:

| Acción | Qué hacer |
|--------|-----------|
| Añadir sesión | Nuevo elemento en `sesiones:` |
| Marcar completada | `estado: "completada"` |
| Añadir PDF | `notas_pdf: "archivo.pdf"` |
| Seminario terminado | `estado: "completado"` en `info:` |

## 📁 Seminarios antiguos (solo PDF)

```bash
mkdir seminarios/2024-primavera-algebra
# Añade el PDF directamente y enlázalo desde seminarios.qmd
```

## 💻 Previsualización local

```bash
pip install pyyaml
quarto preview --profile es  # Castellano
quarto preview --profile ca  # Català
quarto preview --profile en  # English

# O construir todos los idiomas:
./build.sh
```

## 🌍 Sistema multilingüe

El sitio soporta tres idiomas (es, ca, en). No necesitas hacer nada especial para los seminarios - el contenido de `seminario.yml` se muestra igual en todos los idiomas.

Si necesitas añadir nuevas traducciones para la interfaz:

1. Edita los archivos YAML en `_i18n/` (`es.yml`, `ca.yml`, `en.yml`)
2. Añade la clave bajo la sección `t:` en cada archivo

Ejemplo en `_i18n/es.yml`:
```yaml
t:
  mi_nueva_clave: "Mi texto en español"
```

Ejemplo en `_i18n/ca.yml`:
```yaml
t:
  mi_nueva_clave: "El meu text en català"
```

Ejemplo en `_i18n/en.yml`:
```yaml
t:
  mi_nueva_clave: "My text in English"
```

Luego úsala:
- En archivos `.qmd`: `{{< var t.mi_nueva_clave >}}`
- En código Python: `t['mi_nueva_clave']` (importando `from i18n import get_translations; t = get_translations()`)

## ❓ ¿Preguntas?

Abre un Issue en GitHub o contacta a los organizadores.
