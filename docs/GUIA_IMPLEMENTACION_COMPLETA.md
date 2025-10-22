# 🧠 Guía Completa de Implementación - Proyecto EEG Wavelets y PSD

## 📋 Información del Proyecto

**Proyecto:** Análisis de Señales EEG - Transformada Wavelet y PSD  
**Autor:** Felipe Rangel  
**Institución:** Universidad Pontificia Javeriana  
**Programa:** Mestría en Inteligencia Artificial  
**Repositorio:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD.git](https://github.com/felirangelp/EEG_Wavelets_-_PSD.git)  
**Dashboard Web:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)

## 🎯 Objetivos del Proyecto

- ✅ **Transformada Wavelet Discreta** con función `wavedec()` equivalente
- ✅ **Cálculo de frecuencias centrales** para cada nivel de descomposición
- ✅ **Estimación PSD** con método Welch
- ✅ **Comparación PSD vs FFT**
- ✅ **Dashboard interactivo** con HTML y Plotly
- ✅ **Documentación completa** integrada

## 🚀 Guía de Implementación Paso a Paso

### **Paso 1: Descargar el Proyecto**

#### Opción A: Clonar desde GitHub (Recomendado)
```bash
# Clonar el repositorio
git clone https://github.com/felirangelp/EEG_Wavelets_-_PSD.git

# Entrar al directorio del proyecto
cd EEG_Wavelets_-_PSD
```

#### Opción B: Descargar ZIP
1. Ir a: [https://github.com/felirangelp/EEG_Wavelets_-_PSD](https://github.com/felirangelp/EEG_Wavelets_-_PSD)
2. Hacer clic en "Code" → "Download ZIP"
3. Extraer el archivo ZIP
4. Entrar al directorio extraído

### **Paso 2: Verificar Estructura del Proyecto**

El proyecto debe tener la siguiente estructura:
```
📦 EEG_Wavelets_-_PSD
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
│   ├── DOCUMENTACION_TECNICA.md          # Documentación técnica detallada
│   ├── DOCUMENTACION_FINAL_ORGANIZADA.md # Organización del proyecto
│   ├── documentacion.html                # Documentación HTML estática
│   ├── project_config.ini               # Configuración del proyecto
│   └── INDICE_DOCUMENTACION.md           # Índice de documentación
└── 📁 venv_eeg/                          # Ambiente virtual Python (se crea)
```

### **Paso 3: Configurar Ambiente Python**

#### 3.1 Verificar Python
```bash
# Verificar versión de Python (requiere 3.10+)
python3 --version
# Debe mostrar: Python 3.10.x o superior
```

#### 3.2 Crear Ambiente Virtual
```bash
# Crear ambiente virtual
python3 -m venv venv_eeg

# Activar ambiente virtual
# En macOS/Linux:
source venv_eeg/bin/activate
# En Windows:
# venv_eeg\Scripts\activate
```

#### 3.3 Instalar Dependencias
```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Verificar instalación
pip list | grep -E "(numpy|scipy|matplotlib|plotly|PyWavelets)"
```

### **Paso 4: Ejecutar el Proyecto**

#### Opción A: Dashboard HTML (Más Fácil)
```bash
# Abrir dashboard interactivo en el navegador
open dashboards/dashboard_eeg_simple.html
# En Windows: start dashboards/dashboard_eeg_simple.html
# En Linux: xdg-open dashboards/dashboard_eeg_simple.html
```

#### Opción B: Análisis Python
```bash
# Asegurarse de que el ambiente virtual esté activado
source venv_eeg/bin/activate

# Ejecutar análisis completo
python src/eeg_analysis.py
```

#### Opción C: Script Automático
```bash
# Dar permisos de ejecución (solo la primera vez)
chmod +x run_analysis.sh

# Ejecutar script automático
./run_analysis.sh
```

### **Paso 5: Usar el Dashboard**

#### 5.1 Configuración
1. **Archivo EEG:** Seleccionar `sEEG.mat` o `FileEEG.mat`
2. **Wavelet:** Elegir tipo (recomendado: Daubechies 4)
3. **Niveles:** Configurar entre 3-8 (recomendado: 6)
4. **Frecuencia:** Establecer frecuencia de muestreo (recomendado: 250 Hz)

#### 5.2 Análisis
1. Hacer clic en **"Analizar Señal"**
2. Esperar a que se generen los gráficos
3. Explorar las diferentes pestañas:
   - **Análisis Completo:** Gráficos interactivos
   - **Documentación:** Explicaciones detalladas
   - **Resultados Python:** Análisis generado por Python

### **Paso 6: Interpretar Resultados**

#### 6.1 Bandas de Frecuencia EEG
- **Delta (0.5-4 Hz)**: Sueño profundo
- **Theta (4-8 Hz)**: Relajación, meditación
- **Alpha (8-13 Hz)**: Relajación despierta
- **Beta (13-30 Hz)**: Concentración activa
- **Gamma (30-100 Hz)**: Procesamiento cognitivo

#### 6.2 Resultados Esperados (sEEG con db4, 6 niveles)
- **D1**: 89.29 Hz (Gamma alta)
- **D2**: 44.64 Hz (Gamma media)
- **D3**: 22.32 Hz (Beta alta)
- **D4**: 11.16 Hz (Alpha)
- **D5**: 5.58 Hz (Theta)
- **D6**: 2.79 Hz (Delta)

## 🔧 Solución de Problemas Comunes

### **Error: "python3: command not found"**
```bash
# Instalar Python 3.10+ desde python.org o usar gestor de paquetes
# macOS con Homebrew:
brew install python@3.10
# Ubuntu/Debian:
sudo apt update && sudo apt install python3.10
```

### **Error: "pip: command not found"**
```bash
# Instalar pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### **Error: "No module named 'pywt'"**
```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt
```

### **Error: Dashboard no carga**
```bash
# Verificar que el archivo existe
ls -la dashboards/dashboard_eeg_simple.html

# Abrir con navegador específico
open -a "Google Chrome" dashboards/dashboard_eeg_simple.html
```

### **Error: Archivos .mat no encontrados**
```bash
# Verificar que los archivos estén en el directorio raíz
ls -la *.mat
# Debe mostrar: sEEG.mat y FileEEG.mat
```

## 📊 Características del Dashboard

### **Gráficos Interactivos**
1. **📈 Señal EEG Original** - Dominio del tiempo
2. **🌊 Descomposición Wavelet** - Niveles de frecuencia
3. **📊 Frecuencias Centrales** - Por nivel de descomposición
4. **📈 PSD Método Welch** - Densidad espectral suave
5. **📊 Comparación PSD** - Welch vs FFT

### **Funcionalidades**
- **⚙️ Configuración en tiempo real** de parámetros
- **📚 Documentación integrada** completa
- **🔍 Explicaciones detalladas** para cada gráfico
- **📱 Diseño responsivo** para diferentes pantallas
- **👤 Información del autor** en la cabecera

## 🌐 Acceso Web

### **Dashboard Online**
- **URL:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)
- **Funcionalidad:** Completa, sin necesidad de instalación local
- **Navegadores:** Chrome, Firefox, Safari, Edge

### **Ventajas del Acceso Web**
- ✅ **Sin instalación** requerida
- ✅ **Acceso inmediato** desde cualquier dispositivo
- ✅ **Siempre actualizado** con la última versión
- ✅ **Compatible** con todos los navegadores modernos

## 📚 Documentación Adicional

### **Archivos de Documentación**
- **`README.md`** - Documentación principal del proyecto
- **`docs/DOCUMENTACION_TECNICA.md`** - Detalles técnicos de implementación
- **`docs/INDICE_DOCUMENTACION.md`** - Índice completo de documentación
- **`docs/Transformada Wavelet y PSD en EEG.md`** - Tarea original del proyecto

### **Recursos de Aprendizaje**
- **Wavelets:** [PyWavelets Documentation](https://pywavelets.readthedocs.io/)
- **PSD:** [SciPy Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)
- **Plotly:** [Plotly.js Documentation](https://plotly.com/javascript/)

## 🎓 Aplicaciones Académicas

### **Para Estudiantes**
- **Análisis de señales EEG** con wavelets
- **Comparación de métodos** PSD vs FFT
- **Visualización interactiva** de resultados
- **Interpretación de bandas** de frecuencia

### **Para Investigadores**
- **Código fuente** completamente documentado
- **Métodos implementados** con explicaciones técnicas
- **Resultados reproducibles** con datos incluidos
- **Dashboard interactivo** para presentaciones

### **Para Profesores**
- **Material didáctico** completo
- **Ejemplos prácticos** con datos reales
- **Dashboard web** para demostraciones
- **Documentación técnica** detallada

## 🚀 Comandos de Verificación Rápida

```bash
# Verificar estructura del proyecto
ls -la

# Verificar archivos EEG
ls -la *.mat

# Verificar dashboard
ls -la dashboards/

# Verificar ambiente Python
source venv_eeg/bin/activate && python --version

# Verificar dependencias
pip list | grep -E "(numpy|scipy|matplotlib|plotly|PyWavelets)"

# Probar dashboard
open dashboards/dashboard_eeg_simple.html
```

## 📞 Soporte y Contacto

### **Autor**
**Felipe Rangel**  
Proyecto: Transformada Wavelet y PSD en EEG  
Mestría en Inteligencia Artificial - Universidad Pontificia Javeriana

### **Repositorio**
- **GitHub:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD](https://github.com/felirangelp/EEG_Wavelets_-_PSD)
- **Issues:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD/issues](https://github.com/felirangelp/EEG_Wavelets_-_PSD/issues)

### **Dashboard Web**
- **URL:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)

---

## 🎉 ¡Proyecto Listo para Usar!

Este proyecto está completamente implementado y documentado. Puedes:

1. **Usar el dashboard web** inmediatamente sin instalación
2. **Descargar y ejecutar** localmente siguiendo esta guía
3. **Modificar y extender** el código según tus necesidades
4. **Usar los datos** incluidos para tus propios análisis

**¡Disfruta explorando el análisis de señales EEG con wavelets y PSD!** 🧠✨
