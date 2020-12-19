import pandas as pd 
import os

file_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(file_path, 'data.xlsx')
df = pd.read_excel(base_path)
print(df)
