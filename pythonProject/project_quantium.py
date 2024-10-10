import pandas as pd

data_0 = pd.read_csv("data/daily_sales_data_0.csv")
data_1 = pd.read_csv("data/daily_sales_data_1.csv")
data_2 = pd.read_csv("data/daily_sales_data_2.csv")

# Filter for "pink morsel" products only
pink_morsel_data_0 = data_0[data_0['product'] == 'pink morsel']
pink_morsel_data_1 = data_1[data_1['product'] == 'pink morsel']
pink_morsel_data_2 = data_2[data_2['product'] == 'pink morsel']

# Convert price to float and remove '$' sign
pink_morsel_data_0['price'] = pink_morsel_data_0['price'].replace({'\$': ''}, regex=True).astype(float)
pink_morsel_data_1['price'] = pink_morsel_data_1['price'].replace({'\$': ''}, regex=True).astype(float)
pink_morsel_data_2['price'] = pink_morsel_data_2['price'].replace({'\$': ''}, regex=True).astype(float)

# Calculate sales as price * quantity
pink_morsel_data_0['sales'] = pink_morsel_data_0['price'] * pink_morsel_data_0['quantity']
pink_morsel_data_1['sales'] = pink_morsel_data_1['price'] * pink_morsel_data_1['quantity']
pink_morsel_data_2['sales'] = pink_morsel_data_2['price'] * pink_morsel_data_2['quantity']

# Select only the required columns: Sales, Date, Region
formatted_data_0 = pink_morsel_data_0[['sales', 'date', 'region']]
formatted_data_1 = pink_morsel_data_1[['sales', 'date', 'region']]
formatted_data_2 = pink_morsel_data_2[['sales', 'date', 'region']]

# Concatenate the dataframes
formatted_data = pd.concat([formatted_data_0, formatted_data_1, formatted_data_2])

print(formatted_data.head())
#End of code