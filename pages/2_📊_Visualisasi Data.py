import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.title("📊 Visualisasi Data")

URL1 = '(1)_sales_data.csv'
df = pd.read_csv(URL1)

# sidebar
def sidebar():
    st.sidebar.title("Choose Visualization")
    page = st.sidebar.radio("Select Visualization", ["Composition","Relationship","Comparison","Distribution"])
    return page

# composition warehouse
def warehouse():
    colors = ['#ff6666', '#bfbfbf', '#f0f0f0']
    visual_warehouse = df['warehouse'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    visual_warehouse.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors, ax=ax)
    st.pyplot(fig)

def main_warehouse():
    warehouse()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Berdasarkan hasil komposisi warehouse, dapat dilihat bahwa Central mendominasi kontribusi
                terbesar dengan 48% dari total penjualan, menunjukkan signifikansi strategis gudang tersebut 
                dalam rantai pasokan. Meskipun North memiliki kontribusi yang cukup besar dengan 34%, ada potensi 
                untuk pertumbuhan lebih lanjut. Sementara itu, West memiliki kontribusi yang lebih rendah sebesar 
                18%, menandakan adanya tantangan atau peluang untuk memperbaiki kinerja di wilayah tersebut.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Untuk meningkatkan penjualan, strategi pemasaran dan distribusi dapat dioptimalkan dengan 
                fokus pada wilayah Central, evaluasi lebih lanjut terhadap wilayah North untuk mengidentifikasi 
                peluang pertumbuhan, dan analisis mendalam terhadap kinerja wilayah West untuk menyelesaikan 
                hambatan yang ada.""")

# composition client_type
def client_type():
    colors = ['#1e90ff', '#bfbfbf']
    visual_client_type = df['client_type'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    visual_client_type.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors, ax=ax)
    st.pyplot(fig)

def main_client_type():
    client_type()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Berdasarkan hasil komposisi client type mayoritas penjualan (77.5%) berasal dari pelanggan ritel, 
             sedangkan hanya 22.5% dari penjualan berasal dari pelanggan grosir. Hal ini menunjukkan kecenderungan 
             bisnis lebih bergantung pada penjualan langsung kepada konsumen akhir daripada penjualan dalam jumlah 
             besar kepada pihak grosir.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Mengoptimalkan strategi pemasaran dan layanan pelanggan untuk menarik lebih banyak konsumen ritel. 
             Ini bisa melibatkan penawaran promosi khusus, meningkatkan kualitas layanan, atau memperluas jaringan 
             penjualan ritel. Selain itu, perlu dilakukan evaluasi strategi untuk menarik lebih banyak pelanggan 
             grosir atau meningkatkan kerjasama dengan distributor grosir.""")

# composition product_line
def product():
    colors = ['#bfbfbf', '#FF1493', '#bfbfbf', '#bfbfbf', '#bfbfbf', '#bfbfbf' ]
    fig = px.bar(df, y="product_line", color="product_line", color_discrete_sequence=colors)
    fig.update_layout(title="Product Line")
    st.plotly_chart(fig)


def main_product():
    product()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Produk dalam kategori breaking system memiliki kontribusi penjualan tertinggi sebesar, 
             diikuti oleh suspension & traction dan electrical system. Sementara itu, penjualan 
             produk frame & body, miscellaneous, dan engine memiliki kontribusi yang lebih rendah.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Strategi stok dapat dioptimalkan dengan meningkatkan ketersediaan produk-produk dalam kategori breaking system, 
             suspension & traction, dan electrical system untuk memenuhi permintaan yang tinggi tersebut. Promosi khusus atau diskon 
             dapat diberikan untuk produk-produk dalam kategori-kategori ini guna meningkatkan penjualan lebih lanjut. Sementara 
             itu, evaluasi strategi pemasaran dan penjualan perlu dilakukan untuk produk-produk dalam kategori frame & body, miscellaneous, 
             dan engine yang memiliki kontribusi penjualan lebih rendah, dengan tujuan mengidentifikasi faktor-faktor yang memengaruhi 
             penjualan dan meningkatkan kinerja produk-produk tersebut.""")

# composition payment
def payment():
    colors = ['#cccc00', '#bfbfbf', '#f0f0f0']
    visual_payment = df['payment'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    visual_payment.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors, ax=ax)
    st.pyplot(fig)

def main_payment():
    payment()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Mayoritas transaksi (65.9%) dilakukan menggunakan kartu kredit, sementara persentase kecil 
             transaksi (11.6%) menggunakan pembayaran tunai, dan sekitar 22.5% menggunakan transfer bank. 
             Hal ini mengindikasikan preferensi dominan pelanggan untuk menggunakan kartu kredit sebagai 
             metode pembayaran, kemungkinan karena kenyamanan dan keamanan yang ditawarkan oleh metode tersebut.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Mengintegrasikan sistem pembayaran digital atau layanan pembayaran online lainnya dapat memberikan 
             fleksibilitas kepada pelanggan dan meningkatkan kemudahan dalam bertransaksi. Selain itu, memberikan 
             insentif khusus untuk penggunaan metode pembayaran alternatif seperti tunai atau transfer bank dapat 
             merangsang penggunaan metode pembayaran yang lebih beragam, sehingga mengurangi ketergantungan pada kartu kredit.""")

# relationship antara quantity dengan harga produk
def quantity_price(df):
    sns.catplot(data=df, x="quantity", y="unit_price", kind="point", errorbar=None)
    plt.title("Hubungan antara harga produk dengan quantity produk")
    fig = plt.gcf()
    return fig

def main_quantity_price():
    fig = quantity_price(df)
    st.pyplot(fig)
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Grafik menunjukkan bahwa tidak ada hubungan yang jelas antara harga produk dan jumlah penjualan. Hal ini menunjukkan 
             bahwa faktor-faktor lain mungkin mempengaruhi jumlah penjualan.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Melakukan identifikasi faktor-faktor lain yang memengaruhi penjualan, seperti promosi atau persediaan di toko, serta 
             memahami preferensi pelanggan untuk mengkustomisasi strategi pemasaran.""")

# relationship antara quantity dengan total
def quantity_total(df):
    sns.catplot(data=df, x="quantity", y="total", kind="point", errorbar=None)
    plt.title("Hubungan antara quantity produk dengan total harga")
    fig = plt.gcf()
    return fig

def main_quantity_total():
    fig = quantity_total(df)
    st.pyplot(fig)
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Grafik menunjukkan adanya hubungan positif antara jumlah produk yang dibeli oleh pelanggan (quantity) dan total harga yang 
             dibayarkan. Artinya, semakin banyak produk yang dibeli, semakin besar total harga yang dibayarkan. Sebaliknya, semakin sedikit 
             produk yang dibeli, semakin kecil total harga yang dibayarkan.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Menawarkan paket penjualan atau diskon untuk pembelian dalam jumlah besar untuk mendorong peningkatan quantity pembelian dan 
             memperhatikan pengaturan harga dengan mempertimbangkan faktor kuantitas pembelian pelanggan.""")

# comparison client type dengan product line
def client_product():
    fig = px.histogram(df, y="client_type", color="product_line", barmode="group")

    fig.update_layout(
        title="Perbandingan pembelian produk berdasarkan tipe pembeli",
        xaxis_title="Frekuensi",
        yaxis_title="Client_Type"
    )

    st.plotly_chart(fig)

def main_client_product():
    client_product()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Frekuensi pembelian produk oleh pelanggan retail lebih tinggi daripada pelanggan wholesale untuk semua jenis produk. Ini mengindikasikan 
             bahwa pelanggan retail cenderung membeli produk secara lebih sering daripada pelanggan wholesale. Meskipun frekuensi pembelian oleh pelanggan 
             wholesale relatif rendah, namun mereka cenderung membeli dalam jumlah besar.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Mengembangkan strategi pemasaran yang berbeda untuk menargetkan pelanggan retail yang cenderung membeli produk secara sering, dan strategi 
             yang berbeda lagi untuk menarik pelanggan wholesale yang cenderung membeli dalam jumlah besar.""")

# distribution quantity
def quantity():
    fig, ax = plt.subplots()
    sns.histplot(df["quantity"], kde=True, ax=ax)
    ax.axvline(df["quantity"].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    ax.axvline(df["quantity"].median(), color='blue', linestyle='dashed', linewidth=1, label='Median')
    ax.set_title("Distribution of Quantity")
    ax.legend()

    st.pyplot(fig)

def main_quantity():
    quantity()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Visualisasi menunjukkan bahwa puncak kurva distribusi data berada lebih ke kiri dari nilai median, dan nilai median berada lebih ke kiri dari nilai mean. 
             Hal ini mengindikasikan bahwa distribusi data tidak mengikuti pola lonceng sempurna atau distribusi normal. Lebih banyak data terkonsentrasi di sisi kiri 
             grafik, menunjukkan bahwa lebih banyak pembelian dilakukan dengan jumlah kecil dibandingkan dengan pembelian dengan jumlah besar.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Melakukan analisis lebih lanjut untuk memahami faktor-faktor yang mempengaruhi pembelian dalam jumlah kecil dan besar, seperti preferensi produk, tren pasar, 
             dan perilaku konsumen, untuk mengoptimalkan strategi penjualan dan pemasaran, serta mengelola persediaan dengan memperhatikan bahwa lebih banyak pembelian 
             dilakukan dengan jumlah kecil dan mengoptimalkan stok untuk mengakomodasi permintaan yang lebih tinggi dari pembelian kecil ini.""")

# distribution unit price
def unit_price():
    fig, ax = plt.subplots()
    sns.histplot(df["unit_price"], kde=True, ax=ax)
    ax.axvline(df["unit_price"].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    ax.axvline(df["unit_price"].median(), color='blue', linestyle='dashed', linewidth=1, label='Median')
    ax.set_title("Distribution of Unit Price")
    ax.legend()

    st.pyplot(fig)

def main_unit_price():
    unit_price()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Visualisasi menunjukkan bahwa puncak kurva distribusi data berada lebih ke kiri dari nilai median, dan nilai median berada lebih ke kiri dari nilai mean. Hal ini 
             mengindikasikan bahwa distribusi data tidak mengikuti pola lonceng sempurna atau distribusi normal. Lebih banyak data terkonsentrasi di sisi kiri grafik, menunjukkan 
             bahwa lebih banyak produk yang ditawarkan dengan harga yang lebih kecil dibandingkan dengan produk yang ditawarkan dengan harga yang lebih besar.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Melakukan pemetaan ulang portofolio produk untuk memastikan adanya variasi harga yang cukup untuk memenuhi kebutuhan dan preferensi pelanggan yang beragam. Menawarkan 
             produk dengan berbagai kisaran harga dapat membantu menjangkau berbagai segmen pasar dengan lebih baik.""")

# distribution total
def total():
    fig, ax = plt.subplots()
    sns.histplot(df["total"], kde=True, ax=ax)
    ax.axvline(df["total"].mean(), color='red', linestyle='dashed', linewidth=1, label='Mean')
    ax.axvline(df["total"].median(), color='blue', linestyle='dashed', linewidth=1, label='Median')
    ax.set_title("Distribution of Total")
    ax.legend()

    st.pyplot(fig)

def main_total():
    total()
    # interpretasi
    st.subheader("Interpretasi:")
    st.write("""Visualisasi menunjukkan bahwa puncak kurva distribusi data berada lebih ke kiri dari nilai median, dan nilai median berada lebih ke kiri dari nilai mean. Hal ini mengindikasikan 
             bahwa distribusi data tidak mengikuti pola lonceng sempurna atau distribusi normal. Lebih banyak data terkonsentrasi di sisi kiri grafik, menunjukkan bahwa lebih banyak pembelian 
             dengan total bayar yang kecil dibandingkan dengan pembelian dengan total bayar yang besar.""")
    # actionable insight
    st.subheader("Actionable Insight:")
    st.write("""Melakukan segmentasi pelanggan berdasarkan total bayar pembelian mereka untuk memahami lebih dalam preferensi dan kebutuhan mereka. Dengan demikian, dapat dirancang strategi pemasaran 
             yang lebih terarah dan efektif sesuai dengan kebutuhan setiap segmen pelanggan.""")

# main
def main():
    page = sidebar()

    if page == "Composition":
        st.write("""## Composition""")
        selected_chart = st.selectbox("Select Composition", ["Warehouse","Client Type","Product Line","Payment"])
        if selected_chart == "Warehouse":
            main_warehouse()
        elif selected_chart == "Client Type":
            main_client_type()
        elif selected_chart == "Product Line":
            main_product()
        elif selected_chart == "Payment":
            main_payment()

    elif page == "Relationship":
        st.write("""## Relationship""")
        selected_chart = st.selectbox("Select Relationship", ["Relationship quantity with unit price","Relationship quantity with total"])
        if selected_chart == "Relationship quantity with unit price":
            main_quantity_price()
        elif selected_chart == "Relationship quantity with total":
            main_quantity_total()

    elif page == "Comparison":
        st.write("""## Comparison""")
        selected_chart = st.selectbox("Select Comparison", ["Comparison Client Type with Product Line"])
        if selected_chart == "Comparison Client Type with Product Line":
            main_client_product()
    
    elif page == "Distribution":
        st.write("""## Distribution""")
        selected_chart = st.selectbox("Select Distribution", ["Quantity","Unit Price","Total"])
        if selected_chart == "Quantity":
            main_quantity()
        elif selected_chart == "Unit Price":
            main_unit_price()
        elif selected_chart == "Total":
            main_total()

if __name__ == "__main__":
    main()
