import joblib
import pandas as pd
from sklearn.datasets import fetch_kddcup99
from sklearn.ensemble import RandomForestClassifier

print("1/3. Descargando dataset oficial KDD Cup 99 (10% subset)...")
# percent10=True descarga exactamente el subconjunto oficial del 10%
kdd_data = fetch_kddcup99(percent10=True, as_frame=True)
df = kdd_data.frame

# En KDD Cup '99 hay 41 columnas de entrada (3 categóricas y 38 numéricas) + label
# Descartamos las 3 categóricas ('protocol_type', 'service', 'flag') y la columna 'labels'
columnas_no_numericas = ['protocol_type', 'service', 'flag', 'labels']
cols_numericas = [c for c in df.columns if c not in columnas_no_numericas]

# Convertimos explícitamente a float para garantizar las 38 características numéricas exactas
X = df[cols_numericas].astype(float)

# Etiqueta binaria: 0 = tráfico normal, 1 = intrusión / ataque
y = df['labels'].apply(lambda val: 0 if 'normal' in str(val) else 1).astype(int)

# Tomamos 60,000 registros para un entrenamiento rápido (10-15 seg) y estadísticamente representativo
X_train = X.iloc[:60000]
y_train = y.iloc[:60000]

print(f"Dimensiones de entrenamiento: {X_train.shape} (esperado: 38 columnas)")

print("2/3. Entrenando RandomForestClassifier con datos oficiales...")
rf = RandomForestClassifier(n_estimators=30, max_depth=12, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

print("3/3. Guardando model.pkl para producción...")
joblib.dump(rf, 'model.pkl')
print("=== ENTRENAMIENTO FINALIZADO CON EXITO ===")