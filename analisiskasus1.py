import pandas as pd
import matplotlib.pyplot as plt

# Load sales and inventory data
sales_df = pd.read_csv('d:/Semester 4/latihan analisis data/penjualan.csv')
inventory_df = pd.read_csv('d:/Semester 4/latihan analisis data/persediaan.csv')

# Step 1: Mengidentifikasi Barang Terlaris
# Calculate total sales per item
total_sales_per_item = sales_df.groupby(['Nama Barang', 'Kategori Barang']).agg({'Jumlah Terjual': 'sum', 'Total': 'sum'}).reset_index()

# Identify the best-selling items
top_selling_items = total_sales_per_item.sort_values(by='Jumlah Terjual', ascending=False).head(5)

# Plotting Pie Chart for top selling items
plt.figure(figsize=(10, 7))

# Pie chart for total sales of top-selling items
plt.pie(top_selling_items['Jumlah Terjual'], labels=top_selling_items['Nama Barang'], autopct='%1.1f%%', startangle=140)

# Adding title
plt.title('Proporsi Penjualan Barang Terlaris')

plt.show()
