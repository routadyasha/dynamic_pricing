import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df_path = os.path.join("data","raw","amazon_smartphones.csv")
df = pd.read_csv(df_path)

print("First 5 rows")
print(df.head())

print("\nData info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Convert price, rating, and reviews to numeric
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["reviews"] = pd.to_numeric(df["reviews"], errors="coerce")

# Drop rows with missing price or rating
df.dropna(subset=["price", "rating"], inplace=True)

# Basic stats
print("\nDescriptive statistics:")
print(df.describe())

# Plot distribution of price
plt.figure(figsize=(10, 5))
sns.histplot(df["price"], bins=30, kde=True)
plt.title("Price Distribution")
plt.xlabel("Price (INR)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Price vs Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="rating", y="price")
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (INR)")
plt.tight_layout()
plt.show()

# Save cleaned version
cleaned_path = os.path.join("data", "processed", "amazon_smartphones_cleaned.csv")
os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
df.to_csv(cleaned_path, index=False)
print(f"\nSaved cleaned data to {cleaned_path}")