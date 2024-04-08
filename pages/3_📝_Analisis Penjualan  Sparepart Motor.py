import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.title("📝 Analisis Penjualan Sparepart Motor")

URL2 = '(2)_Data_Cleaned.csv'
df = pd.read_csv(URL2)

# fungsi plot elbow
def plot_elbow(X):
    distortions = []
    K = range(2, 10)
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        distortions.append(kmeans.inertia_)

    fig, ax = plt.subplots()
    ax.plot(K, distortions, 'bx-')
    ax.set_xlabel('Number of Clusters')
    ax.set_ylabel('Distortion')
    ax.set_title('Elbow Method For Optimal k')
    st.pyplot(fig)

# data train kmeans
def train_kmeans(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    return kmeans

# plot clustering
def plot_clusters(data, labels):
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='warehouse', y='quantity', hue=labels, palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Warehouse)')
        ax.set_xlabel('Warehouse')
        ax.set_ylabel('Quantity')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='product_line', y='quantity', hue=labels, palette='viridis', ax=ax)
        ax.set_title('Clustered Data (Product Line)')
        ax.set_xlabel('Product Line')
        ax.set_ylabel('Quantity')
        st.pyplot(fig)

#main
def main():
    st.write("Data Overview:")
    st.write(df.head())

    st.write("Elbow Plot:")
    plot_elbow(df)

    n_clusters = st.sidebar.slider("Select Number of Clusters", 1, 3, 3)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    kmeans_model = train_kmeans(X_scaled, n_clusters)
    cluster_labels = kmeans_model.predict(X_scaled)

    df['Cluster'] = cluster_labels

    st.write("Data with Cluster Labels:")
    st.write(df)

    plot_clusters(df, cluster_labels)
    st.header("Kesimpulan:")
    st.write("""Dapat dilihat sebelumnya pada visualisasi elbow plot di dapatkan hasil bahwa cluster dengan k 3 adalah cluster yang optimal, sehingga data akan optimal jika dibagi kedalam 3 cluster, 
             yaitu 0, 1, dan 2. Sebaran data berdasarkan cluster dapat dilihat melalui scatter plot diatas. Terdapat 2 scatter plot yang membahas cluster data warehouse dengan quantity dan cluster data product
             line dengan quantity. Dapat ditarik kesimpulan bahwa penting dalam manajemen persediaan untuk produk-produk yang menunjukkan tingkat penjualan tinggi di semua kategori, serta penting untuk memastikan 
             ketersediaan yang mencukupi dari produk-produk ini melalui tiap gudang/warehouse untuk mengoptimalkan pendapatan perusahaan. Analisis lebih lanjut terhadap pola penjualan dalam cluster dapat 
             memberikan wawasan tambahan untuk strategi pengelolaan stok yang lebih efektif.""")
    
if __name__ == "__main__":
    main()
