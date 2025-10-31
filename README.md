# Car-Recommendation-System
A Machine Learning based Car Recommendation System built using Flask and scikit-learn that suggests the most suitable cars based on user preferences like budget, fuel type, and seating capacity.


# 🚗 Car Recommendation System

A **Content-Based Recommendation System** that helps users find the most suitable cars based on their preferences — like budget, body type, fuel type, transmission, and seating capacity.

This project is built using **Python (Flask)** for backend, **HTML/CSS** for frontend, and **Scikit-learn** for machine learning.

---

## 🧩 Features

✅ User-friendly web interface (HTML + CSS)  
✅ Flask backend to connect UI with ML model  
✅ Car recommendations based on similarity using **K-Nearest Neighbors (KNN)**  
✅ Uses **Cosine Similarity** for accurate matching  
✅ Data preprocessing with **OneHotEncoder** and **MinMaxScaler**  
✅ Dynamic results page displaying top recommended cars  
✅ Duplicate car removal for cleaner results  

---

## ⚙️ Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **ML Libraries:** Pandas, NumPy, Scikit-learn  
- **Algorithm:** K-Nearest Neighbors (KNN) with Cosine Similarity  
- **Dataset:** Cleaned Car Dataset (`cleaned_car_dataset.csv`)

---

## 🚀 How It Works

1. The user enters their preferences (budget, body type, fuel, etc.) on the homepage.  
2. Flask receives the input and sends it to the `recommendation.py` module.  
3. The ML model processes the input using similarity-based search.  
4. The backend returns top car recommendations.  
5. Results are displayed beautifully on the results page.

---

## 📂 Project Structure
Car-Recommendation-System/
│
├── static/
│ ├── style.css # Styling for the frontend
│
├── templates/
│ ├── index.html # Homepage with user form
│ ├── results.html # Recommendation result page
│
├── model/
│ ├── init.py # Model initialization
│ ├── recommendation.py # ML model and logic
│
├── app.py # Flask main file
├── cleaned_car_dataset.csv
├── README.md
└── requirements.txt



---

## 🧠 Machine Learning Overview

This is a **content-based filtering** recommendation system.  
The model uses **K-Nearest Neighbors (KNN)** to find cars that are most similar to the user’s preferences using **cosine similarity**.

### Preprocessing:
- **Categorical features** (Body_Type, Fuel_Type, Transmission) → OneHotEncoded  
- **Numerical features** (Price, Seats, Displacement) → Scaled using MinMaxScaler  

### Model:
- Built using `NearestNeighbors(n_neighbors=7, metric="cosine")`  
- Finds similar cars by comparing feature vectors in multidimensional space.

---

## 🖥️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Car-Recommendation-System.git
   cd Car-Recommendation-System


