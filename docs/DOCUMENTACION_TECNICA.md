# 📚 Documentación Técnica - Proyecto EEG

## 🎯 Información del Proyecto

**Proyecto:** Análisis de Señales EEG - Transformada Wavelet y PSD  
**Autor:** Felipe Rangel  
**Institución:** Universidad Pontificia Javeriana  
**Programa:** Mestría en Inteligencia Artificial  
**Fecha:** Octubre 2025  
**Versión:** 1.0.0  

## 📋 Objetivos Cumplidos

### ✅ Objetivos Principales
1. **Transformada Wavelet Discreta** - Implementación completa con `pywt.wavedec()`
2. **Cálculo de Frecuencias Centrales** - Para cada nivel de descomposición
3. **Estimación PSD** - Método Welch implementado con `scipy.signal.welch()`
4. **Comparación PSD vs FFT** - Análisis comparativo implementado
5. **Dashboard Interactivo** - HTML con Plotly.js funcional

### ✅ Objetivos Técnicos
- Reemplazo completo de funciones MATLAB por Python
- Implementación de análisis tiempo-frecuencia
- Visualización interactiva de resultados
- Documentación técnica completa

## 🔧 Implementación Técnica

### 1. Transformada Wavelet Discreta
```python
# MATLAB: [c,l] = wavedec(x,n,wname)
# Python equivalente:
coeffs = pywt.wavedec(signal, wavelet, level=n)
```

**Características:**
- Wavelets disponibles: Daubechies, Haar, Coiflet, Biorthogonal
- Niveles configurables: 3-8 niveles
- Reconstrucción por niveles usando `pywt.upcoef()`

### 2. Frecuencias Centrales
```python
# MATLAB: FREQ = centfrq('wname')
# Python equivalente:
central_freq = pywt.central_frequency(wavelet)
freq_per_level = central_freq * fs / (2**level)
```

**Cálculo por nivel:**
- D1: 89.29 Hz (Gamma alta)
- D2: 44.64 Hz (Gamma media)
- D3: 22.32 Hz (Beta alta)
- D4: 11.16 Hz (Alpha)
- D5: 5.58 Hz (Theta)
- D6: 2.79 Hz (Delta)

### 3. Estimación PSD
```python
# MATLAB: [pxx,f] = pwelch(x,window,noverlap,nfft,fs)
# Python equivalente:
f, psd = scipy.signal.welch(x, fs, window='hann', nperseg=256, noverlap=128)
```

**Parámetros:**
- Ventana: Hann (por defecto)
- Segmentos: 256 muestras
- Solapamiento: 50%

### 4. Comparación PSD vs FFT
- **Método Welch**: Suavizado alto, varianza baja, estable
- **Método FFT**: Resolución alta, detalle completo, ruidoso

## 📊 Resultados Obtenidos

### Análisis de Señal sEEG
- **Archivo:** sEEG.mat
- **Wavelet:** Daubechies 4 (db4)
- **Niveles:** 6
- **Frecuencia de muestreo:** 250 Hz

### Bandas de Frecuencia Identificadas
- **Gamma alta (D1)**: 89.29 Hz - Procesamiento cognitivo
- **Gamma media (D2)**: 44.64 Hz - Procesamiento cognitivo
- **Beta alta (D3)**: 22.32 Hz - Concentración activa
- **Alpha (D4)**: 11.16 Hz - Relajación despierta
- **Theta (D5)**: 5.58 Hz - Relajación, meditación
- **Delta (D6)**: 2.79 Hz - Sueño profundo

## 🎨 Dashboard Interactivo

### Características Técnicas
- **Framework:** HTML5 + CSS3 + JavaScript
- **Visualizaciones:** Plotly.js
- **Diseño:** Responsivo y moderno
- **Interactividad:** Configuración en tiempo real

### Gráficos Implementados
1. **Señal EEG Original** - Dominio del tiempo
2. **Descomposición Wavelet** - Niveles de frecuencia
3. **Frecuencias Centrales** - Por nivel de descomposición
4. **PSD Método Welch** - Densidad espectral suave
5. **Comparación PSD** - Welch vs FFT

## 📁 Estructura del Proyecto

```
📦 Proyecto EEG - Estructura Final
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
├── 📁 docs/                              # Documentación técnica
│   ├── Transformada Wavelet y PSD en EEG.md  # Tarea original
│   ├── DOCUMENTACION_TECNICA.md          # Este archivo
│   ├── DOCUMENTACION_FINAL_ORGANIZADA.md # Organización del proyecto
│   ├── documentacion.html                # Documentación HTML estática
│   └── project_config.ini               # Configuración del proyecto
└── 📁 venv_eeg/                          # Ambiente virtual Python
```

## 🚀 Instrucciones de Uso

### Opción 1: Dashboard HTML (Recomendado)
```bash
# Abrir dashboard interactivo
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

## 🔧 Configuración del Ambiente

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

## 📈 Interpretación de Resultados

### Bandas de Frecuencia EEG
- **Delta (0.5-4 Hz)**: Sueño profundo, estados inconscientes
- **Theta (4-8 Hz)**: Relajación, meditación, estados creativos
- **Alpha (8-13 Hz)**: Relajación despierta, estados de calma
- **Beta (13-30 Hz)**: Concentración activa, estados de alerta
- **Gamma (30-100 Hz)**: Procesamiento cognitivo, integración sensorial

### Métodos de Análisis
- **Wavelet**: Análisis tiempo-frecuencia localizado, ideal para señales no estacionarias
- **PSD Welch**: Estimación suave y robusta, reduce el ruido
- **PSD FFT**: Resolución completa pero ruidosa, útil para análisis detallado

## 🎯 Logros Técnicos

### ✅ Implementaciones Exitosas
1. **Reemplazo completo de MATLAB** por Python
2. **Análisis tiempo-frecuencia** con wavelets
3. **Estimación espectral robusta** con método Welch
4. **Visualización interactiva** con dashboard HTML
5. **Documentación técnica completa**

### ✅ Optimizaciones Realizadas
- Manejo robusto de archivos .mat
- Validación de señales EEG
- Interfaz de usuario intuitiva
- Código modular y mantenible

## 🔍 Solución de Problemas

### Error de Archivos .mat
- Verificar que los archivos estén en el directorio raíz
- Comprobar que los archivos no estén corruptos
- Validar que las señales tengan más de 100 muestras

### Error de Dependencias
```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt
```

### Error de Dashboard
- Usar el dashboard HTML: `open dashboards/dashboard_eeg_simple.html`
- Verificar que el navegador soporte JavaScript

## 📚 Referencias Técnicas

### Librerías Python Utilizadas
- **PyWavelets**: Transformada wavelet discreta
- **SciPy**: Procesamiento de señales y análisis espectral
- **NumPy**: Operaciones numéricas y arrays
- **Matplotlib**: Visualizaciones estáticas
- **Plotly**: Gráficos interactivos

### Métodos Implementados
- **DWT**: Transformada Wavelet Discreta
- **Welch**: Estimación de densidad espectral de potencia
- **FFT**: Transformada Rápida de Fourier
- **Análisis tiempo-frecuencia**: Descomposición wavelet

## 🎉 Conclusión

El proyecto ha sido implementado exitosamente cumpliendo todos los objetivos técnicos:

- ✅ **Transformada Wavelet Discreta** implementada
- ✅ **Frecuencias centrales** calculadas correctamente
- ✅ **Estimación PSD** con método Welch funcional
- ✅ **Comparación PSD vs FFT** implementada
- ✅ **Dashboard interactivo** operativo
- ✅ **Documentación técnica** completa

**El proyecto está listo para uso académico y profesional.** 🚀
