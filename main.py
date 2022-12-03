import pandas as pd
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

df = pd.read_csv('dipole.dat', sep="\s+", skiprows=1, names=['frame', 'dip_x', 'dip_y', 'dip_z', '|dip|'])
# timeframe = input("Укажите время разделения фреймов: ")
# timeframe = float(timeframe)
timeframe = 5 * 10 ** -15
df.insert(1, "time", df['frame'] * timeframe)
# 1. Попробовать построить спектр без выбора столбца (пересчет фреймов во время, 1 фр = 5 фс, -15 степень)
axis = '|dip|'
y = np.array(df[axis])
x = np.array(df['time'])
plt.plot(x, y, c='r')
plt.xlabel('time')
plt.ylabel('dip')
plt.show()
fs = 1 / timeframe # частота дискретизаци, задается пользователем на основе снятых данных
window = sc.signal.windows.chebwin(4096, 45)

f, SPM = sc.signal.welch(y, fs, window, 4096) # построение СПМ с использованием окна,
# на выбор какого, использую окно Чебышева степени 3/2
f_true = f / (300 * 10 ** 8) # перевод частот в волновое число, для удобства
plt.semilogy(f_true, SPM)
plt.xlim(0, 6000) # в каком дипазоне частот строить график
plt.xlabel('Частота [cm^-1]')
plt.ylabel('СПМ')
plt.grid()
plt.show()

f1, SPM1 = sc.signal.welch(y, fs, 'boxcar', 1000) # СПМ без окон
f_true1 = f1 / (300 * 10 ** 8)
plt.semilogy(f_true1, SPM1)
plt.xlim(0, 6000)
plt.xlabel('Частота [cm^-1]')
plt.ylabel('СПМ')
plt.grid()
plt.show()

# 2. Сделать окно Хэмминга, например, построить график промежуточный для дипольного момента

# 3. Выбор столбца
# axis = input("По какому моменту строим спектр? ('dip_x', 'dip_y', 'dip_z', '|dip|'): ")
# ______________________
# удобная запись в файл, сохранение картинок...и т.п.
