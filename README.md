# 🎮 Predicción de éxito global de videojuegos con FastAPI

Este proyecto implementa el despliegue de un modelo de clasificación para predecir si un videojuego será un **éxito global** (ventas superiores a 30 millones de unidades) usando datos del histórico `vgsales.csv`.

## 📌 Descripción General

- **Modelo:** RandomForestClassifier
- **API:** FastAPI + Uvicorn
- **Dataset:** Información de videojuegos (año, género, plataforma, ventas por región)
- **Objetivo:** Exponer el modelo como un servicio web accesible a través de una API REST

## 📁 Estructura del Proyecto

```
├── entrenar_modelo_vgsales.py      # Script para entrenamiento del modelo
├── main.py                         # API REST en FastAPI
├── modelo_vgsales.pkl              # Modelo entrenado
├── columnas_vgsales.pkl            # Lista de columnas del modelo
├── requirements.txt                # Dependencias del proyecto
├── vgsales.csv                     # Dataset del proyecto
```

## ⚙️ Requisitos

```bash
pip install -r requirements.txt
```

## 🚀 Entrenamiento del Modelo

```bash
python entrenar_modelo_vgsales.py
```

Esto genera dos archivos:

- `modelo_vgsales.pkl`: modelo entrenado
- `columnas_vgsales.pkl`: columnas utilizadas como entrada

## 🖥️ Ejecución del API

```bash
uvicorn main:app --reload
```

Una vez en ejecución, visita:

- Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Endpoint principal: `POST /predict`

## 📥 Ejemplo de Entrada

```json
{
  "Year": 2009,
  "Genre": "Sports",
  "Platform": "Wii",
  "NA_Sales": 15.75,
  "EU_Sales": 11.01,
  "JP_Sales": 3.28,
  "Other_Sales": 2.96
}
```

## ✅ Respuesta esperada

```json
{
  "exito_global": true
}
```

## 📄 Descripciones de Archivos

- **`entrenar_modelo_vgsales.py`**: Entrena y guarda el modelo de clasificación.
- **`main.py`**: Implementa la API REST con FastAPI para realizar predicciones.
- **`requirements.txt`**: Lista de librerías necesarias.
- **`modelo_vgsales.pkl`**: Modelo entrenado con Random Forest.
- **`columnas_vgsales.pkl`**: Columnas del dataset utilizadas durante el entrenamiento.

## ✍️ Autor

DavidTs - Proyecto para la Especialización en Analítica de Datos para la Toma de Decisiones

---

_Repositorio generado como parte de un ejercicio práctico de despliegue de modelos con FastAPI._
