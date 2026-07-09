# 🎓 Student Performance Prediction System

A Machine Learning web application developed using **Python**, **Scikit-learn**, and **Streamlit** to predict students' final academic performance (G3).

---

## 📌 Project Overview

This project predicts a student's final grade using demographic, family, academic, and lifestyle information.

A **Random Forest Regressor** model was trained using the Student Performance Dataset and deployed through a Streamlit web application.

---

## 🎯 Objectives

- Explore and analyze the dataset using Exploratory Data Analysis (EDA)
- Preprocess and encode categorical variables
- Train a Random Forest Regression model
- Evaluate model performance
- Save the trained model
- Build a Streamlit application for real-time predictions

---

## 📂 Dataset

**Dataset:** Student Performance Dataset

The dataset contains student demographic, family, social, and academic information used to predict the final grade (G3).

Target Variable:

- G3 (Final Grade)

Features include:

- School
- Gender
- Age
- Family Information
- Study Time
- Previous Grades
- Internet Access
- Health
- Alcohol Consumption
- Absences
- And many more...

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook

---

## 🤖 Machine Learning Model

Algorithm Used:

**Random Forest Regressor**

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── student.csv
│
├── models/
│   ├── student_performance_model.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   └── Student_Performance_Prediction.ipynb
│
├── screenshots/
│
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Student-Performance-Prediction.git
```

Go to the project folder

```bash
cd Student-Performance-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
cd app
streamlit run app.py
```

---

## 📊 Model Workflow

1. Load Dataset
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Encoding
5. Train/Test Split
6. Train Random Forest Model
7. Evaluate Model
8. Save Trained Model
9. Build Streamlit Application
10. Predict Student Performance

---

## 📷 Screenshots

Add screenshots of:

- Dataset Preview
- EDA Charts
- Model Evaluation
- Streamlit Home Page
- Prediction Result

Example:

```
screenshots/
    home.png
    prediction.png
    evaluation.png
```

---

## 📈 Results

The Random Forest model achieved good predictive performance and can accurately estimate the final student grade (G3).

---

## 👨‍💻 Author

**Sahan Perera**

COM763 Machine Learning Coursework

---

## 📄 License

This project was developed for educational purposes only.
# Student-Performance-Prediction
Machine Learning project to predict student performance using Random Forest and Streamlit.
