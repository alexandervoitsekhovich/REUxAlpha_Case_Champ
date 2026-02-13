import pandas as pd
import matplotlib.pyplot as plt
from area_visuals import MGD, months
from TA_analysis import area_per_client
import seaborn as sb

df = pd.read_csv("TA datasheet.csv")
stats = df.set_index("Показатель")["Значение"]

monthly_profile = MGD.groupby("Месяц")["Сезонный индекс"].mean()
awaited_revenue_monthly = stats["Прогноз (базовый)"] / 12

comfort_limit = 1.5

forecast_2026 = (monthly_profile * awaited_revenue_monthly).reindex(list(months.keys()))
predicted_density = area_per_client / monthly_profile.reindex(list(months.keys()))

plot_data = pd.DataFrame({
    'Месяц': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    'Плотность': predicted_density.values
})

sb.set_theme(style="whitegrid")
plt.figure(figsize=(14, 8))

line_plot = sb.lineplot(
    data=plot_data,
    x='Месяц',
    y='Плотность',
    marker='o',
    linewidth=4,
    color='#2c3e50',
    markersize=10
)

plt.axhspan(0, 0.9, color='#e74c3c', alpha=0.3, label='Критично (Меньше 0.9 м²)') # Красный
plt.axhspan(0.9, 1.0, color='#f1c40f', alpha=0.3, label='Тесно (0.9 - 1.0 м²)')   # Желтый
plt.axhspan(1.0, 1.5, color='#2ecc71', alpha=0.3, label='Комфорт (Выше 1.0 м²)')    # Зеленый

plt.title('Прогноз плотности в залах на 2026 год\n(м² на 1 активного клиента)', fontsize=18, pad=20)
plt.ylabel('Свободное пространство (м²)', fontsize=14)
plt.xlabel(None)
plt.ylim(0.5, 1.4)

plt.legend(loc='upper right', frameon=True, shadow=True)
sb.despine(left=True, bottom=True)

plt.show()
