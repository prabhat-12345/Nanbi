import streamlit as st
import time

# Premium Page Configuration with colorful emojis
st.set_page_config(
    page_title="Happy Birthday Nandanipriyadarshini! 🌟", 
    page_icon="🎂", 
    layout="centered"
)

# Premium Custom CSS for Vivid Colors, Glowing Text, and Fluid Animations
st.markdown("""
    <style>
    /* Vibrant Premium Cosmic Background */
    .stApp {
        background: linear-gradient(135deg, #0f0c20 0%, #24243e 50%, #300030 100%);
    }
    
    /* Glowing Title with Colorful Gradient and Animation */
    .vibrant-title {
        font-family: 'Playfair Display', 'Georgia', serif;
        font-size: 45px !important;
        font-weight: 900;
        background: linear-gradient(45deg, #FF3366, #FF9933, #FFCC00, #33CCFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 1.5px;
        filter: drop-shadow(0px 2px 10px rgba(255,51,102,0.3));
        animation: glowPulse 2s infinite alternate;
    }
    
    .vibrant-subtitle {
        color: #E0E0E0;
        text-align: center;
        font-size: 18px;
        font-weight: 500;
        letter-spacing: 1px;
        margin-bottom: 30px;
    }

    /* Luxury Holographic Card Design */
    .luxury-glow-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 204, 0, 0.4);
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 0 30px rgba(255, 153, 51, 0.25);
        margin-top: 25px;
        animation: popUp 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* Student Name Spotlight Panel */
    .name-spotlight {
        background: linear-gradient(90deg, #FF3366, #FF9933);
        color: white !important;
        font-size: 28px !important;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        border-radius: 15px;
        margin-top: 25px;
        box-shadow: 0 10px 25px rgba(255, 51, 102, 0.4);
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    /* English Quote Typography */
    .quote-text {
        font-family: 'Lora', 'Georgia', serif;
        font-size: 24px;
        color: #FFF5E6;
        line-height: 1.6;
        text-align: center;
        font-style: italic;
        margin-bottom: 20px;
    }

    .author-tag {
        font-size: 14px;
        color: #FFCC00;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 700;
        margin-bottom: 35px;
    }

    /* Keyframe Animations */
    @keyframes glowPulse {
        0% { filter: drop-shadow(0px 2px 8px rgba(255,51,102,0.3)); }
        100% { filter: drop-shadow(0px 4px 20px rgba(51,204,255,0.6)); }
    }
    @keyframes popUp {
        0% { opacity: 0; transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    /* Colorful Custom Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #FF3366 0%, #FF9933 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 15px 30px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 25px rgba(255, 51, 102, 0.5) !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
        letter-spacing: 1px;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.03) translateY(-3px) !important;
        background: linear-gradient(45deg, #FF9933 0%, #FF3366 100%) !important;
        box-shadow: 0 8px 30px rgba(255, 153, 51, 0.7) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Layout Header Structure
st.markdown('<h1 class="vibrant-title">✨ A Celebration of Excellence ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="vibrant-subtitle">🌈 Dedicated to an exceptional mind on her special day 📚</p>', unsafe_allow_html=True)

# Main Action Button for Celebration
if st.button("🎁 Open Your Magical Birthday Surprise 🌟", use_container_width=True):
    # Multi-layered rich animation effects on cloud runtime
    st.balloons() 
    st.snow()     
    
    # Safe Single-string clean HTML rendering framework
    card_html = (
        '<div class="luxury-glow-card">'
        '    <p class="quote-text">"The future belongs to those who believe in the beauty of their dreams."</p>'
        '    <p class="author-tag">🏆 — Eleanor Roosevelt</p>'
        '    <div style="font-family: \'Inter\', sans-serif; font-size: 17px; color: #E5E7EB; text-align: center; line-height: 1.8;">'
        '        <strong>Happy Birthday! 🎉🎂🎈</strong><br><br>'
        '        It is a profound privilege to guide a student with your brilliant intellect, '
        '        relentless dedication, and unwavering curiosity. Your potential is absolutely limitless, '
        '        and I have no doubt that your journey ahead will be nothing short of extraordinary.🚀<br><br>'
        '        May this wonderful year unlock dazzling new opportunities, profound happiness, '
        '        and the spectacular success you so deeply deserve. Keep shining like the bright star you are!🌟⭐'
        '    </div>'
        '    <div class="name-spotlight">✨ Happy Birthday Nandanipriyadarshini! 👑🎂</div>'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Bottom success toast banner
    st.toast("Wishing you the most colorful and splendid birthday ever! 🥳🧁🎉", icon="💖")
else:
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 16px; margin-top: 60px; font-weight: 500;'>👉 Click the magical glowing portal above to reveal your message!</p>", unsafe_allow_html=True)
    
