import pandas  as pd
import streamlit as st

st.title("Manejo de Dataframes")
st.sidebar.title("Parámetros")


modulo = st.sidebar.selectbox("Seleccione un modulo",["Filtros","Consultas","Agrupaciones","Muestras"])
df = pd.read_csv("Datos/InsuranceCompany.csv")

if modulo == "Filtros":
    
    st.write(df)

    st.write("Columnas del dataframe",df.columns)
    columnas=list(df.columns)

    #FILTRO 1
    st.write("FILTRO 1")
    seleccion_Columna=st.multiselect("Seleccione las columnas",columnas)
    st.write(seleccion_Columna)


    ingreso_indice=st.number_input("Ingrese el valor de índice")
    df_filtro_1=df.loc[int(ingreso_indice),seleccion_Columna]
    st.write(df_filtro_1)

    #FILTRO 2
    st.write("FILTRO 2")

    indice_columna=st.number_input("Ingrese el valor de la columnna")
    indice_fila=st.number_input("Ingrese el valor de la fila")
    df_filtro_2=df.iloc[int(indice_fila),int(indice_columna)]
    st.write(df_filtro_2)

elif modulo == "Consultas":
    st.subheader("modulo consultas    ")
    consulta = st.text_input("Ingrese el query")
    
    try:   
        df_query=df.query(consulta)
        st.write(df_query)
    except:
        st.write("Ingrese e query y presione enter")

    
    coincidencia = st.text_input("Ingrese una coincidencia")
    seleccion_columna1=st.selectbox("Escoja una columna",list(df.columns))
    
    try:   
        df_coincidencia=df[df[seleccion_columna1].str.contains(coincidencia)]
        st.write(df_coincidencia)
    except:
        st.write("Ingrese la coincidencia")

elif modulo == "Agrupaciones":
    st.subheader("> Modulo agrupaciones")
    lista_columnas = list(df.columns)
    lista_columnas_numericas = list(df.select_dtypes(include=['float64','int64']).columns)

    seleccion_columna2=st.multiselect("Escoja una columna",lista_columnas)
    columna_cuantitativa=st.selectbox("Escoja una columna cuantitativa",lista_columnas_numericas)

    df_agrupacion_promedio=df.groupby(seleccion_columna2)[columna_cuantitativa].mean()
    st.write(df_agrupacion_promedio)

elif modulo == "Muestras":
    st.subheader("> Modulo muestras")

    muestra_aleatoria=df.sample(n=int(st.number_input("Ingrese el tamaño de la muestra")),random_state=42)
    st.write(muestra_aleatoria)

    muestra_aleatoria_2=df.sample(frac=float(st.number_input("Ingrese una fraccion")),random_state=42)
    st.write(muestra_aleatoria_2)