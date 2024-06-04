import streamlit as st
import joblib

def main():
    st.set_page_config(
        page_title="Health Cost Predictor",
        page_icon="🏥",
        layout="centered",
        initial_sidebar_state="auto",
    )

    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center">Health Cost Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('gb_model_joblib')

    st.write("Please fill in the following information to get an estimate of your health insurance cost.")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Enter Your Age", 18, 100, 30)
        sex = st.selectbox("Sex", ("Male", "Female"))
        bmi = st.number_input("Enter Your BMI Value", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    with col2:
        num_children = st.slider("Enter Number of Children", 0, 4, 0)
        is_smoker = st.selectbox("Smoker", ("Yes", "No"))
        region = st.slider("Enter Your Region [1-4]", 1, 4, 1)

    if st.button('Predict'):
        if sex == "Male":
            sex_encoded = 1
        else:
            sex_encoded = 0

        if is_smoker == "Yes":
            is_smoker_encoded = 1
        else:
            is_smoker_encoded = 0

        prediction = model.predict([[age, sex_encoded, bmi, num_children, is_smoker_encoded, region]])
        st.balloons()
        st.success(f'Your estimated health insurance cost is ${round(prediction[0], 2)}')

if __name__ == '__main__':
    main()
