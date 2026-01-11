# Seminario de Estudiantes de Matemáticas UB

[![Build and Deploy](https://github.com/carlosferlo/seminario-de-estudiantes-matematicas-ub/actions/workflows/publish.yml/badge.svg)](https://github.com/tu-usuario/seminario-de-estudiantes-matematicas-ub/actions/workflows/publish.yml)

Sitio web del Seminario de Estudiantes de Matemáticas de la Universitat de Barcelona.

## 🌐 Ver el sitio

Visita: [https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/](https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/)

## 🚀 Desarrollo local

### Requisitos

- [Quarto](https://quarto.org/docs/get-started/) (>= 1.3)
- Git

### Instrucciones

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/seminario-de-estudiantes-matematicas-ub.git
cd seminario-de-estudiantes-matematicas-ub

# Previsualizar el sitio
quarto preview
```

## 📝 Añadir un nuevo seminario

1. Crea una carpeta en `seminarios/` con formato `YYYY-semestre-tema`
2. Copia las plantillas de `_templates/seminario-nuevo/`
3. Edita los archivos con tu contenido
4. Actualiza `index.qmd` y `seminarios.qmd`
5. Haz un Pull Request

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## 🔧 Estructura del proyecto

```
├── _quarto.yml           # Configuración Quarto
├── index.qmd             # Página principal
├── seminarios.qmd        # Archivo de seminarios
├── about.qmd             # Sobre nosotros
├── seminarios/           # Contenido de cada seminario
│   └── YYYY-semestre-tema/
├── _templates/           # Plantillas
└── .github/workflows/    # CI/CD
```

## 🔄 CI/CD

El sitio se despliega automáticamente en GitHub Pages cuando se hace push a `main`:

1. Se compilan los archivos LaTeX a PDF
2. Se renderiza el sitio Quarto
3. Se despliega en GitHub Pages

## 📄 Licencia

El contenido de este repositorio está bajo licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## 👥 Contacto

- Email: carlos.ferlo@outlook.com
- Facultat de Matemàtiques i Informàtica, UB
