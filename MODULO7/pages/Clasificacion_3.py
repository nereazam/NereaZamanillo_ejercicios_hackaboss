import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar el conjunto de datos
@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

df = load_dataset()

# Preprocesar los datos para clasificación
X = df.drop(columns=['price'])
y = df['cut']  # Variable objetivo: 'cut'

# Convertir variables categóricas a variables dummy
X = pd.get_dummies(X, drop_first=True)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de clasificación
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
clf.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

# Evaluar el modelo
st.header("Evaluación del Modelo de Clasificación")
st.write(f"Accuracy Score: {accuracy_score(y_test, y_pred)}")
st.write(classification_report(y_test, y_pred))
