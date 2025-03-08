import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title='Análisis Exploratorio de Diamantes', page_icon=':gem:')

# Título
st.title('Análisis Exploratorio de Datos de Diamantes')
st.write("Este es un análisis detallado del conjunto de datos de diamantes, usando técnicas de filtrado, visualización y estadísticas.")

# Cargar el conjunto de datos
@st.cache_resource
def load_dataset():
    url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv'
    return pd.read_csv(url)

df = load_dataset()

# Mostrar datos originales
st.header('Datos Originales')
st.dataframe(df)

# Filtros de datos
st.header('Filtros Globales')

# Filtros categóricos
st.subheader('Filtros Categóricos')
color = df['color'].unique()
selected_color = st.multiselect('Selecciona el color de diamantes', options=color, default=color)

cut = df['cut'].unique()
selected_cut = st.multiselect('Selecciona el tipo de corte', options=cut, default=cut)

clarity = df['clarity'].unique()
selected_clarity = st.multiselect('Selecciona la claridad', options=clarity, default=clarity)

# Filtros numéricos
st.subheader('Filtros Numéricos')

# Rango de precio
price_min, price_max = st.slider(
    'Selecciona el rango de precio',
    min_value=df['price'].min(),
    max_value=df['price'].max(),
    value=(df['price'].min(), df['price'].max())
)

# Rango de peso (carat)
carat_min, carat_max = st.slider(
    'Selecciona el rango de peso (carat)',
    min_value=df['carat'].min(),
    max_value=df['carat'].max(),
    value=(df['carat'].min(), df['carat'].max())
)

# Rango de profundidad (depth)
depth_min, depth_max = st.slider(
    'Selecciona el rango de profundidad',
    min_value=df['depth'].min(),
    max_value=df['depth'].max(),
    value=(df['depth'].min(), df['depth'].max())
)

# Rango de tabla (table)
table_min, table_max = st.slider(
    'Selecciona el rango de tabla',
    min_value=df['table'].min(),
    max_value=df['table'].max(),
    value=(df['table'].min(), df['table'].max())
)

# Filtrar datos
df_filtered = df[ 
    (df['cut'].isin(selected_cut)) & 
    (df['color'].isin(selected_color)) & 
    (df['clarity'].isin(selected_clarity)) & 
    (df['price'] >= price_min) & (df['price'] <= price_max) & 
    (df['carat'] >= carat_min) & (df['carat'] <= carat_max) & 
    (df['depth'] >= depth_min) & (df['depth'] <= depth_max) & 
    (df['table'] >= table_min) & (df['table'] <= table_max) 
]

# Mostrar datos filtrados
st.subheader('Datos Filtrados')
st.dataframe(df_filtered)

# Estadísticas antes y después del filtrado
st.write(f'Número de filas antes del filtrado: **{df.shape[0]}**')
st.write(f'Número de filas después del filtrado: **{df_filtered.shape[0]}**')
st.write(f'Número de filas eliminadas: **{df.shape[0] - df_filtered.shape[0]}**')

# Gráficos con Matplotlib
st.header('Gráficos con Matplotlib')

# Histograma de precios
st.subheader('Histograma de Precios')
fig, ax = plt.subplots(figsize=(10,6))
ax.hist(df_filtered['price'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma de Precios de Diamantes')
ax.set_xlabel('Precio')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

# Boxplot de precios
st.subheader('Boxplot de Precios')
fig, ax = plt.subplots(figsize=(10,6))
ax.boxplot(df_filtered['price'], showmeans=True)
ax.set_title('Boxplot de Precios')
ax.set_ylabel('Precio')
st.pyplot(fig)

# Gráfico de dispersión: precio vs. carat
st.subheader('Gráfico de Dispersión: Precio vs. Peso (Carat)')
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df_filtered['carat'], df_filtered['price'], alpha=0.5)
ax.set_title('Relación entre Precio y Peso (Carat)')
ax.set_xlabel('Peso (Carat)')
ax.set_ylabel('Precio')
st.pyplot(fig)

# Gráficos con Seaborn
st.header('Gráficos con Seaborn')

# KDE plot de precios
st.subheader('KDE Plot de Precios')
fig, ax = plt.subplots(figsize=(10,6))
sns.kdeplot(df_filtered['price'], shade=True, color='purple', ax=ax)
ax.set_title('Distribución de Precios (Kernel Density Estimation)')
ax.set_xlabel('Precio')
ax.set_ylabel('Densidad')
st.pyplot(fig)

# Heatmap de correlaciones
st.subheader('Mapa de Calor de Correlaciones')
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df_filtered.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Mapa de Calor de Correlaciones')
st.pyplot(fig)

# Gráficos con Plotly
st.header('Gráficos Interactivos con Plotly')

# Gráfico de barras: Precio vs. Carat (promedio por precio)
df_grouped = df_filtered.groupby('price', as_index=False)['carat'].mean()
fig = px.bar(df_grouped, x='price', y='carat', color='price', title='Precio Promedio por Peso (Carat)')
st.plotly_chart(fig)

# Gráfico de dispersión interactivo
st.subheader('Gráfico de Dispersión Interactivo: Precio vs. Profundidad')
fig = px.scatter(df_filtered, x='depth', y='price', color='cut', title='Relación entre Precio y Profundidad')
st.plotly_chart(fig)

# Gráfico facetado de corte
st.subheader('Gráfico Facetado de Corte')
fig = px.scatter(df_filtered, x='depth', y='table', color='price', facet_col='cut', opacity=0.7)
st.plotly_chart(fig)

# Opción para descargar datos
st.header('Descargar Datos')
st.write('Puedes descargar los datos filtrados o el dataset original.')

col1, col2 = st.columns(2)

# Descargar datos originales
with col1:
    st.download_button(
        'Descargar Datos Originales',
        data=df.to_csv(index=False),
        file_name='diamonds_original.csv',
        mime='text/csv'
    )

# Descargar datos filtrados
with col2:
    st.download_button(
        'Descargar Datos Filtrados',
        data=df_filtered.to_csv(index=False),
        file_name='diamonds_filtered.csv',
        mime='text/csv'
    )
