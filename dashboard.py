import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from area_predict_2026 import predicted_density


st.set_page_config(page_title="Фитнесс-индустрия анализ 2026", layout="wide")
st.title("Состояние и боли фитнес-индустрии")


@st.cache_data
def load_data():
    df1 = pd.read_csv("TA datasheet.csv")

    df2 = pd.read_csv("Market growth dynamics.csv")
    return df1, df2


TA, MGD = load_data()
stats = TA.set_index("Показатель")["Значение"].to_dict()

st.sidebar.header("Настройки комфорта")
comfort_threshold = st.sidebar.slider(
    "Порог комфорта (м² на чел.)",
    min_value=0.5, max_value=2.0, value=1.0, step=0.1
)
st.sidebar.info(f"Вы установили стандарт: {comfort_threshold} м² на клиента.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Объем рынка 2026", f"{stats['Прогноз (базовый)']/1e9:.1f} млрд ₽", "+12%",
              "orange", delta_arrow="down")
with col2:
    st.metric("Средний LTV", f"{stats['Объем рынка (выручка)']/stats['Количество клиентов']:,.0f} ₽")
with col3:
    st.metric("Доминирование DDX", f"{stats['Доля DDX Fitness в инвестициях']:.0f}%")
with col4:
    st.metric("Средняя плотность", "0.9 м²", "Критично мало", "red", delta_arrow="off")

st.subheader("Прогноз тесноты по месяцам на 2026 год")
months = {
    'Январь': 1,
    'Февраль': 2,
    'Март': 3,
    'Апрель': 4,
    'Май': 5,
    'Июнь': 6,
    'Июль': 7,
    'Август': 8,
    'Сентябрь': 9,
    'Октябрь': 10,
    'Ноябрь': 11,
    'Декабрь': 12
}
avg_rev = MGD.groupby('Год')['Объем рынка'].transform('mean')
MGD['Seasonal_Index'] = MGD['Объем рынка'] / avg_rev
seasonal_profile = MGD.groupby('Месяц')['Seasonal_Index'].mean().reindex(list(months.keys()))

fig, ax = plt.subplots(figsize=(12, 5))
sb.lineplot(x=seasonal_profile.index, y=predicted_density, marker='o', linewidth=3, ax=ax, color='#2c3e50')
ax.axhline(comfort_threshold, color='red', linestyle='--', label=f'Ваш порог: {comfort_threshold}')
ax.fill_between(seasonal_profile.index, 0, comfort_threshold, color='red', alpha=0.1)
plt.xticks(rotation=45)
plt.legend()
st.pyplot(fig)

st.warning(f"В месяцах, где график ниже линии {comfort_threshold}, бизнес теряет лояльность клиентов из-за тесноты.")
