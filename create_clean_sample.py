import pandas as pd

# Load data
df = pd.read_csv("train.csv")

# Sample the first 10,000 rows
df_clean = df.head(10000).copy()

# Rename columns from Spanish to English
df_clean.rename(columns={
    "Semana": "Week",
    "Agencia_ID": "Agency_ID",
    "Canal_ID": "Channel_ID",
    "Ruta_SAK": "Route_ID",
    "Cliente_ID": "Client_ID",
    "Producto_ID": "Product_ID",
    "Venta_uni_hoy": "Weekly_Units_Sold",
    "Venta_hoy": "Weekly_Sales_Price",
    "Demanda_uni_equil": "Unit_Demand"
}, inplace=True)

# Save to new CSV
df_clean.to_csv("train_clean.csv", index=False)

print("train_clean.csv created with 10,000 rows and renamed columns.")