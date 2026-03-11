import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Karthi_001@localhost:5432/online_retail")

df = pd.read_sql("SELECT * FROM customer_features", engine)

df["clv_score"] = df["frequency"] * df["avg_order_value"]

# Segment customers
features = df[[
    "recency",
    "frequency",
    "monetary",
    "avg_order_value",
    "t"
]]
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia)
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

kmeans = KMeans(n_clusters=4, random_state=42)
df["cluster"] = kmeans.fit_predict(scaled_features)

cluster_summary = df.groupby("cluster")[[
    "recency",
    "frequency",
    "monetary",
    "avg_order_value",
    "t"
]].mean()

print(cluster_summary)

cluster_names = {
    0: "VIP",
    1: "Loyal",
    2: "Mid Value",
    3: "At Risk"
}

df["segment"] = df["cluster"].map(cluster_names)


# Save results
df.to_csv(r"D:/CLV suite/data/processed/customer_segments.csv", index=False)
