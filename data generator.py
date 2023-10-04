import numpy as np
import pandas as pd

# Create a NumPy array of random values for each feature
name = np.random.choice(["Apple", "Banana", "Orange", "Grape", "Strawberry"], size=60)
subtype = np.random.choice(["Fuji", "Gala", "Golden Delicious", "Red Delicious", "Granny Smith"], size=60)
mass = np.random.randint(10, 20, size=60)
width = np.random.randint(1, 5, size=60)
height = np.random.randint(1, 5, size=60)
cscore = np.random.randint(0, 100, size=60)

# Create a pandas DataFrame from the NumPy arrays
df = pd.DataFrame({'name': name, 'subtype': subtype, 'mass': mass, 'width': width, 'height': height, 'cscore': cscore})

# Print the DataFrame
print(df.head())

df.to_csv('fruits_data.csv')
