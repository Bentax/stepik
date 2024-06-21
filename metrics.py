import pandas as pd
import numpy as np
from numpy import NaN

# Создадим датафрейм с пропущенным значением признака Р для объекта А
df = pd.DataFrame({'P1':[3,5,4,5], 'P2':[4,5,3,4], 'P3':[5,5,3,3], 'P4':[3,4,2,3], 'P':[4,3,5,NaN]}, index=['A1', 'A2', 'A3', 'A'])

# Посчитаем метрики
dict_metrics = {'A1':[], 'A2':[], 'A3':[]}
for i in df.index[:-1]:
  dict_metrics[i].append(np.power((df.loc['A'][:-1]-df.loc[i][:-1]).pow(2).sum(), 0.5).round(2)) # считаем Евклидово расстояние
  dict_metrics[i].append((df.loc['A'][:-1]-df.loc[i][:-1]).abs().sum()) # считаем Манхэттеновское расстояние
  dict_metrics[i].append((df.loc['A'][:-1]-df.loc[i][:-1]).abs().max()) # считаем max-метрику

metrics = pd.DataFrame(dict_metrics, index=['Euclid', 'Manhatten', 'Max'])

# Считаем варианты значений для каждой метрики
dict_value = {'Euclid':[], 'Manhatten':[], 'Max':[]}
for i in metrics.index:
  norm_mul = (1/((1/metrics.loc[i]).sum())) # нормирующий множитель
  similarity = ((df.loc[:]['P'][:-1]/metrics.loc[i]).sum()) # значение признака * мера близости(=величина, обратно пропорциональная мере расстояния)
  value_P = (norm_mul*similarity).round(2)
  dict_value[i].append(value_P)
  print(f'значение признака P для А по метрике {i}: {value_P}')
# значение признака P для А по метрике Euclid: 4.13
# значение признака P для А по метрике Manhatten: 4.1
# значение признака P для А по метрике Max: 4.25
