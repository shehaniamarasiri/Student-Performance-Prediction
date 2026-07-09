import streamlit as st
import pandas as pd
import joblib
import os


# Load Model


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(
    os.path.join(BASE_DIR, "models", "student_performance_model.pkl")
)

feature_names = joblib.load(
    os.path.join(BASE_DIR, "models", "feature_names.pkl")
)


st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)


# Sidebar


st.sidebar.title("🎓 Student Performance")

st.sidebar.markdown("---")

st.sidebar.subheader("Model Performance")

st.sidebar.metric("R² Score", "0.84")
st.sidebar.metric("MAE", "0.84")
st.sidebar.metric("RMSE", "1.18")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Machine Learning Model

Random Forest Regressor

Dataset:
Student Performance Dataset
"""
)


# Title


st.title("🎓 Student Performance Prediction")

st.write(
"""
Predict a student's final grade (G3) using a trained
Random Forest Machine Learning model.
"""
)

st.markdown("---")


# Student Information

st.header("👨‍🎓 Student Information")

col1, col2 = st.columns(2)

with col1:

    school = st.selectbox(
        "School",
        ["GP", "MS"]
    )

    sex = st.selectbox(
        "Gender",
        ["F", "M"]
    )

    age = st.slider(
        "Age",
        15,
        22,
        17
    )

    address = st.selectbox(
        "Address",
        ["R", "U"]
    )

    famsize = st.selectbox(
        "Family Size",
        ["GT3", "LE3"]
    )

    Pstatus = st.selectbox(
        "Parents Living Together",
        ["A", "T"]
    )

    guardian = st.selectbox(
        "Guardian",
        ["father", "mother", "other"]
    )

    traveltime = st.slider(
        "Travel Time",
        1,
        4,
        1
    )

    studytime = st.slider(
        "Study Time",
        1,
        4,
        2
    )

    failures = st.slider(
        "Past Failures",
        0,
        3,
        0
    )

with col2:

    Medu = st.slider(
        "Mother Education",
        0,
        4,
        2
    )

    Fedu = st.slider(
        "Father Education",
        0,
        4,
        2
    )

    Mjob = st.selectbox(
        "Mother Job",
        [
            "at_home",
            "health",
            "other",
            "services",
            "teacher"
        ]
    )

    Fjob = st.selectbox(
        "Father Job",
        [
            "at_home",
            "health",
            "other",
            "services",
            "teacher"
        ]
    )

    reason = st.selectbox(
        "Reason",
        [
            "course",
            "home",
            "other",
            "reputation"
        ]
    )

    schoolsup = st.selectbox(
        "School Support",
        ["no", "yes"]
    )

    famsup = st.selectbox(
        "Family Support",
        ["no", "yes"]
    )

    paid = st.selectbox(
        "Extra Paid Classes",
        ["no", "yes"]
    )

    activities = st.selectbox(
        "Extra Activities",
        ["no", "yes"]
    )

st.markdown("---")


# Lifestyle Information

st.header("🏡 Lifestyle Information")

col3, col4 = st.columns(2)

with col3:

    nursery = st.selectbox(
        "Attended Nursery",
        ["no", "yes"]
    )

    higher = st.selectbox(
        "Higher Education",
        ["no", "yes"]
    )

    internet = st.selectbox(
        "Internet Access",
        ["no", "yes"]
    )

    romantic = st.selectbox(
        "Romantic Relationship",
        ["no", "yes"]
    )

    famrel = st.slider(
        "Family Relationship",
        1,
        5,
        3
    )

    freetime = st.slider(
        "Free Time",
        1,
        5,
        3
    )

with col4:

    goout = st.slider(
        "Going Out",
        1,
        5,
        3
    )

    Dalc = st.slider(
        "Weekday Alcohol",
        1,
        5,
        1
    )

    Walc = st.slider(
        "Weekend Alcohol",
        1,
        5,
        1
    )

    health = st.slider(
        "Health",
        1,
        5,
        3
    )

    absences = st.slider(
        "Absences",
        0,
        93,
        2
    )

st.markdown("---")


# Academic Performance


st.header("📚 Academic Performance")

col5, col6 = st.columns(2)

with col5:

    G1 = st.slider(
        "First Period Grade (G1)",
        0,
        20,
        10
    )

with col6:

    G2 = st.slider(
        "Second Period Grade (G2)",
        0,
        20,
        10
    )

st.markdown("---")

colA, colB = st.columns(2)

with colA:
    predict = st.button(
        "🎯 Predict Final Grade",
        use_container_width=True
    )

with colB:
    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

if reset:
    st.session_state.clear()
    st.rerun()
    

# Prediction


if predict:


    school_map = {
        "GP": 0,
        "MS": 1
    }

    sex_map = {
        "F": 0,
        "M": 1
    }

    address_map = {
        "R": 0,
        "U": 1
    }

    famsize_map = {
        "GT3": 0,
        "LE3": 1
    }

    pstatus_map = {
        "A": 0,
        "T": 1
    }

    guardian_map = {
        "father": 0,
        "mother": 1,
        "other": 2
    }

    job_map = {
        "at_home": 0,
        "health": 1,
        "other": 2,
        "services": 3,
        "teacher": 4
    }

    reason_map = {
        "course": 0,
        "home": 1,
        "other": 2,
        "reputation": 3
    }

    yesno_map = {
        "no": 0,
        "yes": 1
    }


    data = {
        "school": school_map[school],
        "sex": sex_map[sex],
        "age": age,
        "address": address_map[address],
        "famsize": famsize_map[famsize],
        "Pstatus": pstatus_map[Pstatus],
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": job_map[Mjob],
        "Fjob": job_map[Fjob],
        "reason": reason_map[reason],
        "guardian": guardian_map[guardian],
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": yesno_map[schoolsup],
        "famsup": yesno_map[famsup],
        "paid": yesno_map[paid],
        "activities": yesno_map[activities],
        "nursery": yesno_map[nursery],
        "higher": yesno_map[higher],
        "internet": yesno_map[internet],
        "romantic": yesno_map[romantic],
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }



    input_df = pd.DataFrame([data])


    input_df = input_df.reindex(columns=feature_names)


    prediction = model.predict(input_df)

    grade = float(prediction[0])


    grade = max(0, min(20, grade))



    st.markdown("---")

    st.header("🎯 Prediction Result")

    st.metric(
        label="Predicted Final Grade (G3)",
        value=f"{grade:.2f} / 20"
    )

    st.progress(int((grade / 20) * 100))

    st.write(
        f"### Percentage : {(grade/20)*100:.1f}%"
    )

    if grade >= 16:

        st.success("🏆 Outstanding Performance!")
        st.balloons()

    elif grade >= 14:

        st.success("🌟 Very Good Performance!")

    elif grade >= 12:

        st.info("👍 Good Performance!")

    elif grade >= 10:

        st.info("✅ Pass")

    else:

        st.error("📚 Needs Improvement")

    st.markdown("### Performance Level")

    if grade >= 16:
        st.write("⭐⭐⭐⭐⭐ Outstanding")

    elif grade >= 14:
        st.write("⭐⭐⭐⭐ Very Good")

    elif grade >= 12:
        st.write("⭐⭐⭐ Good")

    elif grade >= 10:
        st.write("⭐⭐ Pass")

    else:
        st.write("⭐ Fail")


    st.sidebar.markdown("---")
    st.sidebar.subheader("Prediction")
    st.sidebar.metric("Predicted G3", f"{grade:.2f}")



st.markdown("---")

with st.expander("ℹ About This Project"):

    st.write("""
### Student Performance Prediction

  This application predicts a student's final grade (G3)
using a Random Forest Regressor model trained on the
Student Performance Dataset.

**Course**
COM763 – Machine Learning

  **Technologies Used**

- Python
 - Streamlit
- Pandas
 - Scikit-learn
- Joblib

**Machine Learning Model**

 Random Forest Regressor

**Developer**

  W R A Shehani Geethanjali Amarasiri
""")