import pandas as pd

df = pd.read_csv("data/sales_data.csv", encoding="ISO-8859-1", engine="python")

print(df.head())
print("\nDataset Shape:", df.shape)
print("\nColumns in Dataset:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nSales & Profit Correlation:")
print(df[["Sales", "Profit"]].corr())
print("\nLoss Making Transactions:")
print(df[df["Profit"] < 0].shape[0])
print("\nAverage Profit by Region:")
print(df.groupby("Region")["Profit"].mean().sort_values(ascending=False))
print("\nDiscount vs Profit Correlation:")
print(df[["Discount", "Profit"]].corr())



