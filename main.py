import scipy.io as scio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath1 = "C:/Users/haobin/Desktop/individual/wykht8y7tg-1/Panasonic 18650PF Data/Panasonic 18650PF Data/25degC/5 pulse disch/03-11-17_08.47 25degC_5Pulse_HPPC_Pan18650PF.mat"
data_25degc=scio.loadmat(filepath1)
filepath2= "C:/Users/haobin/Desktop/individual/wykht8y7tg-1/Panasonic 18650PF Data/-20degC/5 pulse disch/06-15-17_11.31 n20degC_5Pulse_HPPC_Pan18650PF.mat"
data_n20degc=scio.loadmat(filepath2)
filepath3="C:/Users/haobin/Desktop/individual/wykht8y7tg-1/Panasonic 18650PF Data/0degC/5 pulse/05-20-17_10.44 0degC_5pulse_HPPC_Pan18650PF.mat"
data_0degc=scio.loadmat(filepath3)
list=['TimeStamp', 'Voltage', 'Current', 'Ah', 'Wh', 'Power', 'Battery_Temp_degC','Time','Chamber_Temp_degC']
data_25degc=data_25degc['meas']
data_25degc_len = np.arange(len(data_25degc[0,0][list[3]]))
data_Ah1 = data_25degc[0, 0][list[3]]
data_25degc_voltage = data_25degc[0, 0][list[1]]
max_values = max(abs(data_Ah1))
data_Ah_process1 = (max_values+data_Ah1)/max_values
data_25degc_Ah=data_Ah_process1.flatten()

data_n20degc=data_n20degc['meas']
data_n20degc_len = np.arange(len(data_n20degc[0,0][list[3]]))
data_Ah2 = data_n20degc[0, 0][list[3]]
data_n20degc_voltage = data_n20degc[0, 0][list[1]]
max_values = max(abs(data_Ah2))
data_Ah_process2 = (max_values+data_Ah2)/max_values
data_n20degc_Ah=data_Ah_process2.flatten()

data_0degc=data_0degc['meas']
data_0degc_len = np.arange(len(data_0degc[0,0][list[3]]))
data_Ah3 = data_0degc[0, 0][list[3]]
data_0degc_voltage = data_0degc[0, 0][list[1]]
max_values = max(abs(data_Ah3))
data_Ah_process3 = (max_values+data_Ah3)/max_values
data_0degc_Ah=data_Ah_process3.flatten()
fig, ax = plt.subplots()
#ax.plot(data_25degc_len, data_Ah,label = list[3]+'25degc')
ax.plot(data_Ah_process1 ,data_25degc_voltage ,label = '25degc_OCV vs SOC')
ax.plot(data_Ah_process2 ,data_n20degc_voltage ,label = '-20degc_OCV vs SOC')
ax.plot(data_Ah_process3 ,data_0degc_voltage ,label = '0degc_OCV vs SOC')
ax.legend()
ax.set(xlabel='SOC percentage', ylabel='OCV (v)',
        title='SOC vs OCV at25° and -20° and 0° at discharge')
def to_percent(temp, position):
  return '%1.0f'%(100*temp) + '%'
plt.gca().xaxis.set_major_formatter((to_percent))

ax.grid()

plt.show()