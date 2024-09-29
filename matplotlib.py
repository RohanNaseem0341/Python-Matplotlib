import matplotlib.pyplot as plt

import pandas as pd

data=pd.read_csv("data.csv")
plt.plot(data['Duration'],data['Pulse'])
plt.show()