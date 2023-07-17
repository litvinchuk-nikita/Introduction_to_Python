"""
Задача No57. Решение в группах
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_test.csv')

df.shape

df.dtypes

"""Задача No59. Решение в группах
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""

df.columns

df.isnull().sum()

df[df['median_income'] < 20]['median_house_value']

df[['longitude', 'latitude']]

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

"""Задача N61. Решение в группах
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value
"""

print(df['median_house_value'].max(), df['median_house_value'].min())

df[df['median_income'] == 3.1250]['median_house_value'].max()

df[df['median_house_value'] == df['median_house_value'].min()]['population'].max()
