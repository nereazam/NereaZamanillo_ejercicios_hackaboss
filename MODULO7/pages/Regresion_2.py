import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Cargar el conjunto de datos
@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

df = load_dataset()

# Preprocesar los datos
X = df.drop(columns=['price'])
y = df['price']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un pipeline de regresión
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Entrenar el modelo
pipeline.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(pipeline, 'models/pipeline_regresion.joblib')

# Realizar predicciones sobre el conjunto de prueba
y_pred = pipeline.predict(X_test)

# Evaluar el modelo
st.header("Evaluación del Modelo de Regresión")
st.write(f"R2 Score: {r2_score(y_test, y_pred)}")
st.write(f"MAE: {mean_absolute_error(y_test, y_pred)}")
st.write(f"MSE: {mean_squared_error(y_test, y_pred)}")
st.write(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False)}")

# Predicción de un nuevo dato
st.header("Predicción de Precio de Diamante")
carat = st.number_input("Carat:", min_value=0.2, max_value=5.0, value=1.0)
depth = st.number_input("Depth:", min_value=40.0, max_value=80.0, value=60.0)
table = st.number_input("Table:", min_value=50.0, max_value=70.0, value=60.0)
color = st.selectbox("Color:", options=df['color'].unique())
cut = st.selectbox("Cut:", options=df['cut'].unique())
clarity = st.selectbox("Clarity:", options=df['clarity'].unique())

# Crear un DataFrame para el nuevo dato
input_data = pd.DataFrame([[carat, depth, table, color, cut, clarity]], columns=X.columns)
input_pred = pipeline.predict(input_data)
st.write(f"Predicción del Precio: {input_pred[0]}")
