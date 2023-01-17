
import pandas as pd
reader = pd.read_csv('my_data.txt')
print(reader.head())

reader["Count_Of_Words1"] = reader['Details'].apply(lambda n : len(n.split()))
print(reader.head())


