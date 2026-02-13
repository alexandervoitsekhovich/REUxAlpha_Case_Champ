import pandas as pd

df = pd.read_csv("TA datasheet.csv")
stats = df.set_index("Показатель")["Значение"]

avg_entry_cost = stats["Общий объем инвестиций"] / stats["Чистый прирост объектов (всего)"]
LTV = stats["Объем рынка (выручка)"] / stats["Количество клиентов"]
area_per_client = stats["Общая площадь"] / stats["Количество клиентов"]
large_club_ratio = stats["Чистый прирост (Клубы >500 кв.м)"] / stats["Чистый прирост объектов (всего)"] * 100
main_stakeholder_market_share = stats['Общий объем инвестиций'] * stats["Доля DDX Fitness в инвестициях"] / 100


if __name__ == "__main__":
    print(stats, '\n')
    print(f"Среднее вложение для новой точки: {avg_entry_cost} рублей")
    print(f"LTV: {LTV} рублей")
    print(f"Площадь на 1 клиента (кв. метры): {area_per_client}")
    print(f"Доля крупных клубов: {large_club_ratio}%")
    print(f"Инвестиции DDX: {main_stakeholder_market_share}")
    print(f"Инвестиции Остальных: {stats["Общий объем инвестиций"] - main_stakeholder_market_share}")
