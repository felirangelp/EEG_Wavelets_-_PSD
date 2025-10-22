# 🧠 Análisis de Señales EEG - Transformada Wavelet y PSD

## 📋 Información del Proyecto

**Proyecto:** Análisis de Señales EEG - Transformada Wavelet y PSD  
**Autor:** Felipe Rangel  
**Institución:** Universidad Pontificia Javeriana  
**Programa:** Mestría en Inteligencia Artificial  
**Fecha:** Octubre 2025  
**Versión:** 1.0.0  
**Repositorio:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD.git](https://github.com/felirangelp/EEG_Wavelets_-_PSD.git)  
**Dashboard Web:** [https://felirangelp.github.io/EEG_Wavelets_-_PSD/](https://felirangelp.github.io/EEG_Wavelets_-_PSD/)  

## 📋 Descripción del Proyecto

Este proyecto implementa el análisis de señales EEG usando **Transformada Wavelet Discreta** y **Estimación de Densidad Espectral de Potencia (PSD)** en Python, reemplazando completamente las funciones de MATLAB con equivalentes en Python.

## 🎯 Objetivos Cumplidos

- ✅ **Transformada Wavelet Discreta** con función `wavedec()` equivalente
- ✅ **Cálculo de frecuencias centrales** para cada nivel de descomposición
- ✅ **Estimación PSD** con método Welch
- ✅ **Comparación PSD vs FFT**
- ✅ **Dashboard interactivo** con HTML y Plotly
- ✅ **Documentación completa** integrada

## 🌐 Acceso Web (Recomendado)

### Dashboard Online - Sin Instalación Requerida
- **URL Principal:** [https://felirangelp.github.io/EEG_Wavelets_-_PSD/](https://felirangelp.github.io/EEG_Wavelets_-_PSD/)
- **Dashboard Directo:** [https://felirangelp.github.io/EEG_Wavelets_-_PSD/dashboards/dashboard_eeg_simple.html](https://felirangelp.github.io/EEG_Wavelets_-_PSD/dashboards/dashboard_eeg_simple.html)

**Ventajas del Acceso Web:**
- ✅ **Sin instalación** requerida
- ✅ **Acceso inmediato** desde cualquier dispositivo
- ✅ **Siempre actualizado** con la última versión
- ✅ **Compatible** con todos los navegadores modernos

## 🚀 Inicio Rápido Local

### Opción 1: Dashboard HTML Local
```bash
# Abrir dashboard interactivo localmente
open dashboards/dashboard_eeg_simple.html
```

### Opción 2: Análisis Python
```bash
# Activar ambiente virtual
source venv_eeg/bin/activate

# Ejecutar análisis
python src/eeg_analysis.py

# O usar script automático
./run_analysis.sh
```

## 📁 Estructura del Proyecto

```
📦 Proyecto EEG - Estructura Final Organizada
├── 📄 README.md                           # Documentación principal
├── 📄 requirements.txt                    # Dependencias Python
├── 📄 run_analysis.sh                     # Script de ejecución
├── 📄 sEEG.mat                           # Archivo EEG 1
├── 📄 FileEEG.mat                        # Archivo EEG 2
├── 📁 src/                               # Código fuente Python
│   └── eeg_analysis.py                   # Análisis principal
├── 📁 dashboards/                         # Dashboards interactivos
│   ├── dashboard_eeg_simple.html          # Dashboard HTML principal
│   └── sEEG_analysis.html               # Análisis HTML generado
├── 📁 docs/                              # Documentación técnica organizada
│   ├── Transformada Wavelet y PSD en EEG.md  # Tarea original
│   ├── DOCUMENTACION_TECNICA.md          # Documentación técnica detallada
│   ├── DOCUMENTACION_FINAL_ORGANIZADA.md # Organización del proyecto
│   ├── documentacion.html                # Documentación HTML estática
│   ├── project_config.ini               # Configuración del proyecto
│   └── INDICE_DOCUMENTACION.md           # Índice de documentación
└── 📁 venv_eeg/                          # Ambiente virtual Python
```

## 🎨 Dashboard Interactivo

### Características del Dashboard HTML:
- **📊 5 Gráficos Interactivos** con explicaciones detalladas
- **⚙️ Configuración en tiempo real** de parámetros
- **📚 Documentación integrada** completa
- **🔍 Explicaciones detalladas** para cada gráfico
- **📱 Diseño responsivo** para diferentes pantallas

### Gráficos Incluidos:
1. **📈 Señal EEG Original** - Dominio del tiempo
2. **🌊 Descomposición Wavelet** - Niveles de frecuencia
3. **📊 Frecuencias Centrales** - Por nivel de descomposición
4. **📈 PSD Método Welch** - Densidad espectral suave
5. **📊 Comparación PSD** - Welch vs FFT

## 🔧 Configuración

### Ambiente Virtual Python
```bash
# Crear ambiente virtual
python3 -m venv venv_eeg

# Activar ambiente
source venv_eeg/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias Principales
- **Python 3.10+**
- **PyWavelets** - Transformada wavelet
- **SciPy** - Procesamiento de señales
- **NumPy** - Operaciones numéricas
- **Matplotlib** - Visualizaciones
- **Plotly** - Gráficos interactivos

## 📊 Análisis Implementados

### 1. Transformada Wavelet Discreta
- **Función MATLAB**: `[c,l] = wavedec(x,n,wname)`
- **Función Python**: `pywt.wavedec(signal, wavelet, level=n)`
- **Wavelets disponibles**: Daubechies, Haar, Coiflet, Biorthogonal
- **Niveles configurables**: 3-8 niveles

### 2. Frecuencias Centrales
- **Función MATLAB**: `FREQ = centfrq('wname')`
- **Función Python**: `pywt.central_frequency(wavelet)`
- **Cálculo por nivel**: `freq = central_freq * fs / (2^level)`

### 3. Estimación PSD
- **Función MATLAB**: `[pxx,f] = pwelch(x,window,noverlap,nfft,fs)`
- **Función Python**: `scipy.signal.welch(x, fs, window, nperseg, noverlap)`
- **Ventanas disponibles**: Hann, Hamming, Blackman, Bartlett

### 4. Comparación PSD vs FFT
- **Método Welch**: Estimación suave y estable
- **Método FFT**: Alta resolución pero ruidoso
- **Comparación visual**: Gráficos superpuestos

## 📈 Resultados Obtenidos

Para la señal sEEG con wavelet db4 y 6 niveles:
- **D1**: 89.29 Hz (Gamma alta)
- **D2**: 44.64 Hz (Gamma media)
- **D3**: 22.32 Hz (Beta alta)
- **D4**: 11.16 Hz (Alpha)
- **D5**: 5.58 Hz (Theta)
- **D6**: 2.79 Hz (Delta)
- **A**: 2.79 Hz (Delta)

## 🎯 Interpretación de Resultados

### Bandas de Frecuencia EEG:
- **Delta (0.5-4 Hz)**: Sueño profundo
- **Theta (4-8 Hz)**: Relajación, meditación
- **Alpha (8-13 Hz)**: Relajación despierta
- **Beta (13-30 Hz)**: Concentración activa
- **Gamma (30-100 Hz)**: Procesamiento cognitivo

### Métodos de Análisis:
- **Wavelet**: Análisis tiempo-frecuencia localizado
- **PSD Welch**: Estimación suave y robusta
- **PSD FFT**: Resolución completa pero ruidosa

## 🚀 Uso del Dashboard

1. **Abrir dashboard**: `open dashboards/dashboard_eeg_simple.html`
2. **Configurar parámetros**: Archivo, wavelet, niveles, frecuencia
3. **Analizar señal**: Hacer clic en "Analizar Señal"
4. **Ver resultados**: Revisar gráficos con explicaciones
5. **Consultar documentación**: Pestaña "Documentación"

## 📚 Documentación Adicional

### 📄 Documentación Técnica
- **📄 Tarea Original**: `docs/Transformada Wavelet y PSD en EEG.md`
- **📄 Documentación Técnica**: `docs/DOCUMENTACION_TECNICA.md`
- **📄 Organización del Proyecto**: `docs/DOCUMENTACION_FINAL_ORGANIZADA.md`
- **📄 Índice de Documentación**: `docs/INDICE_DOCUMENTACION.md`
- **📄 Configuración**: `docs/project_config.ini`

### 📄 Documentación HTML
- **📄 Documentación Estática**: `docs/documentacion.html`
- **📄 Resultados**: `dashboards/sEEG_analysis.html`

## 🔧 Solución de Problemas

### Error de Dashboard Python
Si hay problemas con los dashboards de Python/Dash, use el dashboard HTML:
```bash
open dashboards/dashboard_eeg_simple.html
```

### Error de Dependencias
```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt
```

### Error de Archivos .mat
- Verificar que los archivos estén en el directorio raíz
- Comprobar que los archivos no estén corruptos

## 👨‍💻 Autor

**Felipe Rangel**  
Proyecto: Transformada Wavelet y PSD en EEG  
Mestría en Inteligencia Artificial - Universidad Javeriana

## 📄 Licencia

Este proyecto es parte de un trabajo académico de la Universidad Javeriana.

---

## 🎉 ¡Proyecto Completado!

Todos los objetivos han sido implementados exitosamente:
- ✅ Transformada Wavelet Discreta
- ✅ Frecuencias centrales calculadas
- ✅ Estimación PSD con método Welch
- ✅ Comparación PSD vs FFT
- ✅ Dashboard interactivo funcional
- ✅ Documentación completa

**¡El proyecto está listo para usar!** 🚀
