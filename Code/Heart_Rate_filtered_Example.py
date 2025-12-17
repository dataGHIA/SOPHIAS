import pandas as pd

# Cargar CSV
df = pd.read_csv("heartrate.txt")

# Asegurar que Heart Rate es numérico
df[" Heart Rate"] = pd.to_numeric(df[" Heart Rate"], errors="coerce")

# Aplicar filtrado con ventana de 15 muestras (media móvil)
df["HR_filtered"] = df[" Heart Rate"].rolling(window=15).mean()

df.to_csv("heartrate_filtered.csv", index=False)