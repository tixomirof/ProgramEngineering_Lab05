import streamlit as st
import pandas as pd

def getData():
    return pd.read_csv("https://huggingface.co/datasets/ankislyakov/titanic/resolve/main/titanic_train.csv")

def filterData(data, selected_age_category):
    if selected_age_category == 'Молодой':
        filtered_df = data[data['Age'] < 30]
    elif selected_age_category == 'Среднего возраста':
        filtered_df = data[(data['Age'] >= 30) & (data['Age'] < 60)]
    else:
        filtered_df = data[data['Age'] >= 60]
    return filtered_df

st.title("Программная инженерия: лабораторная работа №3")
st.header("Вариант-11 (Тихомиров Алексей)")

st.write("Исходная таблица данных:")
df = getData()
st.dataframe(df)

age_category = st.selectbox(
    "Выберите возрастную категорию:",
    ('Молодой', 'Среднего возраста', 'Старый')
)

filtered_df = filterData(df, age_category)

if not filtered_df.empty:
    survival_rate = filtered_df['Survived'].mean()
    st.write(f"Доля спасенных: {survival_rate:.2%}")
    st.write(f"Доля погибших: {1 - survival_rate:.2%}")
else:
    st.write("Нет данных для выбранной категории")

st.dataframe(filtered_df)