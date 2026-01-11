#!/bin/bash
# =============================================================================
# Script de build multilingüe para el Seminario de Estudiantes de Matemáticas UB
# =============================================================================
# Este script genera el sitio en los tres idiomas soportados:
# - Castellano (es)
# - Catalán (ca)
# - Inglés (en)
#
# Uso: ./build.sh
# =============================================================================

set -e  # Salir si hay error

echo "🔨 Generando sitio multilingüe..."
echo ""

# Limpiar directorio de salida
rm -rf _site
mkdir -p _site

# Renderizar cada idioma
echo "Renderizando versión en Castellano..."
quarto render --profile es

echo ""
echo "Renderizando versión en Catalán..."
quarto render --profile ca

echo ""
echo "Renderizando versión en Inglés..."
quarto render --profile en

# Crear página de redirección en la raíz
echo ""
echo "📝 Creando redirección a español..."
cat > _site/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Seminario de Estudiantes de Matemáticas UB</title>
    <meta http-equiv="refresh" content="0; url=es/index.html">
    <link rel="canonical" href="es/index.html">
</head>
<body>
    <p>Redirecting to <a href="es/index.html">Spanish version</a>...</p>
</body>
</html>
EOF

echo ""
echo "✅ Sitio generado correctamente en _site/"
echo "   - _site/es/ (Castellano - default)"
echo "   - _site/ca/ (Catalán)"
echo "   - _site/en/ (Inglés)"
echo ""
echo "Para previsualizar: python -m http.server -d _site 8000"
