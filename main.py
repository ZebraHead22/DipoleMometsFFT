import pandas as pd
import numpy as np
import scipy as sc
from matplotlib import pyplot as plt
from scipy import fft

df = pd.read_csv('dipole_gly.dat', sep="\s+", skiprows=1, names=['frame', 'dip_x', 'dip_y', 'dip_z', '|dip|'])
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

y_m = np.mean(y)
y = y - y_m

fft_data = np.abs(sc.fft.rfft(y)) / y.size
fft_freqs = sc.fft.rfftfreq(len(y), d=timeframe)

plt.plot(fft_freqs / (300 * 10 ** 8), fft_data, 'r')
plt.xlabel('Frequency ($cm^{-1}$)')
plt.ylabel('Amplitude (a.u.)')
plt.xlim([0, 6000])
plt.show()

# 2. Сделать окно Хэмминга, например, построить график промежуточный для дипольного момента
# ham = np.bartlett(len(y)) / y.size
# new_y = ham * y
# axis_new_y = sc.fft.rfft(new_y)
# plt.plot(fft_freqs / (300 * 10 ** 8), np.abs(axis_new_y))
# plt.legend(['Without window', 'With window'])
# plt.show()

# 3. Выбор столбца
# axis = input("По какому моменту строим спектр? ('dip_x', 'dip_y', 'dip_z', '|dip|'): ")
# ______________________
# удобная запись в файл, сохранение картинок...и т.п.
