import streamlit as st
import pickle

# Load the trained model
with open("trained_model.pkl", "rb") as f:
    model = pickle.load(f)

# Set up the Streamlit app
st.title("Student Pass Prediction App")
st.write("Enter the student's details to predict if they have passed or not.")

# Example input fields - adjust these based on your model's requirements
# For instance, you might have fields for test scores, attendance, assignments, etc.
Midterm1 = st.number_input("Enter Exam Score", min_value=0, max_value=100, step=1)
Attendance = st.number_input("Enter Attendance Percentage", min_value=0, max_value=100, step=1)
Midterm2 = st.number_input("Enter Assignment Score", min_value=0, max_value=100, step=1)

# Prepare the input for prediction
# Adjust this list of inputs to match your model's expected input structure
student_features = [[Midterm1, Attendance, Midterm2]]

# Make prediction when the button is clicked
if st.button("Predict"):
    try:
        # Get prediction from the model
        prediction = model.predict(student_features)
        
        # Interpret the prediction
        if prediction[0] == 1:
            st.success("The student is predicted to have passed.")
        else:
            st.warning("The student is predicted to have not passed.")
            
    except Exception as e:
        st.write("An error occurred during prediction:", e)
