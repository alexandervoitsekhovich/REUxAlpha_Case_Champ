import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from TA_analysis import area_per_client


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
MGD["Площадь на человека"] = area_per_client / MGD["Сезонный индекс"]
pt = MGD.pivot(index="Год", columns="Месяц", values="Площадь на человека")
pt = pt[months.keys()]

if __name__ == "__main__":
    plt.figure(figsize=(12, 5))
    sb.heatmap(pt, annot=True, fmt=".2f")
    plt.title('Сезонные коэффициенты рынка (0.9 = среднее)')
    plt.show()
