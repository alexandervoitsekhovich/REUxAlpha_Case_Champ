import pandas as pd
import matplotlib.pyplot as plt


MGD = pd.read_csv("Market growth dynamics.csv")

months = {
    "Январь": 1,
    "Февраль": 2,
    "Март": 3,
    "Апрель": 4,
    "Май": 5,
    "Июнь": 6,
    "Июль": 7,
    "Август": 8,
    "Сентябрь": 9,
    "Октябрь": 10,
    "Ноябрь": 11,
    "Декабрь": 12
}

MGD["Номер месяца"] = MGD["Месяц"].map(months)
avg_revenue = MGD.groupby("Год")["Объем рынка"].transform("mean")
MGD["Сезонный индекс"] = MGD["Объем рынка"] / avg_revenue
MGD["Номер месяца"] = MGD['Номер месяца'].astype("int64")
MGD['Date'] = pd.to_datetime(MGD['Год'].astype(str) + '-' + MGD['Номер месяца'].astype(str) + '-01')
MGD = MGD.sort_values('Date')

if __name__ == "__main__":
    plt.figure(figsize=(12, 6))
    plt.plot(MGD['Date'], MGD['Объем рынка'], marker='o', color='green', linewidth=2)
    plt.title('Динамика выручки фитнес-индустрии (Янв 2024 - Янв 2026)')
    plt.ylabel('Выручка, руб.')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
