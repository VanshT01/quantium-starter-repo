import pandas as pd
dataframes = [] # Array of dataframes
file_names = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv'] # Array of file names
for file_name in file_names:
    df = pd.read_csv(file_name) # create a dataframe df to read the csv file
    df = df[df['product'] == "pink morsel"] # Filter out the rows to those with "pink morsel"
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)  # Remove $ sign and convert to float
    df['sales'] = df['quantity'] * df['price']  # Calculate sales
    df = df[['sales', 'date', 'region']] # Clean the data to filter out all columns except sales, date and region
    dataframes.append(df) # Append the dataframe of this csv file to the array of all dataframes 

final_df = pd.concat(dataframes, ignore_index = True) # Concatenate all elements of dataframes into a final one
final_df.to_csv("formatted_sales_data.csv", index=False) # Save dataframe in a new file
