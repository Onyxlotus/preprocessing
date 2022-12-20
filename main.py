import pandas as pd

usd_eur_df = pd.read_csv("Dannye_Zadanie.csv", sep=';', on_bad_lines='skip')
print("size: ", usd_eur_df.shape)
usd_eur_df.head(5)

new_columns_name = ['TICKER', 'PER', 'DATE', 'TIME', 'OPEN', 'HIGH', 'LOW', 'CLOSE']
usd_eur_df.set_axis(new_columns_name, axis='columns', inplace=True)
usd_eur_df.head()