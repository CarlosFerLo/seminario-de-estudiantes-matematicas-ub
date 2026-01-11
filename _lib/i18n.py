"""
Módulo de internacionalización (i18n) para el Seminario de Estudiantes de Matemáticas UB.

Este módulo carga las traducciones desde los archivos YAML en _i18n/ para los tres 
idiomas soportados:
- Castellano (es) - por defecto
- Catalán (ca)
- Inglés (en)

Uso:
    from i18n import get_translations
    t = get_translations()
    print(t['proximas_sesiones'])

Las traducciones se definen en:
    - _i18n/es.yml
    - _i18n/ca.yml
    - _i18n/en.yml
"""

import os
from pathlib import Path
from typing import Optional

# Intentamos importar PyYAML, si no está disponible usamos un parser simple
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def _simple_yaml_parse(content: str) -> dict:
    """
    Parser YAML simple para casos donde PyYAML no está disponible.
    Solo soporta el formato básico usado en nuestros archivos de traducción.
    """
    result = {}
    current_section = None
    
    for line in content.split('\n'):
        # Ignorar comentarios y líneas vacías
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        
        # Detectar secciones (ej: "t:")
        if stripped.endswith(':') and ':' not in stripped[:-1]:
            current_section = stripped[:-1]
            result[current_section] = {}
            continue
        
        # Parsear key: value
        if ':' in stripped and current_section:
            parts = stripped.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()
            
            # Remover comillas del valor
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]
            
            result[current_section][key] = value
    
    return result


def _load_yaml_file(filepath: Path) -> dict:
    """Carga un archivo YAML y retorna su contenido como diccionario."""
    if not filepath.exists():
        return {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if HAS_YAML:
        data = yaml.safe_load(content) or {}
    else:
        data = _simple_yaml_parse(content)
    
    # Extraer las traducciones del objeto 't'
    return data.get('t', data)


def _get_i18n_dir() -> Path:
    """Obtiene la ruta al directorio _i18n."""
    # Buscar desde el directorio del script hacia arriba
    current = Path(__file__).parent.parent
    i18n_dir = current / '_i18n'
    
    if i18n_dir.exists():
        return i18n_dir
    
    # Fallback: buscar desde el directorio de trabajo actual
    cwd = Path.cwd()
    for parent in [cwd] + list(cwd.parents):
        i18n_dir = parent / '_i18n'
        if i18n_dir.exists():
            return i18n_dir
    
    return Path('_i18n')


# Cargar las traducciones al importar el módulo
_i18n_dir = _get_i18n_dir()
TRANSLATIONS = {
    'es': _load_yaml_file(_i18n_dir / 'es.yml'),
    'ca': _load_yaml_file(_i18n_dir / 'ca.yml'),
    'en': _load_yaml_file(_i18n_dir / 'en.yml'),
}


def get_lang() -> str:
    """
    Obtiene el idioma actual basándose en la variable de entorno QUARTO_PROFILE.
    
    Returns:
        str: Código de idioma ('es', 'ca', o 'en'). Por defecto 'es'.
    """
    profile = os.environ.get('QUARTO_PROFILE', 'es')
    # El perfil puede ser algo como "es" o "es,default", tomamos el primer valor
    lang = profile.split(',')[0].strip()
    if lang not in TRANSLATIONS:
        lang = 'es'
    return lang


def get_translations(lang: Optional[str] = None) -> dict:
    """
    Obtiene el diccionario de traducciones para el idioma especificado.
    
    Args:
        lang: Código de idioma ('es', 'ca', 'en'). Si no se especifica,
              se detecta automáticamente desde QUARTO_PROFILE.
    
    Returns:
        dict: Diccionario con las traducciones para el idioma.
    """
    if lang is None:
        lang = get_lang()
    
    return TRANSLATIONS.get(lang, TRANSLATIONS['es'])


def t(key: str, lang: Optional[str] = None) -> str:
    """
    Función de conveniencia para obtener una traducción específica.
    
    Args:
        key: Clave de la traducción (ej: 'proximas_sesiones')
        lang: Código de idioma. Si no se especifica, se detecta automáticamente.
    
    Returns:
        str: Texto traducido o la clave si no existe.
    """
    translations = get_translations(lang)
    return translations.get(key, key)


# Alias cortos para uso en templates
_ = t
tr = get_translations
