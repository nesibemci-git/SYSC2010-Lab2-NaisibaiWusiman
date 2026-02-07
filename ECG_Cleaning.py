
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
#import Lab2_ecg.csv


#plotting t and lead_I from Lab2_ecg.csv
df = pd.read_csv('Lab2_ecg.csv')
plt.plot(df['t'], df['lead_I'])
plt.xlabel('t')
plt.ylabel('lead')
plt.title('t vs lead')
plt.show()

# subset
subset = df[(df['t'] > 0) & (df['t'] <= 1000)]
plt.plot(subset['t'], subset['lead_I'])
plt.xlabel('t')
plt.ylabel('lead')
plt.title('subset t vs lead')
plt.show()

# Subtract the mean (remove DC offset)
# Convert to numpy array
lead_I = np.array(df['lead_I'])
t = np.array(df['t'])

# Subtract the mean using numpy
mean_value = np.mean(lead_I)
lead_I_corrected = lead_I - mean_value
plt.plot(t, lead_I_corrected)
plt.xlabel('t') 
plt.ylabel('lead_I_corrected')
plt.title('t vs lead_I corrected')  
plt.show()

#smoothed data
signal = np.convolve(lead_I,np.ones(7)/7,mode='same')
plt.plot(t, signal)
plt.xlabel('t') 
plt.ylabel('smoothed lead_I')
plt.title('t vs smoothed lead_I')  
plt.show()

# first 500 of smooted lead_I and unsmoothed lead_I
plt.plot(t[:500], signal[:500], label='Smoothed lead_I')
plt.plot(t[:500], lead_I[:500], label='Original lead_I')
plt.xlabel('t') 
plt.ylabel('lead_I')
plt.title('t vs lead_I (first 500 samples)')
plt.legend()
plt.show()

# Creating cleaned data 
cleaned_df = pd.DataFrame({
    'time': t,
    'ecg': signal
})

cleaned_df.to_csv('processed_ecg.csv', index=False)