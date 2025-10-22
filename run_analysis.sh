#!/bin/bash
# Script para ejecutar el análisis de EEG
# Proyecto: Transformada Wavelet y PSD en EEG

echo "=== Análisis de Señales EEG con Wavelets y PSD ==="
echo ""

# Activar ambiente virtual
echo "Activando ambiente virtual..."
source venv_eeg/bin/activate

# Verificar que las dependencias estén instaladas
echo "Verificando dependencias..."
pip list | grep -E "(numpy|scipy|matplotlib|plotly|PyWavelets)"

echo ""
echo "Opciones disponibles:"
echo "1. Ejecutar análisis básico (genera archivos HTML)"
echo "2. Abrir dashboard HTML interactivo"
echo "3. Ambos"
echo ""

read -p "Seleccione una opción (1-3): " choice

case $choice in
    1)
        echo "Ejecutando análisis básico..."
        python src/eeg_analysis.py
        ;;
    2)
        echo "Abriendo dashboard HTML interactivo..."
        open dashboards/dashboard_eeg_simple.html
        echo "Dashboard abierto en el navegador"
        ;;
    3)
        echo "Ejecutando análisis básico..."
        python src/eeg_analysis.py
        echo ""
        echo "Abriendo dashboard HTML interactivo..."
        open dashboards/dashboard_eeg_simple.html
        echo "Dashboard abierto en el navegador"
        ;;
    *)
        echo "Opción inválida"
        ;;
esac
