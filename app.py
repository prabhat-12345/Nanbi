import streamlit as st

# Page setup
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# Custom Styles
st.markdown("""
    <style>
    .big-title {
        font-size: 45px !important;
        font-weight: bold;
        color: #FF4B4B;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .wishes {
        font-size: 20px;
        color: #333333;
        text-align: center;
        line-height: 1.8;
    }
    .card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.1);
        border: 2px solid #FF4B4B;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🎉 Happy Birthday to my Favourite Student! 🎂</p>', unsafe_allow_html=True)

# Celebration Trigger Button
if st.button("✨ Click for a Surprise! ✨", use_container_width=True):
    st.balloons() # Automatic balloon animation on cloud
    
    st.markdown("""
    <div class="card">
        <h2 style='text-align: center; color: #FF7676;'>Dear Student, 🌟</h2>
        <p class="wishes">
            Aap jaise mehnati aur honhar student ka teacher hona mere liye garv ki baat hai. 
            Aapki curiosity aur sikhne ki chahat aapko bahut aage le jayegi.<br><br>
            God bless you with endless success, happiness, and good health. 
            Hamesha aise hi muskurate raho aur nayi oonchaiyon ko chhuo!
        </p>
        <h3 style='text-align: center; color: #FF4B4B;'>🎂 Have a Blast! 🎈</h3>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; color: #666;'>Upar diye gaye button par click karein surprise dekhne ke liye! 👀</p>", unsafe_allow_html=True)
  
