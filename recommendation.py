import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv("cleaned_car_dataset.csv")

# Select relevant columns
selected_cols = [
    "Make", "Model", "Ex-Showroom_Price", "Body_Type", "Fuel_Type",
    "Type", "Seating_Capacity", "Displacement", "Number_of_Airbags"
]
cars_df = df[selected_cols].dropna().reset_index(drop=True)

# Define categorical and numerical features
cat_features = ["Body_Type", "Fuel_Type", "Type"]
num_features = ["Ex-Showroom_Price", "Seating_Capacity", "Displacement", "Number_of_Airbags"]

# Encode and scale
ohe = OneHotEncoder(handle_unknown="ignore")
scaler = MinMaxScaler()

cat_encoded = ohe.fit_transform(cars_df[cat_features])
num_scaled = scaler.fit_transform(cars_df[num_features])
X = np.hstack((num_scaled, cat_encoded.toarray()))

# Build recommender model
model = NearestNeighbors(n_neighbors=30, metric="cosine")
model.fit(X)

def recommend_cars(budget_min=None, budget_max=None,
                   body=None, fuel=None, transmission=None,
                   seats=None, top_n=7):
    query = {
        "Body_Type": body or "SUV",
        "Fuel_Type": fuel or "Petrol",
        "Type": transmission or "Manual",
        "Seating_Capacity": float(seats) if seats else 5.0,
        "Ex-Showroom_Price": float((budget_min or 500000) + (budget_max or 2000000)) / 2,
        "Displacement": cars_df["Displacement"].median(),
        "Number_of_Airbags": cars_df["Number_of_Airbags"].median()
    }

    # Scale numeric features
    num_vals = np.array([
        query["Ex-Showroom_Price"], query["Seating_Capacity"],
        query["Displacement"], query["Number_of_Airbags"]
    ]).reshape(1, -1)
    num_scaled = scaler.transform(num_vals)

    # Encode categorical features
    cat_df = pd.DataFrame([[query["Body_Type"], query["Fuel_Type"], query["Type"]]],
                          columns=cat_features)
    cat_encoded = ohe.transform(cat_df)
    query_vec = np.hstack((num_scaled, cat_encoded.toarray()))

    # Get nearest neighbors
    distances, indices = model.kneighbors(query_vec, n_neighbors=30)
    results = cars_df.iloc[indices[0]].copy()
    results["Similarity"] = 1 - distances[0]

    # Sort by similarity
    results = results.sort_values(by="Similarity", ascending=False)

    # Remove duplicate Make + Model
    results = results.drop_duplicates(subset=["Make", "Model"])

    # Get top N unique recommendations
    recommendations = results.head(top_n).reset_index(drop=True)
    return recommendations


if __name__ == "__main__":
    cars = recommend_cars(
        budget_min=800000,
        budget_max=1500000,
        body="SUV",
        fuel="Petrol",
        transmission="Automatic",
        seats=5
    )
    print(cars)
