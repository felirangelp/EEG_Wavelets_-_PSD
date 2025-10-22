#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis de Señales EEG usando Transformada Wavelet Discreta y PSD
Proyecto: Transformada Wavelet y PSD en EEG
Autor: Felipe Rangel
"""

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output
import pywt
from scipy import signal
from scipy.fft import fft, fftfreq
import warnings
warnings.filterwarnings('ignore')

class EEGAnalyzer:
    """Clase para análisis de señales EEG usando Wavelets y PSD"""
    
    def __init__(self):
        self.data = {}
        self.fs = None  # Frecuencia de muestreo
        self.wavelet_coeffs = {}
        self.psd_results = {}
        
    def load_mat_files(self, file_paths):
        """Cargar archivos .mat de EEG"""
        print("Cargando archivos EEG...")
        
        for file_path in file_paths:
            try:
                mat_data = sio.loadmat(file_path)
                filename = file_path.split('/')[-1].replace('.mat', '')
                
                # Buscar la señal EEG en el archivo
                for key, value in mat_data.items():
                    if not key.startswith('__') and isinstance(value, np.ndarray):
                        if len(value.shape) == 1:
                            if len(value) > 100:  # Solo señales con más de 100 muestras
                                self.data[filename] = value.flatten()
                                print(f"✓ Cargado {filename}: {len(self.data[filename])} muestras")
                                break
                        elif len(value.shape) == 2:
                            if value.shape[0] == 1 and value.shape[1] > 100:
                                self.data[filename] = value.flatten()
                                print(f"✓ Cargado {filename}: {len(self.data[filename])} muestras")
                                break
                            elif value.shape[1] > value.shape[0] and value.shape[1] > 100:
                                # Asumir que las filas son canales
                                self.data[filename] = value
                                print(f"✓ Cargado {filename}: {value.shape[0]} canales, {value.shape[1]} muestras")
                                break
                
                # Estimar frecuencia de muestreo (típicamente 250-1000 Hz para EEG)
                if filename not in self.data:
                    print(f"⚠️ No se pudo encontrar señal EEG en {filename}")
                else:
                    # Asumir frecuencia de muestreo estándar
                    self.fs = 250  # Hz
                    
            except Exception as e:
                print(f"❌ Error cargando {file_path}: {e}")
    
    def wavelet_decomposition(self, signal_data, wavelet='db4', levels=6):
        """Implementar Transformada Wavelet Discreta"""
        print(f"Aplicando transformada wavelet '{wavelet}' con {levels} niveles...")
        
        # Asegurar que la señal es 1D
        if len(signal_data.shape) > 1:
            signal_data = signal_data[0] if signal_data.shape[0] == 1 else signal_data[:, 0]
        
        # Descomposición wavelet
        coeffs = pywt.wavedec(signal_data, wavelet, level=levels)
        
        # Separar coeficientes de aproximación y detalle
        cA = coeffs[0]  # Coeficiente de aproximación
        cD = coeffs[1:]  # Coeficientes de detalle
        
        # Reconstruir cada nivel usando upcoef
        reconstructed_levels = []
        
        # Reconstruir aproximación
        recon_approx = pywt.upcoef('a', cA, wavelet, level=levels)
        reconstructed_levels.append(recon_approx)
        
        # Reconstruir cada nivel de detalle
        for i, cD_level in enumerate(cD):
            recon_signal = pywt.upcoef('d', cD_level, wavelet, level=i+1)
            reconstructed_levels.append(recon_signal)
        
        self.wavelet_coeffs[wavelet] = {
            'coeffs': coeffs,
            'reconstructed': reconstructed_levels,
            'levels': levels
        }
        
        return coeffs, reconstructed_levels
    
    def calculate_central_frequencies(self, wavelet='db4', fs=250):
        """Calcular frecuencias centrales de cada nivel de descomposición"""
        print(f"Calculando frecuencias centrales para wavelet '{wavelet}'...")
        
        if wavelet not in self.wavelet_coeffs:
            print("❌ Primero debe realizar la descomposición wavelet")
            return None
        
        levels = self.wavelet_coeffs[wavelet]['levels']
        freqs = {}
        
        # Frecuencia central de la wavelet madre
        central_freq = pywt.central_frequency(wavelet)
        
        for level in range(1, levels + 1):
            # Calcular frecuencia central para cada nivel
            freq = central_freq * fs / (2 ** level)
            freqs[f'D{level}'] = freq
            
        # Frecuencia de aproximación (nivel más bajo)
        freq_approx = central_freq * fs / (2 ** levels)
        freqs['A'] = freq_approx
        
        self.wavelet_coeffs[wavelet]['frequencies'] = freqs
        
        print("Frecuencias centrales calculadas:")
        for level, freq in freqs.items():
            print(f"  {level}: {freq:.2f} Hz")
        
        return freqs
    
    def welch_psd(self, signal_data, fs=250, window='hann', nperseg=None, noverlap=None):
        """Implementar estimación PSD con método Welch"""
        print(f"Calculando PSD con método Welch (ventana: {window})...")
        
        # Asegurar que la señal es 1D
        if len(signal_data.shape) > 1:
            signal_data = signal_data[0] if signal_data.shape[0] == 1 else signal_data[:, 0]
        
        # Parámetros por defecto
        if nperseg is None:
            nperseg = min(len(signal_data) // 4, 1024)
        if noverlap is None:
            noverlap = nperseg // 2
        
        # Calcular PSD con Welch
        freqs, psd = signal.welch(signal_data, fs=fs, window=window, 
                                nperseg=nperseg, noverlap=noverlap)
        
        self.psd_results['welch'] = {
            'frequencies': freqs,
            'psd': psd,
            'window': window,
            'nperseg': nperseg,
            'noverlap': noverlap
        }
        
        return freqs, psd
    
    def fft_psd(self, signal_data, fs=250):
        """Calcular PSD usando FFT"""
        print("Calculando PSD con FFT...")
        
        # Asegurar que la señal es 1D
        if len(signal_data.shape) > 1:
            signal_data = signal_data[0] if signal_data.shape[0] == 1 else signal_data[:, 0]
        
        # Calcular FFT
        fft_values = fft(signal_data)
        freqs = fftfreq(len(signal_data), 1/fs)
        
        # Calcular PSD
        psd = np.abs(fft_values) ** 2 / len(signal_data)
        
        # Solo frecuencias positivas
        positive_freqs = freqs[:len(freqs)//2]
        positive_psd = psd[:len(psd)//2]
        
        self.psd_results['fft'] = {
            'frequencies': positive_freqs,
            'psd': positive_psd
        }
        
        return positive_freqs, positive_psd
    
    def compare_psd_methods(self, signal_data, fs=250):
        """Comparar métodos PSD (Welch vs FFT)"""
        print("Comparando métodos PSD...")
        
        # Calcular ambos métodos
        welch_freqs, welch_psd = self.welch_psd(signal_data, fs)
        fft_freqs, fft_psd = self.fft_psd(signal_data, fs)
        
        return {
            'welch': (welch_freqs, welch_psd),
            'fft': (fft_freqs, fft_psd)
        }
    
    def create_plots(self, signal_name, wavelet='db4'):
        """Crear gráficos para visualización"""
        if signal_name not in self.data:
            print(f"❌ Señal '{signal_name}' no encontrada")
            return None
        
        signal_data = self.data[signal_name]
        
        # Crear subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=[
                f'Señal EEG Original - {signal_name}',
                'Descomposición Wavelet',
                'PSD - Método Welch',
                'PSD - Comparación Welch vs FFT',
                'Frecuencias Centrales por Nivel',
                'Coeficientes Wavelet'
            ],
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Señal original
        time_axis = np.arange(len(signal_data)) / self.fs
        fig.add_trace(
            go.Scatter(x=time_axis, y=signal_data, name='Señal Original'),
            row=1, col=1
        )
        
        # Descomposición wavelet
        if wavelet in self.wavelet_coeffs:
            reconstructed = self.wavelet_coeffs[wavelet]['reconstructed']
            colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink']
            
            for i, recon in enumerate(reconstructed):
                fig.add_trace(
                    go.Scatter(x=time_axis, y=recon, 
                             name=f'Nivel {i}', line=dict(color=colors[i % len(colors)])),
                    row=1, col=2
                )
        
        # PSD Welch
        if 'welch' in self.psd_results:
            welch_freqs, welch_psd = self.psd_results['welch']['frequencies'], self.psd_results['welch']['psd']
            fig.add_trace(
                go.Scatter(x=welch_freqs, y=welch_psd, name='Welch PSD'),
                row=2, col=1
            )
        
        # Comparación PSD
        if 'welch' in self.psd_results and 'fft' in self.psd_results:
            welch_freqs, welch_psd = self.psd_results['welch']['frequencies'], self.psd_results['welch']['psd']
            fft_freqs, fft_psd = self.psd_results['fft']['frequencies'], self.psd_results['fft']['psd']
            
            fig.add_trace(
                go.Scatter(x=welch_freqs, y=welch_psd, name='Welch'),
                row=2, col=2
            )
            fig.add_trace(
                go.Scatter(x=fft_freqs, y=fft_psd, name='FFT'),
                row=2, col=2
            )
        
        # Frecuencias centrales
        if wavelet in self.wavelet_coeffs and 'frequencies' in self.wavelet_coeffs[wavelet]:
            freqs = self.wavelet_coeffs[wavelet]['frequencies']
            levels = list(freqs.keys())
            freq_values = list(freqs.values())
            
            fig.add_trace(
                go.Bar(x=levels, y=freq_values, name='Frecuencias Centrales'),
                row=3, col=1
            )
        
        # Coeficientes wavelet
        if wavelet in self.wavelet_coeffs:
            coeffs = self.wavelet_coeffs[wavelet]['coeffs']
            coeff_lengths = [len(c) for c in coeffs]
            
            fig.add_trace(
                go.Bar(x=[f'Nivel {i}' for i in range(len(coeff_lengths))], 
                      y=coeff_lengths, name='Longitud Coeficientes'),
                row=3, col=2
            )
        
        # Actualizar layout
        fig.update_layout(
            height=1200,
            title_text=f"Análisis Completo de EEG - {signal_name}",
            showlegend=True
        )
        
        # Actualizar ejes
        fig.update_xaxes(title_text="Tiempo (s)", row=1, col=1)
        fig.update_yaxes(title_text="Amplitud", row=1, col=1)
        fig.update_xaxes(title_text="Tiempo (s)", row=1, col=2)
        fig.update_yaxes(title_text="Amplitud", row=1, col=2)
        fig.update_xaxes(title_text="Frecuencia (Hz)", row=2, col=1)
        fig.update_yaxes(title_text="PSD", row=2, col=1)
        fig.update_xaxes(title_text="Frecuencia (Hz)", row=2, col=2)
        fig.update_yaxes(title_text="PSD", row=2, col=2)
        fig.update_xaxes(title_text="Nivel", row=3, col=1)
        fig.update_yaxes(title_text="Frecuencia (Hz)", row=3, col=1)
        fig.update_xaxes(title_text="Nivel", row=3, col=2)
        fig.update_yaxes(title_text="Longitud", row=3, col=2)
        
        return fig

def main():
    """Función principal"""
    print("=== Análisis de Señales EEG con Wavelets y PSD ===\n")
    
    # Crear analizador
    analyzer = EEGAnalyzer()
    
    # Cargar archivos (rutas relativas al directorio raíz del proyecto)
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_paths = [
        os.path.join(project_root, "sEEG.mat"),
        os.path.join(project_root, "FileEEG.mat")
    ]
    
    analyzer.load_mat_files(file_paths)
    
    if not analyzer.data:
        print("❌ No se pudieron cargar archivos EEG")
        return
    
    # Procesar cada señal
    for signal_name, signal_data in analyzer.data.items():
        print(f"\n--- Procesando {signal_name} ---")
        
        # Transformada Wavelet
        coeffs, reconstructed = analyzer.wavelet_decomposition(signal_data, wavelet='db4', levels=6)
        
        # Frecuencias centrales
        freqs = analyzer.calculate_central_frequencies('db4', analyzer.fs)
        
        # PSD
        analyzer.compare_psd_methods(signal_data, analyzer.fs)
        
        # Crear gráficos
        fig = analyzer.create_plots(signal_name, 'db4')
        
        if fig:
            # Guardar como HTML en el directorio dashboards
            import os
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            dashboards_dir = os.path.join(project_root, "dashboards")
            os.makedirs(dashboards_dir, exist_ok=True)
            output_file = os.path.join(dashboards_dir, f"{signal_name}_analysis.html")
            fig.write_html(output_file)
            print(f"✓ Gráficos guardados en: {output_file}")
    
    print("\n=== Análisis completado ===")

if __name__ == "__main__":
    main()
