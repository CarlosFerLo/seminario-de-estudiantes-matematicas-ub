# Contribuir al Seminario de Estudiantes de Matemáticas UB

¡Gracias por tu interés en contribuir! Esta guía te ayudará a añadir nuevos seminarios o mejorar el sitio web.

## Estructura del proyecto

```
seminario-de-estudiantes-matematicas-ub/
├── _quarto.yml           # Configuración del sitio
├── index.qmd             # Página principal
├── seminarios.qmd        # Archivo de todos los seminarios
├── about.qmd             # Página "Sobre nosotros"
├── seminarios/           # Carpeta con todos los seminarios
│   ├── YYYY-semestre-tema/   # Carpeta de cada seminario
│   │   ├── index.qmd         # Página principal del seminario
│   │   ├── sesion1.qmd       # Sesiones individuales
│   │   ├── notas.tex         # Archivos LaTeX (opcional)
│   │   └── notas.pdf         # PDFs generados
│   └── ...
├── _templates/           # Plantillas para nuevos seminarios
└── .github/workflows/    # CI/CD de GitHub Actions
```

## Cómo añadir un nuevo seminario

### Opción 1: Seminario con múltiples sesiones (recomendado)

1. **Crea una carpeta** en `seminarios/` con el formato `YYYY-semestre-tema`:
   ```
   seminarios/2026-primavera-geometria/
   ```

2. **Copia las plantillas** de `_templates/seminario-nuevo/`:
   - `index.qmd` - Página principal del seminario
   - `sesion.qmd` - Plantilla para cada sesión
   - `notas.tex` - Plantilla LaTeX (opcional)

3. **Edita los archivos** con tu contenido

4. **Actualiza `index.qmd` y `seminarios.qmd`** para incluir el enlace al nuevo seminario

### Opción 2: Seminario solo con PDF

Si solo tienes un PDF de un seminario antiguo:

1. **Crea una carpeta** en `seminarios/`:
   ```
   seminarios/2024-primavera-algebra/
   ```

2. **Añade el PDF** directamente a la carpeta:
   ```
   seminarios/2024-primavera-algebra/notas.pdf
   ```

3. **Actualiza `seminarios.qmd`** con un enlace directo al PDF

## Trabajar con archivos LaTeX

Los archivos `.tex` se compilan automáticamente a PDF en el pipeline de CI/CD. Para ello:

1. Coloca tu archivo `.tex` en la carpeta del seminario
2. El pipeline generará automáticamente el PDF
3. Enlaza el PDF en tu `index.qmd`

### Paquetes LaTeX disponibles

El pipeline incluye TinyTeX con los paquetes más comunes. Si necesitas paquetes adicionales, añádelos al archivo `.github/workflows/publish.yml`.

## Escribir contenido en Quarto

### Matemáticas

Usa LaTeX inline con `$...$` y bloques con `$$...$$`:

```markdown
La ecuación de Euler es $e^{i\pi} + 1 = 0$.

$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

### Callouts

```markdown
::: {.callout-note}
## Nota
Contenido de la nota
:::

::: {.callout-tip}
## Ejemplo
Un ejemplo ilustrativo
:::

::: {.callout-important}
## Teorema
Enunciado del teorema
:::

::: {.callout-warning}
## Advertencia
Algo importante a tener en cuenta
:::
```

## Flujo de trabajo Git

1. **Fork** el repositorio
2. **Crea una rama** para tus cambios:
   ```bash
   git checkout -b nuevo-seminario-geometria
   ```
3. **Haz tus cambios** y commits
4. **Push** a tu fork
5. **Crea un Pull Request**

## Previsualización local

Para ver el sitio en tu ordenador:

```bash
# Instalar Quarto: https://quarto.org/docs/get-started/
quarto preview
```

## Convenciones de nombrado

- **Carpetas de seminarios**: `YYYY-semestre-tema` (ej: `2026-otono-teoria-numeros`)
- **Archivos de sesiones**: `sesionN.qmd` (ej: `sesion1.qmd`, `sesion2.qmd`)
- **PDFs**: nombre descriptivo (ej: `notas.pdf`, `ejercicios.pdf`)

## ¿Preguntas?

Contacta con los organizadores del seminario o abre un Issue en GitHub.
