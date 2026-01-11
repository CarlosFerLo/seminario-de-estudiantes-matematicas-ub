# Seminario de Estudiantes de Matemáticas UB

[![Build and Deploy](https://github.com/carlosferlo/seminario-de-estudiantes-matematicas-ub/actions/workflows/publish.yml/badge.svg)](https://github.com/tu-usuario/seminario-de-estudiantes-matematicas-ub/actions/workflows/publish.yml)

Sitio web del Seminario de Estudiantes de Matemáticas de la Universitat de Barcelona.

## 🌐 Ver el sitio

Visita: [https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/](https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/)

El sitio está disponible en tres idiomas:
- 🇪🇸 [Castellano](https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/es/)
- 🏴 [Català](https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/ca/)
- 🇬🇧 [English](https://tu-usuario.github.io/seminario-de-estudiantes-matematicas-ub/en/)

## 🚀 Desarrollo local

### Requisitos

- [Quarto](https://quarto.org/docs/get-started/) (>= 1.3)
- Python 3.x
- Git

### Instrucciones

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/seminario-de-estudiantes-matematicas-ub.git
cd seminario-de-estudiantes-matematicas-ub

# Instalar dependencias Python
pip install -r requirements.txt

# Previsualizar el sitio (un idioma)
quarto preview --profile es   # Castellano
quarto preview --profile ca   # Català
quarto preview --profile en   # English

# Construir sitio completo (todos los idiomas)
./build.sh
```

## 🌍 Sistema multilingüe

El sitio soporta tres idiomas usando el sistema de perfiles de Quarto:

### Estructura

```
├── _quarto.yml           # Configuración base
├── _quarto-es.yml        # Perfil Castellano
├── _quarto-ca.yml        # Perfil Català
├── _quarto-en.yml        # Perfil English
├── _i18n/
│   ├── es.yml            # Traducciones Español
│   ├── ca.yml            # Traducciones Català
│   └── en.yml            # Traducciones English
├── _lib/
│   └── i18n.py           # Carga traducciones YAML para Python
├── index.qmd             # Contenido con bloques condicionales
├── about.qmd
└── seminarios.qmd
```

### Cómo funciona

1. **Textos estáticos en Markdown**: Usan bloques condicionales
   ```markdown
   ::: {.content-visible when-profile="es"}
   ## Bienvenidos
   :::
   
   ::: {.content-visible when-profile="ca"}
   ## Benvinguts
   :::
   ```

2. **Textos en archivos .qmd**: Pueden usar variables de Quarto
   ```markdown
   ## {{< var t.bienvenidos >}}
   ```

3. **Textos generados con Python**: Usan el módulo `_lib/i18n.py`
   ```python
   from i18n import get_translations
   t = get_translations()
   print(t['bienvenidos'])  # Automáticamente en el idioma activo
   ```

### Añadir traducciones

Edita los archivos en `_i18n/` (`es.yml`, `ca.yml`, `en.yml`) y añade la clave bajo la sección `t:`

```yaml
t:
  mi_nueva_clave: "Mi nuevo texto"
```

Luego úsala en .qmd con `{{< var t.mi_nueva_clave >}}` o en Python con `t['mi_nueva_clave']`.

## 📝 Añadir un nuevo seminario

1. Crea una carpeta en `seminarios/` con formato `YYYY-semestre-tema`
2. Copia las plantillas de `_templates/seminario-nuevo/`
3. Edita los archivos con tu contenido
4. Haz un Pull Request

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

## 🔧 Estructura del proyecto

```
├── _quarto.yml           # Configuración Quarto base
├── _quarto-{es,ca,en}.yml # Perfiles de idioma
├── _i18n/                # Archivos de traducción YAML
│   ├── es.yml
│   ├── ca.yml
│   └── en.yml
├── _lib/i18n.py          # Carga traducciones para Python
├── index.qmd             # Página principal
├── seminarios.qmd        # Archivo de seminarios
├── about.qmd             # Sobre nosotros
├── seminarios/           # Contenido de cada seminario
│   └── YYYY-semestre-tema/
├── _templates/           # Plantillas
├── build.sh              # Script para construir todos los idiomas
└── .github/workflows/    # CI/CD
```

## 🔄 CI/CD

El sitio se despliega automáticamente en GitHub Pages cuando se hace push a `main`:

1. Se compilan los archivos LaTeX a PDF
2. Se renderiza el sitio en los tres idiomas (es, ca, en)
3. Se crea una página de selección de idioma
4. Se despliega en GitHub Pages

## 📄 Licencia

El contenido de este repositorio está bajo licencia [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## 👥 Contacto

- Email: carlos.ferlo@outlook.com
- Facultat de Matemàtiques i Informàtica, UB
