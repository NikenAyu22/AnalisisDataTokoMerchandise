import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan path file benar
file_path = "D:/Semester 4/latihan analisis data/penjualan.csv"

# Membaca data penjualan dari file CSV
df_penjualan = pd.read_csv(file_path)

# Tampilkan beberapa baris pertama untuk memastikan nama kolom benar
print(df_penjualan.head())

# Filter data untuk bulan Mei 2024
df_penjualan['Tanggal'] = pd.to_datetime(df_penjualan['Tanggal'], format='%Y-%m-%d')
df_penjualan_mei = df_penjualan[df_penjualan['Tanggal'].dt.month == 5]

# Hitung total penjualan per kategori barang
try:
    total_penjualan_per_kategori = df_penjualan_mei.groupby('Kategori Barang')['Total'].sum()
except KeyError as e:
    print(f"Error: {e}. Pastikan nama kolom di CSV sesuai.")

# Konversi hasil ke DataFrame untuk memudahkan plotting dengan seaborn
total_penjualan_per_kategori = total_penjualan_per_kategori.reset_index()

# Plot diagram batang menggunakan seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x='Kategori Barang', y='Total', data=total_penjualan_per_kategori, palette='viridis')
plt.title('Total Penjualan per Kategori Barang - Mei 2024', fontsize=16)
plt.xlabel('Kategori Barang', fontsize=14)
plt.ylabel('Total Penjualan (Rp)', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
