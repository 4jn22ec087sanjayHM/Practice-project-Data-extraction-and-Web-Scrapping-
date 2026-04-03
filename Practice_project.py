import numpy as np
import pandas as pd

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# URL of archived Wikipedia page
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Read all tables from the webpage
tables = pd.read_html(URL)

# ✅ Select the correct table manually (this is the correct index)
df = tables[3]

# Reset column headers to simple numeric values
df.columns = range(df.shape[1])

# Keep only required columns:
# Column 0 → Country
# Column 2 → GDP (IMF estimates)
df = df[[0, 2]]

# Remove rows with missing values
df = df.dropna()

# Rename columns
df.columns = ["Country", "GDP (Million USD)"]

# Remove commas from GDP values and convert to numeric
df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(str).str.replace(",", "")
df["GDP (Million USD)"] = pd.to_numeric(df["GDP (Million USD)"], errors="coerce")

# Drop invalid rows
df = df.dropna()

# Keep top 10 economies
df = df.head(10)

# Convert GDP from Million USD to Billion USD
df["GDP (Million USD)"] = df["GDP (Million USD)"] / 1000

# Round values to 2 decimal places
df["GDP (Million USD)"] = np.round(df["GDP (Million USD)"], 2)

# Rename column
df.rename(columns={"GDP (Million USD)": "GDP (Billion USD)"}, inplace=True)

# Save to CSV file
df.to_csv("Largest_economies.csv", index=False)

# Display final DataFrame
print(df)