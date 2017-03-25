import pandas as pd

df = pd.read_csv('faculty.csv')
df.iloc[:,-1].to_csv('emails.csv',index=False)
