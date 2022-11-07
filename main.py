import pandas as pd
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

df = pd.read_csv('dipole.dat', sep="\s+", skiprows=1, names=['frame', 'dip_x', 'dip_y', 'dip_z', '|dip|'])
# timeframe = input("Укажите время разделения фреймов: ")
# timeframe = float(timeframe)
timeframe = 5 * 10 ** -15
df.insert(1, "time", df['frame'] * timeframe)
print(df)
# 1. Попробовать построить спектр без выбора столбца (пересчет фреймов во время, 1 фр = 5 фс, -15 степень)
axis = '|dip|'
y = np.array(df[axis])
x = np.array(df['time'])
plt.scatter(x, y, c='deeppink')
plt.xlabel('time')
plt.ylabel('dip')
plt.show()

axis_y = sc.fft.rfft(y)
# n = y.size
axis_x = sc.fft.rfftfreq(len(axis_y), timeframe)
r = axis_x > 0
r = r / 0.03
plt.plot(ax, abs(axis_y), 'r')
# plt.xlim(0, 0.25 * 10 ** -16)
plt.xlabel('Freq')
plt.ylabel('Amplitude')

# 2. Сделать окно Хэмминга, например, построить график промежуточный для дипольного момента
ham = np.hamming(len(axis_y))
new_y = y * ham
axis_new_y = sc.rfft.fft(new_y)
plt.plot(r, np.abs(axis_new_y))
plt.show()

# 3. Выбор столбца
# axis = input("По какому моменту строим спектр? ('dip_x', 'dip_y', 'dip_z', '|dip|'): ")
# ______________________
# удобная запись в файл, сохранение картинок...и т.п.
