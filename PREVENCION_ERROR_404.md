# 🚨 Prevención de Error 404 en GitHub Pages - Guía Completa

## 📋 Problema Común: Error 404 en GitHub Pages

**Error Típico:** Dashboard funciona localmente pero muestra "404 File not found" en GitHub Pages

**Causa Raíz:** Archivos HTML del dashboard siendo ignorados por Git debido a reglas en `.gitignore`

**Impacto:** Dashboard no accesible públicamente, proyecto no funcional para evaluación

## ✅ Solución Preventiva Implementada

### **1. Configuración .gitignore Correcta**

El archivo `.gitignore` está configurado para NO ignorar archivos HTML del proyecto:

```gitignore
# IMPORTANTE: NO ignorar archivos HTML del dashboard
# Los siguientes archivos DEBEN estar en el repositorio para GitHub Pages:
# - dashboards/dashboard_eeg_simple.html
# - dashboards/sEEG_analysis.html
# - dashboards/documentacion.html

# Solo ignorar archivos HTML temporales o de prueba
# *.html  # COMENTADO - No ignorar archivos HTML del proyecto
```

### **2. Verificación Obligatoria**

Antes de hacer push, siempre verificar:

```bash
# Verificar que los archivos HTML están en el repositorio
git ls-files | grep html
# Debe mostrar:
# dashboards/dashboard_eeg_simple.html
# dashboards/sEEG_analysis.html
# dashboards/documentacion.html

# Verificar que NO están siendo ignorados
git check-ignore dashboards/dashboard_eeg_simple.html
# No debe mostrar nada (archivo vacío)
```

### **3. Comandos de Diagnóstico**

```bash
# Diagnóstico completo
echo "=== Archivos HTML en repositorio ==="
git ls-files | grep html

echo "=== Archivos HTML ignorados ==="
git check-ignore dashboards/*.html

echo "=== Estado de archivos HTML ==="
git status dashboards/*.html
```

## 🔧 Proceso de Publicación Seguro

### **Paso 1: Verificación Pre-Push**
```bash
# Verificar estructura
ls -la dashboards/

# Verificar que los archivos están trackeados
git ls-files | grep html

# Verificar que no están ignorados
git check-ignore dashboards/*.html
```

### **Paso 2: Agregar Archivos**
```bash
# Agregar todos los archivos del proyecto
git add .

# Verificar qué se va a commitear
git status
```

### **Paso 3: Commit y Push**
```bash
# Commit con mensaje descriptivo
git commit -m "🚀 Publicar proyecto EEG completo con dashboard funcional"

# Push al repositorio
git push origin main
```

### **Paso 4: Verificación Post-Push**
```bash
# Verificar en GitHub que los archivos están presentes
# Ir a: https://github.com/felirangelp/EEG_Wavelets_-_PSD
# Verificar que aparecen:
# - dashboards/dashboard_eeg_simple.html
# - dashboards/sEEG_analysis.html
# - dashboards/documentacion.html
```

## 🌐 Configuración de GitHub Pages

### **Paso 1: Habilitar GitHub Pages**
1. Ir a: `https://github.com/felirangelp/EEG_Wavelets_-_PSD/settings/pages`
2. En "Source", seleccionar "Deploy from a branch"
3. En "Branch", seleccionar "main"
4. En "Folder", seleccionar "/ (root)"
5. Hacer clic en "Save"

### **Paso 2: Configurar Archivo Index**
Crear `index.html` en la raíz del repositorio:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EEG Wavelets y PSD - Dashboard</title>
    <meta http-equiv="refresh" content="0; url=dashboards/dashboard_eeg_simple.html">
</head>
<body>
    <p>Redirigiendo al dashboard...</p>
    <p>Si no eres redirigido automáticamente, <a href="dashboards/dashboard_eeg_simple.html">haz clic aquí</a>.</p>
</body>
</html>
```

### **Paso 3: URLs de Acceso**
- **Página Principal:** `https://felirangelp.github.io/EEG_Wavelets_-_PSD/`
- **Dashboard Directo:** `https://felirangelp.github.io/EEG_Wavelets_-_PSD/dashboards/dashboard_eeg_simple.html`

## 📊 Verificación de Funcionamiento

### **Checklist de Verificación**
- [ ] Archivos HTML están en el repositorio GitHub
- [ ] GitHub Pages está habilitado
- [ ] `index.html` redirige correctamente
- [ ] Dashboard carga sin errores 404
- [ ] Gráficos de Plotly funcionan
- [ ] Pestañas del dashboard funcionan
- [ ] Archivos .mat están incluidos

### **Comandos de Verificación**
```bash
# Verificar archivos en repositorio
git ls-files | grep -E "(html|mat)"

# Verificar estado de GitHub Pages
curl -I https://felirangelp.github.io/EEG_Wavelets_-_PSD/

# Verificar dashboard específico
curl -I https://felirangelp.github.io/EEG_Wavelets_-_PSD/dashboards/dashboard_eeg_simple.html
```

## 🚨 Solución de Problemas

### **Error: "404 File not found"**
```bash
# Diagnóstico
git ls-files | grep html
git check-ignore dashboards/*.html

# Si faltan archivos, agregarlos
git add dashboards/*.html
git commit -m "🔧 Agregar archivos HTML faltantes"
git push origin main
```

### **Error: "Dashboard no carga"**
```bash
# Verificar que Plotly.js está disponible
# El dashboard usa: https://cdn.plot.ly/plotly-2.35.2.min.js

# Verificar en el navegador:
# F12 → Console → Buscar errores de JavaScript
```

### **Error: "Archivos .mat no encontrados"**
```bash
# Verificar que los archivos están en el repositorio
git ls-files | grep mat

# Si faltan, agregarlos
git add *.mat
git commit -m "📁 Agregar archivos de datos EEG"
git push origin main
```

## 📚 Lecciones Aprendidas

### **1. Configuración .gitignore Crítica**
- Los archivos HTML del dashboard NO deben estar en `.gitignore`
- Comentar reglas que puedan causar problemas
- Verificar siempre qué archivos se están ignorando

### **2. Verificación Obligatoria**
- `git ls-files | grep html` debe mostrar todos los archivos HTML
- `git check-ignore dashboard.html` no debe mostrar nada
- Probar GitHub Pages antes de considerar el proyecto completo

### **3. Proceso de Diagnóstico**
1. Verificar archivos en repositorio
2. Verificar reglas de `.gitignore`
3. Corregir configuración
4. Agregar archivos faltantes
5. Verificar funcionamiento

## 🎯 Aplicación Futura

Para futuros proyectos de dashboard:

1. **Usar esta guía** como referencia
2. **Seguir el proceso** de verificación paso a paso
3. **Verificar siempre** que los archivos HTML estén en el repositorio
4. **Probar GitHub Pages** antes de considerar el proyecto completo

## 🚀 Comando de Verificación Rápida

```bash
# Verificar que el dashboard funcionará
git ls-files | grep html
git check-ignore dashboards/*.html
# Si ambos comandos muestran resultados correctos, el dashboard funcionará
```

---

**Fecha:** Octubre 2025  
**Proyecto:** EEG Wavelets y PSD  
**Autor:** Felipe Rangel  
**Estado:** ✅ Prevención de errores 404 implementada  
**Documentación:** ✅ Completa para futuros proyectos
