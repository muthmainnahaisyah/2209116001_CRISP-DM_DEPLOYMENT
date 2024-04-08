import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.sidebar.success("Select a page above.")

def main():
    st.write("""
    # Welcome to Dashboard Penjualan Produk Sparepart Motor 👋
    Dashboard ini memungkinkan Anda untuk melihat hasil analisis dari data penjualan produk sparepart motor.
    Dengan dibuatnya dashboard ini, Anda dapat:
    - Melihat vasualisasi yang insighful dari data penjualan produk sparepart motor.
    - Melihat hasil analisis penjualan produk parepart motor dengan membaginya ke dalam beberapa cluster/kelompok.

    ## Daftar Menu
    1. 📊 Visualisasi Data
    2. 📝 Analisis Penjualan Sparepart Motor

    """)

    st.write("""
    ## Data Penjualan Produk Sparepart Motor
    Berikut adalah data dari penjualan produk sparepart motor:
    
    """)

    URL1 = '(1)_sales_data.csv'

    df = pd.read_csv(URL1)
    st.write(df)

if __name__ == "__main__":
    main()