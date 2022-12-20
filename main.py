import pandas as pd
import numpy as np

usd_eur_df = pd.read_csv("Dannye_Zadanie.csv", sep=';', on_bad_lines='skip')
print("size: ", usd_eur_df.shape)
usd_eur_df.head(5)

new_columns_name = ['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']
usd_eur_df.set_axis(new_columns_name, axis='columns', inplace=True)
usd_eur_df.head()

df_numeric = usd_eur_df.select_dtypes(include=[np.number])
print(df_numeric)

usd_eur_df.info()

print('dublicate as: ', usd_eur_df.duplicated().sum())
print(usd_eur_df.duplicated())

usd_eur_df[usd_eur_df.duplicated()]

usd_eur_df = usd_eur_df.drop_duplicates()
usd_eur_df[usd_eur_df.duplicated()]

usd_eur_df.info()
usd_eur_df.loc[:, 'OPEN'] = pd.to_numeric(usd_eur_df.loc[:, 'OPEN'], errors="coerce")
print(usd_eur_df.info())
usd_eur_df.isnull().sum()

usd_eur_df[usd_eur_df.isnull().any(axis=1)]
usd_eur_df = usd_eur_df.fillna(method='bfill')
usd_eur_df.info()
usd_eur_df.head()

usd_eur_df.describe()

usd_eur_df.boxplot(column=['OPEN', 'HIGH', 'LOW', 'CLOSE'])
df_new = usd_eur_df.drop_duplicates(keep='first')

df_new.info()
columns_int64 = df_new.select_dtypes(include=['int64'])
print(columns_int64.dtypes)

columns_float64 = df_new.select_dtypes(include=['float64'])
print(columns_float64.dtypes)

convert_columns_int64 = columns_int64.apply(pd.to_numeric, downcast='integer')
print(convert_columns_int64.dtypes, '\n')
convert_columns_float64 = columns_float64.apply(pd.to_numeric, downcast='float')
print(convert_columns_float64.dtypes)


columns_obj = df_new.select_dtypes(include= ['object'])
columns_obj.describe()

columns_ctg = columns_obj.astype('category')
columns_ctg.info()

df_optim = df_new.copy()
df_optim[columns_ctg.columns] = columns_ctg
df_optim[convert_columns_int64.columns] = convert_columns_int64
df_optim[convert_columns_float64.columns] = convert_columns_float64
df_optim.head()

df_optim.info()

df_date = df_optim['DATE'].copy()
df_date = pd.to_datetime(df_date, format='%y%m%d', utc=False)
print(type(df_date))
print(df_date)

df_optim['DATE'] = df_date
df_optim.info()

df_optim.to_csv('clean_dannye.csv', sep=';', index=False)
