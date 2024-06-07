import pandas as pd

# Pastikan path file benar
file_path_penjualan = "D:/Semester 4/latihan analisis data/penjualan.csv"
file_path_customer = "D:/Semester 4/latihan analisis data/customer.csv"

# Membaca data penjualan dan customer dari file CSV
df_penjualan = pd.read_csv(file_path_penjualan)
df_customer = pd.read_csv(file_path_customer)

# Filter data untuk bulan Mei 2024
df_penjualan['Tanggal'] = pd.to_datetime(df_penjualan['Tanggal'], format='%Y-%m-%d')
df_penjualan_mei = df_penjualan[df_penjualan['Tanggal'].dt.month == 5]

# Hitung piutang dari setiap customer berdasarkan penjualan kredit (nomor faktur tidak kosong)
df_piutang = df_penjualan_mei[df_penjualan_mei['Nomor Faktur'].notnull()]
piutang_per_customer = df_piutang.groupby('Nama Customer')['Total'].sum().reset_index()

# Gabungkan data piutang dengan tabel customer
df_customer = df_customer.rename(columns={'Nama Customer': 'Nama Customer'})
df_saldo_akhir_piutang = pd.merge(df_customer, piutang_per_customer, on='Nama Customer', how='left')

# Isi NaN dengan 0 (untuk customer yang tidak memiliki transaksi penjualan kredit)
df_saldo_akhir_piutang['Total'] = df_saldo_akhir_piutang['Total'].fillna(0)

# Hitung saldo akhir piutang
df_saldo_akhir_piutang['Saldo Akhir Piutang'] = df_saldo_akhir_piutang['Saldo Piutang'] + df_saldo_akhir_piutang['Total']

# Tampilkan hasil
print(df_saldo_akhir_piutang[['Kode Customer', 'Nama Customer', 'Saldo Akhir Piutang']])


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan path file benar
file_path_penjualan = "D:/Semester 4/latihan analisis data/penjualan.csv"
file_path_customer = "D:/Semester 4/latihan analisis data/customer.csv"

# Membaca data penjualan dan customer dari file CSV
df_penjualan = pd.read_csv(file_path_penjualan)
df_customer = pd.read_csv(file_path_customer)

# Filter data untuk bulan Mei 2024
df_penjualan['Tanggal'] = pd.to_datetime(df_penjualan['Tanggal'], format='%Y-%m-%d')
df_penjualan_mei = df_penjualan[df_penjualan['Tanggal'].dt.month == 5]

# Hitung piutang dari setiap customer berdasarkan penjualan kredit (nomor faktur tidak kosong)
df_piutang = df_penjualan_mei[df_penjualan_mei['Nomor Faktur'].notnull()]
piutang_per_customer = df_piutang.groupby('Nama Customer')['Total'].sum().reset_index()

# Gabungkan data piutang dengan tabel customer
df_saldo_akhir_piutang = pd.merge(df_customer, piutang_per_customer, on='Nama Customer', how='left')

# Isi NaN dengan 0 (untuk customer yang tidak memiliki transaksi penjualan kredit)
df_saldo_akhir_piutang['Total'] = df_saldo_akhir_piutang['Total'].fillna(0)

# Hitung saldo akhir piutang
df_saldo_akhir_piutang['Saldo Akhir Piutang'] = df_saldo_akhir_piutang['Saldo Piutang'] + df_saldo_akhir_piutang['Total']

# Tampilkan hasil
print(df_saldo_akhir_piutang[['Kode Customer', 'Nama Customer', 'Saldo Akhir Piutang']])

# Visualisasi hasil analisis dalam bentuk diagram garis
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

# Plotting the line plot
ax = sns.lineplot(
    x='Nama Customer', 
    y='Saldo Akhir Piutang', 
    data=df_saldo_akhir_piutang, 
    marker='o', 
    palette='viridis'
)

# Customizing the plot for better aesthetics
ax.set_title('Saldo Akhir Piutang dari Setiap Customer pada Akhir Bulan Mei 2024', fontsize=16, weight='bold')
ax.set_xlabel('Nama Customer', fontsize=14)
ax.set_ylabel('Saldo Akhir Piutang', fontsize=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Adding value labels
for x, y in zip(df_saldo_akhir_piutang['Nama Customer'], df_saldo_akhir_piutang['Saldo Akhir Piutang']):
    ax.text(x, y, f'{y:.0f}', ha='right', va='bottom', fontsize=10, color='blue')

plt.tight_layout()
plt.show()
