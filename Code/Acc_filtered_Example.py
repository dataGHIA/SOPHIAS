import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt

# 1️⃣ Cargar CSV y limpiar nombres
df = pd.read_csv("accelerometer.txt")
df.columns = df.columns.str.strip()

# 2️⃣ Extraer señales
X = df["Acelerómetro: x"].values
Y = df["y"].values
Z = df["z"].values
Timestamp = df["Timestamp"].values

# 3️⃣ Convertir timestamps a segundos y empezar en cero
Timestamp = (Timestamp - Timestamp[0]) / 1000.0

# 4️⃣ Calcular frecuencia de muestreo
sample_intervals = np.diff(Timestamp)
Fs = 1 / np.mean(sample_intervals)
print("Calculated sampling frequency:", Fs, "Hz")

# 5️⃣ Opcional: sobrescribir Fs si quieres simular un muestreo más rápido
Fs = 100  # Hz

# 6️⃣ Crear filtro Butterworth 4º orden, cutoff 15 Hz
Fc = 15  # Hz
b, a = butter(4, Fc / (Fs / 2), btype='low')

# 7️⃣ Filtrar las señales con filtfilt
FilteredX_Butterworth = filtfilt(b, a, X)
FilteredY_Butterworth = filtfilt(b, a, Y)
FilteredZ_Butterworth = filtfilt(b, a, Z)

# 8️⃣ Guardar resultados en el dataframe
df["X_filt"] = FilteredX_Butterworth
df["Y_filt"] = FilteredY_Butterworth
df["Z_filt"] = FilteredZ_Butterworth

df.to_csv("accelerometer_filtered.csv", index=False)
