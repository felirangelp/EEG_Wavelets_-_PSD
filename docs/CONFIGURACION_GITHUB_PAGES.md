# 🌐 Configuración de GitHub Pages - Guía Paso a Paso

## 📋 Información del Proyecto

**Repositorio:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD](https://github.com/felirangelp/EEG_Wavelets_-_PSD)  
**Dashboard Web:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)  
**Autor:** Felipe Rangel - Universidad Pontificia Javeriana

## 🚀 Configuración de GitHub Pages

### **Paso 1: Acceder a Configuración de Pages**

1. **Ir al repositorio:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD](https://github.com/felirangelp/EEG_Wavelets_-_PSD)

2. **Hacer clic en "Settings"** (pestaña superior del repositorio)

3. **Desplazarse hacia abajo** hasta encontrar la sección "Pages" en el menú lateral izquierdo

4. **Hacer clic en "Pages"**

### **Paso 2: Configurar Source**

1. **En "Source":**
   - Seleccionar **"Deploy from a branch"**

2. **En "Branch":**
   - Seleccionar **"main"**
   - Dejar **"/ (root)"** en "Folder"

3. **Hacer clic en "Save"**

### **Paso 3: Verificar Configuración**

Después de guardar, deberías ver:
- ✅ **"Your site is live at https://felirangelp.github.io/EEG_Wavelets_and_PSD/"**
- ✅ Estado: **"Deployed"**

### **Paso 4: Esperar Despliegue**

- **Tiempo estimado:** 1-5 minutos
- **Indicador:** El estado cambiará de "Deploying" a "Deployed"
- **Verificación:** Hacer clic en el enlace para probar

## 🔧 Verificación de Funcionamiento

### **URLs de Acceso**

1. **Página Principal:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)
   - Redirige automáticamente al dashboard
   - Página de bienvenida con información del proyecto

2. **Dashboard Directo:** [https://felirangelp.github.io/EEG_Wavelets_and_PSD/dashboards/dashboard_eeg_simple.html](https://felirangelp.github.io/EEG_Wavelets_and_PSD/dashboards/dashboard_eeg_simple.html)
   - Acceso directo al dashboard interactivo
   - Todas las funcionalidades disponibles

### **Checklist de Verificación**

- [ ] **Página principal carga** sin errores
- [ ] **Redirección automática** funciona (3 segundos)
- [ ] **Dashboard interactivo** carga completamente
- [ ] **Gráficos de Plotly** se renderizan correctamente
- [ ] **Pestañas del dashboard** funcionan
- [ ] **Configuración de parámetros** es funcional
- [ ] **Análisis de señales** se ejecuta correctamente

## 🚨 Solución de Problemas Comunes

### **Error: "404 File not found"**

**Causa:** Archivos HTML no están en el repositorio

**Solución:**
```bash
# Verificar archivos en repositorio
git ls-files | grep html

# Debe mostrar:
# dashboards/dashboard_eeg_simple.html
# dashboards/sEEG_analysis.html
# docs/documentacion.html
# index.html
```

### **Error: "Dashboard no carga"**

**Causa:** Problemas con Plotly.js o JavaScript

**Solución:**
1. **Verificar conexión a internet** (Plotly.js se carga desde CDN)
2. **Probar en navegador diferente**
3. **Verificar consola del navegador** (F12 → Console)

### **Error: "GitHub Pages no se despliega"**

**Causa:** Configuración incorrecta o archivos faltantes

**Solución:**
1. **Verificar configuración** en Settings → Pages
2. **Esperar 5-10 minutos** para el despliegue
3. **Verificar que el branch "main" existe**

## 📊 Estructura de Archivos para GitHub Pages

```
📦 Repositorio GitHub
├── 📄 index.html                           # ✅ Página principal (redirección)
├── 📁 dashboards/                          # ✅ Dashboards interactivos
│   ├── dashboard_eeg_simple.html          # ✅ Dashboard principal
│   └── sEEG_analysis.html                 # ✅ Resultados del análisis
├── 📁 docs/                                # ✅ Documentación
│   └── documentacion.html                  # ✅ Documentación HTML
├── 📁 src/                                 # ✅ Código fuente Python
├── 📄 *.mat                               # ✅ Archivos de datos EEG
├── 📄 requirements.txt                     # ✅ Dependencias Python
└── 📄 README.md                           # ✅ Documentación principal
```

## 🎯 Características del Dashboard Web

### **Funcionalidades Disponibles**
- ✅ **5 Gráficos Interactivos** con Plotly.js
- ✅ **Configuración en tiempo real** de parámetros
- ✅ **Documentación integrada** completa
- ✅ **Análisis de señales EEG** con wavelets
- ✅ **Comparación PSD** Welch vs FFT
- ✅ **Interpretación de bandas** de frecuencia

### **Datos Incluidos**
- ✅ **sEEG.mat** - Señal EEG principal (20,001 muestras)
- ✅ **FileEEG.mat** - Archivo EEG adicional
- ✅ **Resultados pre-calculados** para demostración

### **Tecnologías Utilizadas**
- ✅ **HTML5 + CSS3** - Estructura y estilos
- ✅ **JavaScript** - Interactividad
- ✅ **Plotly.js 2.35.2** - Visualizaciones interactivas
- ✅ **PyWavelets** - Análisis wavelet (código Python)
- ✅ **SciPy** - Procesamiento de señales

## 📚 Documentación Disponible

### **En el Repositorio**
- **`README.md`** - Documentación principal
- **`GUIA_IMPLEMENTACION_COMPLETA.md`** - Guía paso a paso
- **`PREVENCION_ERROR_404.md`** - Prevención de errores
- **`docs/DOCUMENTACION_TECNICA.md`** - Detalles técnicos

### **En el Dashboard Web**
- **Pestaña "Documentación"** - Explicaciones integradas
- **Pestaña "Análisis Completo"** - Gráficos con explicaciones
- **Pestaña "Resultados Python"** - Análisis generado

## 🎓 Uso Académico

### **Para Estudiantes**
- **Acceso inmediato** sin instalación
- **Análisis interactivo** de señales EEG
- **Aprendizaje visual** de conceptos wavelet
- **Comparación de métodos** PSD

### **Para Profesores**
- **Material didáctico** completo
- **Dashboard web** para demostraciones
- **Código fuente** disponible para modificación
- **Documentación técnica** detallada

### **Para Investigadores**
- **Métodos implementados** con explicaciones
- **Código reproducible** con datos incluidos
- **Visualizaciones profesionales** para presentaciones
- **Base para extensiones** futuras

## 🚀 Comandos de Verificación

```bash
# Verificar archivos HTML en repositorio
git ls-files | grep html

# Verificar estado de GitHub Pages
curl -I https://felirangelp.github.io/EEG_Wavelets_and_PSD/

# Verificar dashboard específico
curl -I https://felirangelp.github.io/EEG_Wavelets_and_PSD/dashboards/dashboard_eeg_simple.html
```

## 📞 Soporte

### **Repositorio GitHub**
- **URL:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD](https://github.com/felirangelp/EEG_Wavelets_-_PSD)
- **Issues:** [https://github.com/felirangelp/EEG_Wavelets_-_PSD/issues](https://github.com/felirangelp/EEG_Wavelets_-_PSD/issues)

### **Autor**
**Felipe Rangel**  
Universidad Pontificia Javeriana  
Mestría en Inteligencia Artificial

---

## 🎉 ¡Dashboard Web Funcionando!

El proyecto está completamente desplegado y accesible en:

**🌐 [https://felirangelp.github.io/EEG_Wavelets_and_PSD/](https://felirangelp.github.io/EEG_Wavelets_and_PSD/)**

**¡Disfruta explorando el análisis de señales EEG con wavelets y PSD!** 🧠✨
