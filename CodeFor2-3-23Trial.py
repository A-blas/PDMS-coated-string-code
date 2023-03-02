from matplotlib.image import pil_to_array
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# file = r'PDMS_350mg_3_1 02-3-23 11 41 56 AM\DAQ- Crosshead, … - (Timed).txt'
matches = []
for root, dirs, files in os.walk(r'C:\Users\Alessandra Blasone\OneDrive\Desktop\Code\230203_Sandra_StringTestsInitial_controls-PDMS', topdown=False):
    for filename in files:
        if filename.endswith(('.txt')):
            matches.append(os.path.join(root, filename))

fig, axs = plt.subplots()

color_list = ['#cd6155', '#943126', '#b03a2e', '#cb4335', '#e74c3c', '#21618c', '#2874a6', '#2e86c1', '#3498db', '#5dade2'] 
i = 0

for path in matches:
    df = pd.read_csv(path, skiprows = 6, header= 0, delimiter = '\t')
    df.drop([0], axis = 0, inplace = True)
    df['Load '] = pd.to_numeric(df['Load '], errors = 'coerce')
    df['Strain 1 '] = pd.to_numeric(df['Strain 1 '], errors = 'coerce')
    df['Time '] = pd.to_numeric(df['Time '], errors = 'coerce')
    df.plot(y= 'Load ', x = 'Strain 1 ', kind = 'line', color = color_list[i], ax = axs, label = os.path.basename(os.path.dirname(path)))
    i = i + 1

df.to_excel('excelfolder/test.xlsx')

# for scatter plots add s = {size} for size of dot on plot
# plt.xlabel("Strain")
# plt.ylabel("Stress")
# plt.title("Stress vs Strain in Tensile Testing Machine")

# plt.legend(['Oven 1', 'Oven 2', 'Oven 3', 'Oven 4', 'Oven 5', 'Laser 1', 'Laser 2', 'Laser 3', 'Laser 4', 'Laser 5'])

# plt.show()

