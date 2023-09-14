# -*- coding: UTF-8 -*-
"""
@Project: EEGProcessing_V3 
@File: test_signal_spectrum.py
@IDE: PyCharm 
@Author: Xueqiang Wang
@Date: 2023/9/14 11:56 
@Description:  
"""
from hdf5storage import loadmat
from scipy import signal
import matplotlib.pyplot as plt
# matplotlib.use('QtAgg')


# load data
data = list(loadmat(r'E:\workplace\EEGProcessing\EEG script & dataset\test\BWJ_test_20230830_MICE2.mat').values())
data = data[-1].transpose()[2]
# mini_data = data[:24*305]
F, T, Sxx = signal.spectrogram(data, fs=305, noverlap=0, nperseg=305)


plt.pcolormesh(T, F, Sxx, cmap='jet', vmax=1e-10)
plt.ylim([0, 50])
plt.colorbar()
plt.show()
