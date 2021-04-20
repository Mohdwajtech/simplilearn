import pandas as pd

dataframe = pd.read_csv('SalaryGender.csv')
dataframe.to_csv('changedSalaryGender.csv',index=False)

print(dataframe)