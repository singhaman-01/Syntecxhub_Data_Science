import pandas as pd
print("Pandas Project 2 Started!")
print("Pandas version:",pd.__version__)
df = pd.read_csv("syntecxhub_sales_data_1000.csv")

print("csv file loaded successfully!")
print("number of rows:", len(df))
print("number of columns:", len(df.columns))

#Display first 5 rows
print("\nfirst 5 rows:")
print(df.head())
print("\nlast 5 rows:")
print(df.tail())
print("\ndata types:")
print(df.dtypes)
print("\nSales statistics:")
print("mean Sales:",df["Sales"].mean())
print("median Sales:", df ["Sales"].median())
print("minimum Sales:", df["Sales"].min())
print("maximum Sales:",df["Sales"].max())
print("number of Sales record:",df["Sales"].count())

# Filter high value orders
high_value_orders= df[df["Sales"]>50000]
print("\nhigh-value orders (Sales>50000):")
print(high_value_orders.head(10))
print("\n nunber of high-value orders:", len(high_value_orders))

# Select specific columns
selected_columns= df[["Order_ID","Product","Category","Sales","Profit"]]
print("\nselected columns:")
print(selected_columns.head(10))

#Slice first 10 rows
sliced_data= df.iloc[0:10, 0:5]

print("\nfirst 10 rows and first 5 columns:")
print(sliced_data)

#Save filtered data to csv
high_value_orders.to_csv("high_value_orders.csv", index=False)

#Save selected columns to excel
selected_columns.to_excel("selected_sales_data.xlsx", index=False)
print("\nfiles exported successfully")
