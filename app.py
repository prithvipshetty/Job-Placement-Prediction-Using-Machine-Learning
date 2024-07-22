# import numpy as np
# import pandas as pd
# from PIL import Image
# import streamlit as st
# import pickle
#
# lg = pickle.load(open('placement.pkl','rb'))
#
# # web app
# img = Image.open('Job-Placement-Agency.jpg')
# st.image(img,width=650)
# st.title("Job Placement Predictor")
# st.write("""
# Welcome to the Job Placement Prediction Model. This app uses a machine learning model to predict whether a person is likely to be placed based on various features. Please provide the required information in the input field below.
# """)
# input_text = st.text_input("Enter your ssc percentage, hsc percentage, degree percentage, employee test percentage, mba percentage, gender, ssc board, hsc board, hsc subject(Commerce), hsc subject(Science), undergrad degree, undergrad degree(Sci&Tech), work experience, specialisation in Mkt&HR")
# if input_text:
#     input_list = input_text.split(',')
#     np_df = np.asarray(input_list,dtype=float)
#     prediction = lg.predict(np_df.reshape(1,-1))
#
#     if prediction[0] == 1:
#         st.write("This Person Is Placed")
#     else:
#         st.write("This Person is not Placed")




#
# import numpy as np
# import pandas as pd
# from PIL import Image
# import streamlit as st
# import pickle
#
# # Load the model
# lg = pickle.load(open('placement.pkl', 'rb'))
#
# # Web app interface
# st.set_page_config(page_title="Job Placement Prediction Model", layout="centered")
#
# # Header and Image
# img = Image.open('Job-Placement-Agency.jpg')
# st.image(img, width=650)
# st.title("Job Placement Prediction Model")
#
# # Description
# st.write("""
# Welcome to the **Job Placement Prediction Model**. This application leverages a machine learning model to predict the likelihood of a candidate being placed based on various educational and personal features.
#
# ### How to Use:
# 1. Enter the required features in the input field below, separated by commas.
# 2. Click the **Enter** button to get the prediction result.
#
# ### Required Features:
# - **SSC Percentage**: Secondary School Certificate percentage (e.g., 85.0).
# - **HSC Percentage**: Higher Secondary Certificate percentage (e.g., 88.0).
# - **Degree Percentage**: Undergraduate degree percentage (e.g., 75.0).
# - **Employee Test Percentage**: Employee test percentage (e.g., 80.0).
# - **MBA Percentage**: MBA degree percentage (e.g., 85.0).
# - **Gender**: Enter 1 for male, 0 for female.
# - **SSC Board**: Enter 1 for Central, 0 for Others.
# - **HSC Board**: Enter 1 for Central, 0 for Others.
# - **HSC Subject (Commerce)**: Enter 1 for Commerce, 0 for Others.
# - **HSC Subject (Science)**: Enter 1 for Science, 0 for Others.
# - **Undergrad Degree**: Enter 1 for Sci&Tech, 0 for Others.
# - **Work Experience**: Enter 1 for Yes, 0 for No.
# - **Specialisation in Mkt&HR**: Enter 1 for Yes, 0 for No.
#
# """)
#
# # Input form
# input_text = st.text_input("Enter the features as a comma-separated list:")
#
# if input_text:
#     input_list = input_text.split(',')
#     try:
#         np_df = np.asarray(input_list, dtype=float)
#         prediction = lg.predict(np_df.reshape(1, -1))
#
#         if prediction[0] == 1:
#             st.success("This Person Is Placed")
#         else:
#             st.warning("This Person is not Placed")
#     except ValueError:
#         st.error("Please enter valid numeric values for all features.")
#



import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import pickle

# Load the model
lg = pickle.load(open('placement.pkl', 'rb'))

# Set page configuration
st.set_page_config(page_title="Job Placement Predictor", layout="centered")

# Custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?fit=crop&w=1920&h=1080&q=80');
        background-size: cover;
    }
    .content {
        background: rgba(30, 30, 30, 0.85);
        color: white;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Image
# img = Image.open('Job-Placement-Agency.jpg')
# st.image(img, width=650)
st.title("Job Placement Predictor")

# Description
st.markdown("""
<div class="content">
Welcome to the Job Placement Predictor. This application leverages a machine learning model to predict the likelihood of a candidate being placed based on various educational features.

### How to Use:
1. Enter the required features in the input field below, separated by commas.
2. Click the **Enter** button to get the prediction result.

### Required Features:
- **SSC Percentage**: Secondary School Certificate percentage (e.g., 85.0).
- **HSC Percentage**: Higher Secondary Certificate percentage (e.g., 88.0).
- **Degree Percentage**: Undergraduate degree percentage (e.g., 75.0).
- **Employee Test Percentage**: Employee test percentage (e.g., 80.0).
- **MBA Percentage**: MBA degree percentage (e.g., 85.0).
- **Gender**: Enter 1 for male, 0 for female.
- **SSC Board**: Enter 1 for Central, 0 for Others.
- **HSC Board**: Enter 1 for Central, 0 for Others.
- **HSC Subject (Commerce)**: Enter 1 for Commerce, 0 for Others.
- **HSC Subject (Science)**: Enter 1 for Science, 0 for Others.
- **Undergrad Degree**: Enter 1 for Sci&Tech, 0 for Others.
- **Work Experience**: Enter 1 for Yes, 0 for No.
- **Specialisation in Mkt&HR**: Enter 1 for Yes, 0 for No.
</div>
""", unsafe_allow_html=True)

# Input form
input_text = st.text_input("Enter the features as a comma-separated list:")

if input_text:
    input_list = input_text.split(',')
    try:
        np_df = np.asarray(input_list, dtype=float)
        prediction = lg.predict(np_df.reshape(1, -1))

        if prediction[0] == 1:
            st.success("Congratulations! You have the chances of getting placed.")
        else:
            st.warning("Sorry for this time! Work harder and visit again.")
    except ValueError:
        st.error("Please enter valid numeric values for all features.")


