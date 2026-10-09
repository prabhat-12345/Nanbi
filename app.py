import streamlit as st

# Premium Page Configuration
st.set_page_config(
    page_title="Happy Birthday | Excellence Awaits", 
    page_icon="✨", 
    layout="centered"
)

# Premium Custom CSS & CSS Keyframe Animations
st.markdown("""
    <style>
    /* Premium Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #111827 0%, #312E81 100%);
    }
    
    /* Elegant Title with Glow and Fade-in Animation */
    .premium-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        font-size: 42px !important;
        font-weight: 700;
        background: linear-gradient(to right, #FDE68A, #F59E0B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 1px;
        animation: fadeInDown 1.5s ease-out;
    }
    
    .premium-subtitle {
        color: #9CA3AF;
        text-align: center;
        font-size: 16px;
        font-style: italic;
        margin-bottom: 30px;
        animation: fadeIn 2s ease-out;
    }

    /* Luxury Card Design */
    .luxury-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(253, 230, 138, 0.2);
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
        animation: scaleUp 1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* English Quote Typography */
    .quote-text {
        font-family: 'Lora', 'Georgia', serif;
        font-size: 24px;
        color: #FEE2E2;
        line-height: 1.6;
        text-align: center;
        font-style: italic;
        margin-bottom: 25px;
    }

    .author-tag {
        font-size: 14px;
        color: #F59E0B;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
        margin-bottom: 30px;
    }

    /* Message Typography */
    .message-text {
        font-family: 'Inter', sans-serif;
        font-size: 17px;
        color: #D1D5DB;
        text-align: center;
        line-height: 1.8;
    }

    /* Keyframe Animations */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes scaleUp {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    /* Premium Styled Button Overrides */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 24px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(180, 83, 9, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(180, 83, 9, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Layout Setup
st.markdown('<h1 class="premium-title">A Celebration of Excellence</h1>', unsafe_allow_html=True)
st.markdown('<p class="premium-subtitle">Dedicated to an exceptional student on their special day</p>', unsafe_allow_html=True)

# Button to unlock premium view & triggers high-end cloud animation
if st.button("✨ Reveal Your Birthday Wish ✨", use_container_width=True):
    st.balloons() # Premium built-in cloud animations
    st.snow()     # Soft floating particle effect overlay
    
    # Cleaned single line HTML string to avoid rendering issues on Streamlit Cloud
    html_content = (
        '<div class="luxury-card">'
        '<p class="quote-text">"The future belongs to those who believe in the beauty of their dreams."</p>'
        '<p class="author-tag">— Eleanor Roosevelt</p>'
        '<p class="message-text"><strong>Happy Birthday!</strong><br><br>'
        'It is a profound privilege to guide a student with your intellect, dedication, and unwavering curiosity. '
        'Your potential is limitless, and I have no doubt that your journey ahead will be nothing short of extraordinary.<br><br>'
        'May this year unlock brilliant new opportunities, absolute happiness, and the grand success you so deeply deserve. Keep shining bright!</p>'
        '</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; color: #6B7280; font-size: 15px; margin-top: 50px;'>Click the golden portal above to reveal your message.</p>", unsafe_allow_html=True)
    
