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


