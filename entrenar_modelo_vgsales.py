import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar el archivo CSV
df = pd.read_csv("vgsales.csv")

# Crear variable objetivo
df["exito_global"] = (df["Global_Sales"] > 30).astype(int)

# Seleccionar características
features = ["Year", "Genre", "Platform", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
df = df[features + ["exito_global"]]

#Eliminar datos nulos del dataset
df.dropna(inplace=True)

# Codificar variables categóricas
df = pd.get_dummies(df, columns=["Genre", "Platform"], drop_first=True)

# Dividir datos
X = df.drop("exito_global", axis=1)
y = df["exito_global"]

# Entrenar modelo
modelo = RandomForestClassifier()
modelo.fit(X, y)

# Guardar modelo y columnas
joblib.dump(modelo, "modelo_vgsales.pkl")
joblib.dump(X.columns.tolist(), "columnas_vgsales.pkl")

print("Modelo entrenado con vgsales y guardado.")
