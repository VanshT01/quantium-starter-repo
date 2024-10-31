import pandas as pd

dataframes = []
file_names = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
for file_name in file_names:
    df = pd.read_csv(file_name)
    df = df[df['product'] == "pink morsel"]
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)  # Remove $ sign and convert to float
    df['sales'] = df['quantity'] * df['price']  # Calculate sales
    df = df[['sales', 'date', 'region']]
    dataframes.append(df)
    
final_df = pd.concat(dataframes, ignore_index = True)
final_df.to_csv("formatted_sales_data.csv", index=False)
print(final_df.head)